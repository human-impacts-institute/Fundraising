# Fundraising Dashboard

**HII Program:** Cross-program (supports all 5 programs — CCA, C3 Lab, UEHL, YAC, Fellowship + General Support)
**Objective:** Generate a prioritized, live fundraising dashboard from the HII Google Sheet so the team always knows what to apply to next and what to research.

---

## Key stakeholders

- **Álvaro Valencia** — project owner, runs the dashboard
- **HII team** — dashboard consumers (auth restricted to @humanimpactsinstitute.org)
- **317 funders** in the Google Sheet (source of truth)

---

## Critical dates / workflow

- Dashboard is **not on a fixed schedule** — refreshed manually via the Refresh button on the live site
- Refresh triggers a GitHub Actions workflow; takes ~35 seconds end-to-end
- Scoring recalculates on every refresh; no manual intervention needed

---

## Key files and data sources

| File / System | Role |
|---|---|
| Google Sheet (private) | Source of truth — 317 funders, all data lives here |
| `data/source_url.txt` | Holds the private Sheet CSV URL (keep secret) |
| `scripts/score_grants.py` | Core scoring + dashboard generation script |
| `docs/index.html` | Live dashboard (Netlify-hosted, auth-gated) |
| `docs/assets/refresh-config.js` | Config: Cloudflare Worker URL + GRANT_ADD_URL (TODO) |
| `worker.js` | Cloudflare Worker proxy: browser → GitHub Actions |
| `wrangler.toml` | CF Worker config (repo: human-impacts-institute/Fundraising) |
| `netlify.toml` | Netlify build config (publishes `docs/`) |

---

## Scoring algorithm (summary)

- **Review score**: priority weight + program match count × 4 + staleness + missing data flags + status + relevance
- **Application score**: (only when deadline exists) program match × 6 + urgency + relationship warmth + status − effort penalty
- Funders appear in **On Deck** (have deadline, not closed, not "not ideal") or **Review Queue** (everything else)

---

## Known constraints

- `GRANT_ADD_URL` in `refresh-config.js` is blank — quick-add form is not yet active (needs Google Apps Script Web App URL)
- Source URL is a secret; never commit it to git (it's in `data/source_url.txt` which should stay in `.gitignore` or be passed via `SOURCE_URL` env var in CI)
- Netlify Identity restricts access to @humanimpactsinstitute.org — outside users cannot see the dashboard
- CF Worker (`fundraising-refresh`) must have `GITHUB_TOKEN` set as a secret in Cloudflare dashboard
- Python runtime: requires `pandas` and `requests` (see `requirements.txt`)
