# AI Automation Portfolio

A collection of five practical AI and workflow-automation projects built with **n8n, Google Apps Script, Google Sheets, Gemini, Google Docs, Gmail, and GitHub Actions**.

> **Portfolio status:** Project documentation and folder structure are being prepared. Original workflow exports, screenshots, and the demo video must be added from the working projects before this portfolio is considered complete.

## Table of contents

1. [AI Class Feedback Analyzer](#1-ai-class-feedback-analyzer)
2. [AI Email Summarizer](#2-ai-email-summarizer)
3. [AI Resume Automation](#3-ai-resume-automation)
4. [CS Department FAQ AI Assistant](#4-cs-department-faq-ai-assistant)
5. [Automated Job Alert Monitor](#5-automated-job-alert-monitor)
6. [Two-minute demo video](#two-minute-demo-video)
7. [University project extension](#university-project-extension)
8. [Repository structure](#repository-structure)

## 1. AI Class Feedback Analyzer

**Folder:** [01-AI-Class-Feedback-Analyzer](./01-AI-Class-Feedback-Analyzer/)

Collects student feedback through a form, stores responses in Google Sheets, visualizes ratings, and generates an AI-written report with Gemini. The implementation keeps student names and timestamps out of the Gemini prompt.

**Technology:** Google Forms, Google Sheets, Google Apps Script, Gemini.

**Run it:** Make a copy of the feedback form and spreadsheet, configure the `GEMINI_API_KEY` script property, verify the response tab and question columns, then run `generateClassFeedbackAIReport`.

## 2. AI Email Summarizer

**Folder:** [02-AI-Email-Summarizer](./02-AI-Email-Summarizer/)

Reads the latest five Gmail messages when manually run and creates a concise summary, priority level (High/Medium/Low), and suggested action in a Google Sheet.

**Technology:** Google Apps Script, Gmail, Google Sheets, Gemini.

**Run it:** Configure the `GEMINI_API_KEY` script property, authorize Gmail and Sheets access, confirm the `Emails` sheet headers, and run the summarizer function. Review the generated summaries and suggested actions.

## 3. AI Resume Automation

**Folder:** [03-AI-Resume-Automation](./03-AI-Resume-Automation/)

Uses profile and job information from Google Sheets to prepare a tailored resume using a Google Docs template and save the output as a Google Doc/PDF.

**Technology:** Google Sheets, Google Docs, Google Drive, Apps Script, AI-assisted content generation.

**Run it:** Make copies of the Profile and Job sheets and the Docs template, update template/document IDs and permissions in the script, authorize Google services, then use the Resume Automation menu.

## 4. CS Department FAQ AI Assistant

**Folder:** [04-CS-Department-FAQ-Agent](./04-CS-Department-FAQ-Agent/)

An n8n FAQ assistant that answers common Computer Science department questions, such as office hours, using an AI model. An unanswered-query log can be added to help maintain the FAQ knowledge base.

**Technology:** n8n, webhook/chat input, Gemini (or another configured LLM), optional Google Sheets logging.

**Run it:** Import the exported n8n workflow, configure the required model credentials and trigger, activate or test the workflow, then send a sample question. Expected office-hours test: Monday–Friday, 9 AM–4 PM (replace with the department's verified hours before real use).

## 5. Automated Job Alert Monitor

**Folder:** [05-Automated-Job-Alert-Monitor](./05-Automated-Job-Alert-Monitor/)

Checks configured PPSC/job-page sources for relevant links, filters them using keywords, tracks previously seen results, and emails newly detected matches.

**Technology:** Python, requests, BeautifulSoup, GitHub Actions, email/SMTP.

**Run it:** Configure the source URL and keywords, add the required email credentials as repository secrets, review the workflow schedule, and run the GitHub Actions workflow. Never commit email passwords or other secrets.

## Two-minute demo video

**Status:** Not uploaded yet. Add a publicly viewable video URL here after recording a two-minute walkthrough of the five automations.

## University project extension

### Smart University AI Helpdesk System

Extend the CS Department FAQ Assistant into a university-wide helpdesk. Students could ask about admissions, registration, fee deadlines, department office hours, exam schedules, and campus services. The system would answer from an approved university knowledge base, log questions it cannot answer, and route unresolved requests to the relevant office. An admin dashboard could show common questions, unanswered queries, and response trends.

**Why this extends the portfolio:** It builds directly on the FAQ assistant while adding knowledge-base management, escalation, analytics, and multi-department support.

## Repository structure

```text
AI-Automation-Portfolio/
├── README.md
├── 01-AI-Class-Feedback-Analyzer/
├── 02-AI-Email-Summarizer/
├── 03-AI-Resume-Automation/
├── 04-CS-Department-FAQ-Agent/
├── 05-Automated-Job-Alert-Monitor/
└── university-project/
```

Each automation folder contains its own project guide and a screenshots directory. Add the original exported workflow file (for example, `workflow.json` for n8n exports or the relevant Apps Script source files) and genuine screenshots from the completed project. Do not include API keys, passwords, personal student data, or private email content.
