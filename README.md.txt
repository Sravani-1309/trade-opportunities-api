# Trade Opportunities API

## 📌 Overview

This project is a FastAPI-based backend service that analyzes market data and provides trade opportunity insights for different sectors in India.

The API collects market information, uses AI (Google Gemini) for analysis, and returns a structured markdown report.

---

## 🚀 Features

* FastAPI-based REST API
* Sector-wise market analysis
* Google Gemini AI integration
* Web data collection (DuckDuckGo)
* Rate limiting (SlowAPI)
* API key authentication
* Input validation
* Markdown report generation
* In-memory session tracking

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Google Gemini (google-genai)
* Requests
* SlowAPI
* Python-dotenv

---

## 📡 API Endpoint

### GET /analyze/{sector}

Analyze a specific sector and get trade insights.

### Example:

GET /analyze/technology

### Headers:

x-api-key: mysecretkey

---

## 📄 Sample Response

```
# Market Analysis Report: Technology (India)

## Overview
This report analyzes the technology sector using recent market data and AI insights.

## AI Analysis
- Growth in AI and digital services
- Increasing investment opportunities
- Risks include competition and regulations

## Conclusion
The technology sector presents strong trade opportunities with moderate risks.
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/trade-opportunities-api.git

### 2. Navigate to project

cd trade-opportunities-api

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add environment variables

Create a `.env` file and add:
GEMINI_API_KEY=your_api_key_here

### 5. Run the application

uvicorn app.main:app --reload

---

## 🧪 Testing the API

Use Postman or browser:

URL:
http://127.0.0.1:8000/analyze/technology

Header:
x-api-key: mysecretkey

---

## 🔐 Security Features

* API key authentication
* Rate limiting (5 requests/minute)
* Input validation
* Environment-based secret management

---

## 📂 Project Structure

app/
├── main.py
├── routes.py
├── services/
│   ├── data_service.py
│   ├── ai_service.py
│   └── report_service.py
├── utils/
│   ├── auth.py
│   ├── rate_limiter.py
│   ├── validator.py
│   └── session.py

---

