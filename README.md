# AI Interview Assistant

## Overview

AI Interview Assistant is a multi-agent AI application built using FastAPI and Google Gemini AI to automate interview preparation, candidate evaluation, resume analysis, and hiring recommendations.

The system simulates an AI-powered technical interviewer by generating interview questions, evaluating candidate answers, analyzing resumes against job descriptions, generating interview scorecards, and providing hiring recommendations.

## Features

- AI Interview Question Generator
- Answer Evaluation Agent
- Resume Skill Gap Analyzer
- Interview Scorecard Generator
- Hiring Recommendation Agent
- PDF Interview Report Generator
- Dockerized Deployment
- Swagger API Documentation

### Interview Question Generator

* Generates technical interview questions based on technology and experience level.
* Supports multiple domains such as Python, DevOps, AWS, Kubernetes, and more.

### Interview Generator

* Creates complete interview sessions dynamically using Gemini AI.

### Answer Evaluation Agent

* Evaluates candidate responses.
* Provides scores, feedback, and improvement suggestions.

### Resume Analyzer Agent

* Compares resumes against job descriptions.
* Identifies matched skills and missing skills.
* Generates skill-gap analysis.

### Scorecard Generator Agent

* Generates interview scorecards based on:

  * Question
  * Candidate Answer
  * Feedback
* Produces:

  * Overall Score
  * Technical Knowledge Score
  * Communication Score
  * Problem Solving Score
  * Recommendation

### Hiring Recommendation Agent

* Uses resume analysis and interview scorecards.
* Produces:

  * Hiring Decision
  * Candidate Strengths
  * Areas of Concern
  * Final Recommendation

## Tech Stack

* Python
* FastAPI
* Google Gemini AI
* Pydantic
* Uvicorn
* REST APIs
* Docker

## API Endpoints

* POST /generate-questions
* POST /generate-interview
* POST /evaluate-answer
* POST /analyze-resume
* POST /generate-scorecard
* POST /generate-recommendation

## Screenshots

### Swagger UI
![Swagger Home](Screenshots/swagger-home.png)

### Question Generation
![Question Generation](Screenshots/generate-questions.png)

### Interview Generation
![Interview Generation](Screenshots/generate-interview.png)

### Answer Evaluation
![Answer Evaluation](Screenshots/evaluate-answer.png)

### Resume Analysis
![Resume Analysis](Screenshots/analyze-resume.png)

### Scorecard Generation
![Scorecard Generation](Screenshots/generate-scorecard.png)

### Hiring Recommendation
![Hiring Recommendation](Screenshots/generate-recommendation.png)

### PDF Report Generation API
![PDF Report Generation](Screenshots/generate-report.png)

### Generated PDF Report
![Generated PDF Report](Screenshots/pdf-report-output.png)

### User Registration
![User Registration](Screenshots/register-user.png)

### User Login (JWT Authentication)
![User Login](Screenshots/login-user.png)

### Protected Profile Endpoint
![Protected Profile](Screenshots/profile-auth-success.png)



## Docker Setup

Build Docker Image

```bash
docker build -t ai-interview-assistant .
```

Run Docker Container

```bash
docker run -p 8000:8000 --env-file .env ai-interview-assistant
```

Swagger Documentation

```text
http://localhost:8000/docs
```

## Future Enhancements

* Candidate Dashboard
* Interview History Tracking
* Cloud Deployment (AWS/GCP)


