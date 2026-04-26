# AI Health Guardian  
### Emotion-Aware Smart Healthcare Assistant  

AI Health Guardian is an intelligent healthcare support system that combines **physical symptom analysis + emotional state detection + future risk prediction** to provide users with smart and actionable healthcare guidance.

Unlike traditional symptom checkers, this system does not stop at prediction — it helps users understand the severity of their condition and guides them with the next best action.

# Problem Statement

Most healthcare applications focus only on physical symptoms and ignore emotional and mental health signals like stress, anxiety, and fatigue.

This creates major problems:

- Mental health signals remain unnoticed
- Users cannot understand how serious their condition is
- No real-time guidance is provided
- Delayed decisions can lead to serious health risks

Our project solves this by combining symptom detection with emotion-aware AI to provide complete health insights.

# Proposed Solution

AI Health Guardian analyzes:

- User Symptoms  
- Emotional State  
- Risk Severity  
- Future Health Risk  
- Smart Next-Step Actions

The system predicts disease possibilities, detects stress levels, estimates health risk, and provides real-time action suggestions like:

- Home Care Tips  
- Doctor Consultation  
- Emergency Medical Help  
- Nearby Hospital Finder

This makes healthcare faster, smarter, and more accessible.

---

# Key Features

## Symptom-Based Disease Prediction
Detects possible diseases using user-entered symptoms like chest pain, fever, cough, headache, etc.

## Emotion Detection
Uses NLP to identify stress, anxiety, and emotional state using TextBlob sentiment analysis.

## AI Risk Level Prediction
Classifies user condition into:

- Low Risk
- Medium Risk
- High Risk

##  Future Risk Prediction (WOW Feature)
Shows how the condition may worsen if ignored using what-if simulation.

##  Confidence Score
Displays AI confidence level to improve trust and decision-making.

##  Personalized AI Insight
Provides user-specific intelligent health summaries.

## 🚨 Smart Action Suggestions
Suggests what to do next:

- Home Care
- Book Doctor Appointment
- Emergency Action

##  Nearby Hospital Finder
Direct integration with maps for immediate hospital access.

##  Voice-Based AI Response
System speaks medical advice using browser speech synthesis.

##  Modern Interactive UI
Glassmorphism-based responsive design for better user experience.

---

# 🛠 Technology Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- Flask

## AI / NLP
- TextBlob (Sentiment Analysis)

## Communication
- REST API
- Fetch API

## UI Design
- Glassmorphism
- Responsive Design

---

#  System Workflow

### Step 1 — User Input
User enters symptoms and feelings using the frontend interface.

### Step 2 — Data Transfer
Input is sent to the backend using REST API (Fetch API).

### Step 3 — Backend Processing
Flask receives the data and processes it.

### Step 4 — AI Analysis
System performs:

- Disease Prediction
- Emotion Detection
- Risk Classification
- Future Risk Simulation
- Confidence Score Generation

### Step 5 — Smart Response
System returns:

- Health Prediction
- Action Suggestions
- Hospital Finder
- Voice-Based Response

---

# 📁 Project Structure

```bash
Health_AI_Guardian/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
│
└── README.md
