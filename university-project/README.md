# Smart University AI Helpdesk System

## Project idea

Extend the CS Department FAQ AI Assistant into a university-wide helpdesk that answers student questions about admissions, registration, fee deadlines, department office hours, exam schedules, and campus services using an approved knowledge base.

## Proposed workflow

Student question → Intent detection → Search approved university knowledge base → AI-generated grounded answer → Response to student → Log question and outcome.

If the system cannot find a reliable answer, it should create an escalation ticket for the relevant university office rather than inventing information.

## Core features

- Multi-department FAQ knowledge base.
- Grounded answers with source references.
- Unanswered-query logging and human escalation.
- Admin interface to update FAQs.
- Analytics for common questions and response gaps.
- Privacy controls and role-based access.

## Suggested implementation

n8n for orchestration, a university-approved database or Google Sheets for a prototype knowledge base, Gemini for language understanding and answer drafting, and a simple web/chat interface.

## Evaluation

Measure answer accuracy against a reviewed test set, unanswered-query escalation rate, response time, and student satisfaction. Use synthetic or anonymized data during development.
