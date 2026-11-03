# CS Department FAQ AI Assistant

## Description

An n8n assistant designed to answer common Computer Science department questions using a configured AI model. The exported workflow and project screenshots are included in this folder. Verify actual department information before deployment.

## Workflow

`Question / Chat Trigger → n8n → AI model → Answer`

An unanswered-query log can be added to help maintain the FAQ knowledge base.

## How to run

1. Open n8n and import `CS Department FAQ AI Agent.json`.
2. Configure the required AI model credentials and any trigger settings.
3. Test the workflow with sample questions.
4. Confirm answers against the department's official information before real use.
5. Keep credentials outside the exported workflow and repository.

## Repository contents

- `CS Department FAQ AI Agent.json` — exported n8n workflow.
- `screenshots/` — project and workflow screenshots.

## Security

Do not commit API keys, passwords, tokens, private email content, or identifiable student data.
