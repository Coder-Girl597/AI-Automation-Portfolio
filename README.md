# AI Automation Portfolio

A collection of five practical AI and workflow-automation projects built with **n8n, Google Apps Script, Google Sheets, Gemini, Google Docs, Gmail, Python, and GitHub Actions**.

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

Collects student feedback through a form, stores responses in Google Sheets, visualizes ratings, and generates an AI-written report with Gemini. Student names and timestamps are excluded from the Gemini prompt.

**Technology:** Google Forms, Google Sheets, Google Apps Script, Gemini.

**How to run:** Make a copy of the form and spreadsheet, configure the `GEMINI_API_KEY` script property, verify the response tab and question columns, then run `generateClassFeedbackAIReport`.

## 2. AI Email Summarizer

**Folder:** [02-AI-Email-Summarizer](./02-AI-Email-Summarizer/)

Reads the latest five Gmail messages when manually run and creates a concise summary, priority level (High/Medium/Low), and suggested action in a Google Sheet.

**Technology:** Google Apps Script, Gmail, Google Sheets, Gemini.

**How to run:** Configure `GEMINI_API_KEY`, authorize Gmail and Sheets access, confirm the `Emails` sheet headers, and run the summarizer function. Review the generated summaries and suggested actions.

## 3. AI Resume Automation

**Folder:** [03-AI-Resume-Automation](./03-AI-Resume-Automation/)

Uses profile and job information from Google Sheets to prepare a tailored resume using a Google Docs template and save the output as a Google Doc/PDF.

**Technology:** Google Sheets, Google Docs, Google Drive, Apps Script, AI-assisted content generation.

**How to run:** Make copies of the Profile and Job sheets and the Docs template, update template/document IDs and permissions in the script, authorize Google services, then use the Resume Automation menu.

## 4. CS Department FAQ AI Assistant

**Folder:** [04-CS-Department-FAQ-Agent](./04-CS-Department-FAQ-Agent/)

An n8n FAQ assistant designed to answer common Computer Science department questions, such as office hours, using a configured AI model.

**Technology:** n8n, chat/webhook trigger, Gemini (or another configured LLM), optional Google Sheets logging.

**How to run:** Import the exported n8n workflow, configure model credentials and the trigger, then test with a sample question. Verify department information (including office hours) before real-world use.

## 5. Automated Job Alert Monitor

**Folder:** [05-Automated-Job-Alert-Monitor](./05-Automated-Job-Alert-Monitor/)

Checks a configured PPSC/job page for relevant links, filters them using keywords, tracks previously seen results, and emails newly detected matches.

**Technology:** Python, requests, BeautifulSoup, GitHub Actions, email/SMTP.

**How to run:** Configure the source URL and keywords, add email credentials as repository secrets, verify the GitHub Actions workflow location and schedule, then run the workflow. Never commit email passwords or other secrets.

## Two-minute demo video

## 🎥 2-Minute Demo Video

[Watch My Portfolio Demo]([PASTE_YOUR_YOUTUBE_LINK_HERE](https://youtu.be/c9i-JJNnvis))

## University project extension

### Smart University AI Helpdesk System

Extend the CS Department FAQ Assistant into a university-wide helpdesk. Students could ask about admissions, registration, fee deadlines, department office hours, exam schedules, and campus services. The system would answer from an approved university knowledge base, log questions it cannot answer, and route unresolved requests to the relevant office. An admin dashboard could show common questions, unanswered queries, and response trends.

**Extension value:** This builds on the FAQ assistant while adding knowledge-base management, escalation, analytics, and multi-department support.

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

Each project folder contains a project guide and a screenshots directory. Keep credentials, API keys, passwords, tokens, private email content, and identifiable student data out of this repository.
