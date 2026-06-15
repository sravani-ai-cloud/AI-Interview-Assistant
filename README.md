# AI Interview Assistant

## Overview

AI Interview Assistant is a multi-agent AI application built using FastAPI and Google Gemini AI to automate interview preparation, candidate evaluation, resume analysis, and hiring recommendations.

The system simulates an AI-powered technical interviewer by generating interview questions, evaluating candidate answers, analyzing resumes against job descriptions, generating interview scorecards, and providing hiring recommendations.

## Features

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

### Swagger Home
![Swagger Home](Screenshots/swagger-home.png)

### Generate Questions
![Generate Questions](Screenshots/generate-questions.png)

### Evaluate Answer
![Evaluate Answer](Screenshots/evaluate-answer.png)

### Analyze Resume
![Analyze Resume](Screenshots/analyze-resume.png)

### Generate Scorecard
![Generate Scorecard](Screenshots/generate-scorecard.png)

### Generate Interview
![Generate Interview](Screenshots/generate-interview.png)

### Generate Recommendation
![Generate Recommendation](Screenshots/generate-recommendation.png)

## Future Enhancements

* JWT Authentication
* Candidate Dashboard
* PDF Report Generation
* Interview History Tracking
* Docker Deployment
* Cloud Deployment (AWS/GCP)


