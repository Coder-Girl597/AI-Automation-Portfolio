# CS Department FAQ AI Assistant

## Description

Answers common Computer Science department questions using a configured AI model. Import the n8n workflow, configure credentials and trigger, then test with a question. Verify actual department office hours before deployment.

## Workflow

`Question/Webhook → n8n → Gemini → Answer (optional unanswered-query log)`

## How to run

1. Open the original project and make a safe copy for testing.
2. Configure the required credentials and permissions. Store secrets in environment variables, Apps Script properties, or GitHub Actions secrets—not in this repository.
3. Import or copy the original workflow/source files into this folder.
4. Follow the setup notes in the project and run a test with sample data.
5. Confirm the output and review logs for errors.

## Files to add

- [ ] **Original export:** n8n workflow JSON export. Save it here using the appropriate filename. It has not been attached yet.
- [ ] **Screenshots:** Add genuine screenshots to the `screenshots/` folder (workflow overview, successful test, and output).
- [ ] **Sensitive-data check:** Remove API keys, passwords, tokens, personal email content, and identifiable student data before committing.

## Evidence status

Documentation is prepared. Original exports and screenshots are pending upload from the working project.
