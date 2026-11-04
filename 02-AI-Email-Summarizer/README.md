# AI Email Summarizer

## Description

Manually processes the latest five Gmail messages and writes a concise summary, priority level (High/Medium/Low), and suggested action to a Google Sheet named `Emails`.

## Workflow

`Gmail → Apps Script → Gemini → Google Sheets`

## How to run

1. Make a safe copy of the Apps Script project and spreadsheet.
2. Add your Gemini API key to Apps Script Project Settings → Script Properties as `GEMINI_API_KEY`.
3. Confirm the `Emails` sheet and its column headers.
4. Run the summarizer function manually and authorize Gmail and Sheets access.
5. Review the generated summaries, priorities, and suggested actions.

## Repository contents

- `Script` — Apps Script source code.
- `screenshots/` — screenshot evidence of the project.

## Security

Do not commit API keys, passwords, private email content, or personal information. Use test emails or anonymized examples when demonstrating the workflow.
