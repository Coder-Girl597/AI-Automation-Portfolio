# AI Class Feedback Analyzer

## Description

Collects student feedback through Google Forms, stores responses in Google Sheets, visualizes ratings, and generates an AI-written report with Gemini. Student names and timestamps are excluded from the Gemini prompt.

## Workflow

`Google Forms → Google Sheets → Apps Script → Gemini → AI Report`

## How to run

1. Make a safe copy of the Google Form, response spreadsheet, and Apps Script project.
2. Add your Gemini API key to Apps Script Project Settings → Script Properties as `GEMINI_API_KEY`.
3. Confirm the response tab is named `Response` and check that the question columns match the script.
4. Run `generateClassFeedbackAIReport` and authorize the requested Google services.
5. Review the generated report and chart.

## Repository contents

- `SourceCode` — Apps Script source code.
- `screenshots/` — three project screenshots showing the implementation and output.

## Security

Keep API keys and identifiable student information out of this repository. Use anonymized or sample data for demonstrations.
