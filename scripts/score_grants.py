#!/usr/bin/env python3
"""
score_grants.py

Pulls the "All Potential Grants" tab from Google Sheets as CSV, calculates:
1) Review Priority Score (what to update or research next)
2) Application Priority Score (what to apply to next, when deadlines exist)

Outputs:
- dashboards/grants_dashboard.md
- data/scored_grants.csv (optional snapshot)

Setup
1) Create: data/source_url.txt
   Put this exact URL inside:
   https://docs.google.com/spreadsheets/d/14UTA60hSKQFvoE95IbHURWwx9N55mlGL9ErJJfpLxMI/gviz/tq?tqx=out:csv&sheet=All%20Potential%20Grants

2) Run
   python3 scripts/score_grants.py
"""

from __future__ import annotations

import csv
import os
import re
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import requests


# ----------------------------
# Config: your current columns
# ----------------------------
COL_ORG = "Organization"
COL_PRIORITY = "Priority"
COL_REL = "Relationship Status (Select all that apply)"
COL_GEO = "Funding Geography (i.e. NYC, FRANCE, INTERNATIONAL, ALL)"
COL_LOI = "LOI DEADLINE\nMM/DD/YEAR"
COL_APP = "Application Deadline (MM/DD/YEAR"
COL_LAST_UPDATED = "Date Last Updated"
COL_INFO_SITE = "Information Website"
COL_APP_SITE = "APPLICATION WEBSITE"
COL_WHAT_FUND = "What they Fund"
COL_NOTES = "Notes"

PROGRAM_COLS = [
    "All",
    "C3 Lab",
    "CCA",
    "UEHL",
    "General Support",
    "Fellowship",
    "Internships",
    "YAC",
    "Workshops",
    "Salons",
    "Stories",
]

SOURCE_URL_FILE = os.path.join("data", "source_url.txt")
DASHBOARD_PATH = os.path.join("dashboards", "grants_dashboard.md")
SCORED_CSV_PATH = os.path.join("data", "scored_grants.csv")


# ----------------------------
# Helpers
# ----------------------------
def ensure_dirs() -> None:
    os.makedirs("data", exist_ok=True)
    os.makedirs("scripts", exist_ok=True)
    os.makedirs("dashboards", exist_ok=True)


def read_source_url() -> str:
    if not os.path.exists(SOURCE_URL_FILE):
        raise FileNotFoundError(
            f"Missing {SOURCE_URL_FILE}. Create it and paste your Google Sheets CSV URL."
        )
    with open(SOURCE_URL_FILE, "r", encoding="utf-8") as f:
        url = f.read().strip()
    if not url.startswith("https://docs.google.com/spreadsheets/"):
        raise ValueError("source_url.txt does not look like a Google Sheets URL.")
    return url


def fetch_csv_to_df(url: str) -> pd.DataFrame:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    content = resp.content.decode("utf-8", errors="replace")
    from io import StringIO

    df = pd.read_csv(StringIO(content))
    return df


def norm_str(x: Any) -> str:
    if x is None:
        return ""
    if isinstance(x, float) and pd.isna(x):
        return ""
    return str(x).strip()


def truthy_cell(x: Any) -> bool:
    s = norm_str(x).lower()
    if s in ("", "0", "no", "false", "n", "na", "n/a", "none"):
        return False
    if s in ("1", "yes", "true", "y", "x", "checked", "t"):
        return True
    # sometimes users type program names or notes inside cells
    # if it is non-empty and not an obvious negative, treat as True
    return True


def parse_date_mmddyyyy(x: Any) -> Optional[date]:
    s = norm_str(x)
    if not s:
        return None

    # Handle common variants: 1/5/2026, 01/05/26, 2026-01-05
    s = s.replace("\\", "/").replace("-", "/")
    s = re.sub(r"\s+", " ", s).strip()

    for fmt in ("%m/%d/%Y", "%m/%d/%y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue

    # Some cells may contain extra text
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", s)
    if m:
        mm, dd, yy = m.group(1), m.group(2), m.group(3)
        if len(yy) == 2:
            yy = "20" + yy
        try:
            return datetime.strptime(f"{mm}/{dd}/{yy}", "%m/%d/%Y").date()
        except ValueError:
            return None

    return None


def priority_weight(p: str) -> int:
    s = norm_str(p).upper()
    if "HIGH" in s:
        return 30
    if "MED" in s:
        return 15
    if "LOW" in s:
        return 5
    if s == "":
        return 10
    return 10


def relationship_score(rel: str) -> int:
    s = norm_str(rel).lower()
    if not s:
        return 0

    positive = 0
    if any(k in s for k in ["warm", "existing", "prior", "past grantee", "met", "connection", "intro"]):
        positive += 10
    if any(k in s for k in ["active", "in conversation", "ongoing"]):
        positive += 5
    if any(k in s for k in ["cold", "no relationship"]):
        positive -= 5

    return positive


def effort_penalty(notes: str, what_fund: str) -> int:
    s = (norm_str(notes) + " " + norm_str(what_fund)).lower()
    penalty = 0
    if any(k in s for k in ["invitation only", "invite-only", "by invitation"]):
        penalty += 15
    if any(k in s for k in ["rolling", "open", "ongoing"]):
        penalty -= 3  # easier scheduling, not a penalty
    if any(k in s for k in ["letter of inquiry portal", "complex", "lengthy", "heavy reporting"]):
        penalty += 5
    return max(0, penalty)


def staleness_score(last_updated: Optional[date]) -> int:
    today = date.today()
    if last_updated is None:
        return 12
    days = (today - last_updated).days
    if days > 365:
        return 15
    if days > 180:
        return 10
    if days > 90:
        return 5
    return 0


def urgency_score(deadline: Optional[date]) -> int:
    if deadline is None:
        return 0
    today = date.today()
    delta = (deadline - today).days
    if delta < 0:
        return -10
    if delta <= 30:
        return 25
    if delta <= 60:
        return 18
    if delta <= 120:
        return 10
    if delta <= 240:
        return 5
    return 1


def pick_next_deadline(loi: Optional[date], app: Optional[date]) -> Optional[date]:
    # If LOI exists and is before app, it drives urgency
    candidates = [d for d in [loi, app] if d is not None]
    if not candidates:
        return None
    return min(candidates)


def safe_url(u: Any) -> str:
    s = norm_str(u)
    if s and not s.lower().startswith(("http://", "https://")):
        return "https://" + s
    return s


# ----------------------------
# Scoring
# ----------------------------
@dataclass
class Scores:
    review: int
    apply: Optional[int]
    program_matches: int
    next_deadline: Optional[date]
    missing_deadlines: bool
    missing_sites: bool


def compute_scores(row: pd.Series) -> Scores:
    p_weight = priority_weight(row.get(COL_PRIORITY, ""))
    rel_score = relationship_score(row.get(COL_REL, ""))
    notes = norm_str(row.get(COL_NOTES, ""))
    what_fund = norm_str(row.get(COL_WHAT_FUND, ""))

    loi = parse_date_mmddyyyy(row.get(COL_LOI, ""))
    app = parse_date_mmddyyyy(row.get(COL_APP, ""))
    next_deadline = pick_next_deadline(loi, app)

    last_updated = parse_date_mmddyyyy(row.get(COL_LAST_UPDATED, ""))

    # Program match count
    pm = 0
    for c in PROGRAM_COLS:
        if c in row.index and truthy_cell(row.get(c, "")):
            pm += 1

    missing_deadlines = (loi is None and app is None)
    missing_sites = (not norm_str(row.get(COL_INFO_SITE, "")) and not norm_str(row.get(COL_APP_SITE, "")))

    # Review score: focus on what needs research/update
    review = 0
    review += p_weight
    review += pm * 4
    review += staleness_score(last_updated)
    review += 20 if missing_deadlines else (10 if (loi is None) ^ (app is None) else 0)
    review += 5 if missing_sites else 0
    if not norm_str(row.get(COL_WHAT_FUND, "")):
        review += 5
    if not norm_str(row.get(COL_GEO, "")):
        review += 3

    # Application score: only when any deadline exists
    apply: Optional[int] = None
    if next_deadline is not None:
        apply = 0
        apply += (pm * 6)
        apply += int(p_weight / 2)
        apply += rel_score
        apply += urgency_score(next_deadline)
        apply -= effort_penalty(notes, what_fund)

    return Scores(
        review=review,
        apply=apply,
        program_matches=pm,
        next_deadline=next_deadline,
        missing_deadlines=missing_deadlines,
        missing_sites=missing_sites,
    )


# ----------------------------
# Dashboard rendering
# ----------------------------
def fmt_date(d: Optional[date]) -> str:
    if d is None:
        return ""
    return d.strftime("%Y-%m-%d")


def render_table(rows: List[Dict[str, Any]], title: str, max_rows: int = 25) -> str:
    lines: List[str] = []
    lines.append(f"## {title}")
    lines.append("")
    lines.append("| Rank | Organization | Priority | Next deadline | Programs | Website | Notes |")
    lines.append("| ---: | --- | --- | --- | ---: | --- | --- |")

    for i, r in enumerate(rows[:max_rows], start=1):
        org = norm_str(r.get(COL_ORG, ""))
        pri = norm_str(r.get(COL_PRIORITY, ""))
        nd = fmt_date(r.get("Next Deadline"))
        pm = r.get("Program Matches", 0)

        site = safe_url(r.get(COL_INFO_SITE, "")) or safe_url(r.get(COL_APP_SITE, ""))
        site_md = f"[link]({site})" if site else ""

        notes = norm_str(r.get(COL_NOTES, ""))
        notes = re.sub(r"\s+", " ", notes).strip()
        if len(notes) > 80:
            notes = notes[:77] + "..."

        lines.append(f"| {i} | {org} | {pri} | {nd} | {pm} | {site_md} | {notes} |")

    lines.append("")
    return "\n".join(lines)


def write_dashboard(df: pd.DataFrame) -> None:
    today = date.today().isoformat()

    # Summary stats
    total = len(df)
    missing_deadlines = int(df["Missing Deadlines"].sum())
    missing_sites = int(df["Missing Sites"].sum())
    have_deadlines = total - missing_deadlines

    # Sort lists
    update_queue = df.sort_values(["Review Priority Score", COL_PRIORITY, COL_ORG], ascending=[False, True, True])
    apply_next = df[df["Application Priority Score"].notna()].copy()
    apply_next = apply_next.sort_values(["Application Priority Score", "Next Deadline"], ascending=[False, True])

    md: List[str] = []
    md.append(f"# Grants Dashboard")
    md.append("")
    md.append(f"Last refreshed: {today}")
    md.append("")
    md.append("### Snapshot")
    md.append("")
    md.append(f"- Total funders: {total}")
    md.append(f"- Funders missing both deadlines: {missing_deadlines}")
    md.append(f"- Funders missing websites: {missing_sites}")
    md.append(f"- Funders with at least one deadline: {have_deadlines}")
    md.append("")

    md.append(render_table(update_queue.to_dict(orient="records"), "Update Queue (research and refresh first)", 30))
    md.append(render_table(apply_next.to_dict(orient="records"), "Apply Next (only includes funders with deadlines)", 30))

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md))


def main() -> None:
    ensure_dirs()
    url = read_source_url()
    df = fetch_csv_to_df(url)

    # Ensure key columns exist, but do not crash if some are missing
    for c in [COL_ORG, COL_PRIORITY, COL_REL, COL_LOI, COL_APP, COL_LAST_UPDATED, COL_INFO_SITE, COL_APP_SITE, COL_NOTES]:
        if c not in df.columns:
            df[c] = ""

    # Compute scores per row
    review_scores: List[int] = []
    apply_scores: List[Optional[int]] = []
    program_counts: List[int] = []
    next_deadlines: List[Optional[date]] = []
    missing_deadlines_list: List[bool] = []
    missing_sites_list: List[bool] = []

    for _, row in df.iterrows():
        s = compute_scores(row)
        review_scores.append(s.review)
        apply_scores.append(s.apply)
        program_counts.append(s.program_matches)
        next_deadlines.append(s.next_deadline)
        missing_deadlines_list.append(s.missing_deadlines)
        missing_sites_list.append(s.missing_sites)

    df["Review Priority Score"] = review_scores
    df["Application Priority Score"] = apply_scores
    df["Program Matches"] = program_counts
    df["Next Deadline"] = [fmt_date(d) if d else "" for d in next_deadlines]
    df["Missing Deadlines"] = missing_deadlines_list
    df["Missing Sites"] = missing_sites_list

    # Write outputs
    write_dashboard(df)
    df.to_csv(SCORED_CSV_PATH, index=False, encoding="utf-8")

    print(f"Wrote: {DASHBOARD_PATH}")
    print(f"Wrote: {SCORED_CSV_PATH}")


if __name__ == "__main__":
    main()
