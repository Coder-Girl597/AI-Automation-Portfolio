# Automated Job Alert Monitor

## Description

Checks a configured PPSC/job page, filters relevant links using keywords, avoids repeat alerts by tracking previously seen results, and emails newly detected matches.

## Workflow

`Scheduled GitHub Actions → Python monitor → Keyword filter → seen.json → Email alert`

## Technology

Python, requests, BeautifulSoup, GitHub Actions, and email/SMTP.

## How to run

1. Install dependencies from `requirements.txt`.
2. Configure the source URL and relevant keywords.
3. Add `EMAIL_USER`, `EMAIL_PASS`, `EMAIL_TO`, `PPSC_URL`, and `KEYWORDS` as repository Actions secrets.
4. Check that the workflow file is located in the repository-root `.github/workflows/` directory. The copy in this project folder is retained as project documentation; GitHub Actions does not discover workflows from this nested location.
5. Run the workflow manually to test, then review its logs.

## Repository contents

- `monitor.py` — Python monitoring script.
- `requirements.txt` — Python dependencies.
- `seen.json` — state file used to avoid duplicate alerts.
- `github/workflows/monitor.yml` — workflow copy for project reference; move/copy it to the repository-root `.github/workflows/` to enable GitHub Actions.
- `screenshots/` — project evidence.

## Security

Never commit email passwords, API keys, tokens, or private account data. Store credentials in GitHub Actions secrets.
