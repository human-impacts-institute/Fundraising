# AGENTS.md — Fundraising Dashboard

## Session start protocol
1. Read `memory/STATE.md` — know where things stand before doing anything
2. Read `memory/context.md` if this is your first session or if STATE.md references open questions

## Session end protocol
1. Update `memory/STATE.md` with what changed and what's next
2. If a significant decision was made → append to `memory/DECISIONS.md`
3. If an error or workaround was found → append to `memory/LESSONS.md`

---

## CRITICAL RULE: No new folders without approval
- NEVER create folders outside the authorized structure below
- If you need a new folder, STOP and ask first
- Every new file must go into an existing authorized folder

---

## Authorized folder structure

```
Fundraising Dashboard/
├── AGENTS.md
├── context.md            (alias — canonical copy is memory/context.md)
├── README.md
├── requirements.txt
├── netlify.toml
├── wrangler.toml
├── worker.js
├── scripts/              → Python scripts only
├── dashboards/           → Auto-generated output — NEVER edit manually
├── data/                 → source_url.txt + CSV snapshots
├── docs/                 → Netlify site files
│   └── assets/           → JS, CSS, images, config
└── memory/               → Persistent session memory
    ├── context.md
    ├── STATE.md
    ├── DECISIONS.md
    ├── LESSONS.md
    └── SCRATCH.md
```

---

## Naming conventions
- Python files: `snake_case.py`
- JS/CSS files: `kebab-case.js`
- Memory files: `UPPER_CASE.md` (except context.md)
- No spaces in file or folder names

---

## Before creating any file or folder
1. Run `find . -type d -not -path '*/\.*'` to see current structure
2. Verify the destination folder already exists
3. If it doesn't, STOP and ask the user
4. NEVER run `mkdir` without explicit approval

---

## Critical rules for this project

### dashboards/ is generated — never edit it
`dashboards/grants_dashboard.md` is overwritten on every `python3 scripts/score_grants.py` run.
Edits there will be lost. If you need to change the output format, edit `scripts/score_grants.py`.

### docs/index.html is also generated
`docs/index.html` is overwritten by `score_grants.py`. Same rule applies.

### data/source_url.txt is a secret
Never log its contents, never paste it in output, never commit it if it appears in git status.
The CI pipeline uses the `SOURCE_URL` environment variable instead.

### Test scoring changes locally before pushing
Run `python3 scripts/score_grants.py` from the project root and verify:
1. `dashboards/grants_dashboard.md` looks correct
2. `docs/index.html` renders correctly in a browser
3. No Python errors or warnings

### Cloudflare Worker changes require re-deployment
After editing `worker.js`, run `wrangler deploy` to push changes.
The Worker must have `GITHUB_TOKEN` set as a secret in the Cloudflare dashboard (not in wrangler.toml).
