# StudyPulse-Smart-Study-Time-Predictor

## 🚀 Overview

StudyPulse is an AI-powered adaptive study planner that helps students optimize learning using behavioral data such as sleep, focus, stress, and study patterns. Unlike static schedules, it analyzes these factors to understand performance under different conditions.

The core of StudyPulse is a hybrid intelligence model that combines machine learning with rule-based logic. The machine learning component predicts the most effective study time (morning, afternoon, or night), while the rule-based system refines these predictions by handling real-world conditions such as low sleep, high stress, or approaching exams. This ensures that the recommendations are both accurate and practical.

The system combines **machine learning predictions with rule-based behavioral logic** to generate personalized study schedules, including structured sessions, break strategies, and actionable insights, helping students improve efficiency and prevent burnout.

---

## 🎯 Problem Statement

Many students follow random or inconsistent study patterns without understanding:

* When they are most productive
* How long they should study
* When to take breaks
* How stress and sleep affect performance

This leads to inefficient learning, burnout, and poor performance.

---

## 💡 Solution

StudyPulse solves this by providing:

* Personalized study time prediction
* Adaptive daily schedule
* Burnout detection
* Data-driven insights
* Actionable improvement suggestions

---

## 🧠 Key Features

### 🔹 1. Hybrid Intelligence System

A combination of:

* Machine Learning model (predicts best study time)
* Rule-based logic (handles edge cases like stress and sleep)

This ensures both **accuracy and reliability**.

---

### 🔹 2. Personalized Study Time Prediction

Predicts whether the user performs best in:

* Morning
* Afternoon
* Night

Based on behavioral inputs.

---

### 🔹 3. Dynamic Study Schedule

Generates a structured schedule including:

* Study sessions
* Break intervals
* Activity types (revision, practice, deep learning)

Adapts based on:

* Focus level
* Exam proximity
* Subject difficulty

---

### 🔹 4. Health & Cognitive Analysis

Analyzes:

* Sleep quality
* Focus levels

Provides insights on how they impact:

* Memory
* Learning speed
* Productivity

---

### 🔹 5. Burnout Detection

Identifies high-risk scenarios using:

* Stress levels
* Sleep deprivation

Provides alerts to prevent burnout.

---

### 🔹 6. Productivity Score

Calculates a score (0–100) based on:

* Focus
* Sleep
* Study hours
* Stress

Represents overall study readiness.

---

### 🔹 7. Data Visualization

Displays focus trends using graphs to help users understand performance patterns.

---

### 🔹 8. Personalized Improvement Suggestions

Generates dynamic recommendations based on:

* Combined factors (sleep + stress)
* Focus vs study imbalance
* Exam urgency

---

## 🏗️ System Architecture

### Input Layer

User inputs:

* Study hours
* Sleep hours
* Focus level
* Stress level
* Subject
* Exam days

---

### Processing Layer

* Feature transformation
* ML prediction (best study time)
* Rule-based refinement

---

### Output Layer

* Study schedule
* Insights
* Recommendations
* Visualizations

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Machine Learning:** Scikit-learn
* **Data Handling:** Pandas
* **Visualization:** Matplotlib
* **Model Storage:** Joblib

---

## 📂 Project Structure

```
StudyPulse/
│
├── Home.py              # Main Streamlit app
├── dashboard.py         # Dashboard logic
├── model/
│   └── model.pkl        # Trained ML model
├── data/
│   └── data.csv         # Training dataset
├── assets/
│   └── bg.png           # Background UI
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Key Highlights

* Behavior-driven analysis instead of static planning
* Combines ML + rule-based intelligence
* Real-time adaptive recommendations
* User-centric design with interactive UI

---

## 🔮 Future Improvements

* User history tracking
* More advanced ML models
* Mobile app version
* Real-time performance tracking

---

## 📎 Note

A pre-trained model (`model.pkl`) is included for demonstration purposes.

---

## 🧑‍💻 Author

Developed as part of an online hackathon project.
