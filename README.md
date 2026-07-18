# 🛡️ Fraud Detection System

A Rule-Based Banking Transaction Analysis System that identifies suspicious transactions, generates statistical insights, visualizes fraud patterns, and produces AI-powered investigation reports using Google Gemini.

---

## 📌 Project Overview

Financial institutions process thousands of transactions every day, making manual fraud detection difficult and time-consuming.

This project assists banking fraud analysts by:

- Detecting suspicious transactions using a configurable rule-based fraud engine.
- Calculating Risk Scores and Fraud Probability.
- Providing explainable reasons behind each flagged transaction.
- Generating statistical analytics and visualizations.
- Producing AI-powered fraud investigation reports using Google Gemini.

---

## ✨ Features

- 🔐 Login Interface
- 📂 CSV-based Transaction Upload
- ⚙️ Rule-Based Fraud Detection Engine
- 📊 Risk Score & Fraud Probability Calculation
- 📈 Statistical Analytics using NumPy
- 📉 Interactive Visualizations using Matplotlib
- 🤖 AI Fraud Investigation Report using Google Gemini
- 📋 Detailed Transaction Table with Explainable Reasons
- 🎨 Responsive Dashboard

---

## 🏗️ System Architecture

```
User Login
      │
      ▼
Dashboard
      │
      ▼
Upload CSV Dataset
      │
      ▼
Flask Backend
      │
      ▼
Pandas Data Processing
      │
      ▼
Rule-Based Fraud Engine
      │
      ├────────► Risk Score
      ├────────► Fraud Probability
      ├────────► Status
      └────────► Reasons
                │
                ▼
     NumPy Statistical Analytics
                │
                ▼
   Matplotlib Visualizations
                │
                ▼
 Google Gemini AI Report
                │
                ▼
     Dashboard Output
```

---

## 🛠️ Technology Stack

### Backend
- Flask

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib

### AI Integration
- Google Gemini API
- Google GenAI SDK

### Frontend
- HTML5
- CSS3
- Jinja2

### Environment Management
- python-dotenv

### Version Control
- Git & GitHub

---

## 📊 Visual Analytics

The system generates four visualizations:

- Fraud Distribution (Pie Chart)
- Risk Score Distribution (Bar Chart)
- Fraud Indicator Frequency (Horizontal Bar Chart)
- Login Attempts vs Risk Score (Scatter Plot)

---

## 🤖 AI Integration

Google Gemini is integrated to generate a professional fraud investigation report based on the analyzed transactions.

The generated report includes:

- Executive Summary
- Dataset Statistics
- Risk Assessment
- Common Fraud Indicators
- Investigation Recommendations
- Fraud Prevention Suggestions
- Final Conclusion

---

## 📁 Project Structure

```
Fraud_Detection_System/
│
├── app.py
├── fraud_engine.py
├── visualization.py
├── ai_report.py
├── pdf_generator.py
├── requirements.txt
├── .env.example
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   ├── charts/
│   ├── style.css
│   └── style_.css
│
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Fraud_Detection_System.git
```

Navigate to the project directory:

```bash
cd Fraud_Detection_System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🔮 Future Scope

- Machine Learning-based Fraud Detection
- Database Integration
- Real-time Transaction Monitoring
- Cloud Deployment
- Email/SMS Alert System
- Enhanced User Authentication
- Advanced Fraud Analytics

---

---

## 📬 Connect

### **[Naman Sethi](https://github.com/naman-sethii)**

If you found this project useful, feel free to ⭐ the repository.

---

## 📜 License

This project was developed for academic purposes as part of a college software development project.
