# ⚽ World Cup 2026 Goal Prediction Challenge

> **Zindi Competition** · $1,000 USD Prize Pool  
> Predict goals scored & tournament stage for 48 nations at FIFA World Cup 2026

---

## 🏆 Live Dashboard

👉 **[View Predictions Dashboard](https://share.streamlit.io)** *(https://worldcup2026-prediction.streamlit.app/)*

---

## 📌 Project Overview

This project builds machine learning models to predict:
1. **Total goals** each team will score at FIFA World Cup 2026
2. **Tournament stage** each team will reach (Group → Champion)

**Final Model:** Random Forest  
**Evaluation:** `0.60 × RMSE(Goals) + 0.40 × F1(Stage)`

---

## 📊 Results

| Model | RMSE (Goals ↓) | F1 Score (Stage ↑) |
|-------|---------------|---------------------|
| **Random Forest** ✅ | **3.9516** | **0.4107** |
| XGBoost | 4.2134 | 0.3717 |
| LightGBM | 4.3412 | 0.3602 |

---

## 🔮 Top Predictions

| # | Country | Predicted Goals | Stage |
|---|---------|----------------|-------|
| 1 | 🇫🇷 France | 11.82 | 🏆 Champion |
| 2 | 🇦🇷 Argentina | 10.26 | 🥈 Runner-up |
| 3 | 🇳🇱 Netherlands | 9.90 | 🔵 Semi-final |
| 4 | 🇧🇷 Brazil | 9.27 | 🔵 Semi-final |
| 5 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England | 8.96 | 🟣 Quarter-final |

---

## 📁 Project Structure

```
worldcup2026/
│
├── 📓 notebooks/
│   ├── 01_EDA.ipynb                # Exploratory Data Analysis
│   ├── 02_Feature_Engineering.ipynb # Feature Engineering
│   └── 03_Modeling.ipynb           # Model Training & Evaluation
│
├── 📊 data/
│   ├── Train.csv                   # Historical World Cup data
│   ├── Test.csv                    # 48 teams to predict
│   ├── train_processed_v2.csv      # Engineered features
│   └── submission_final.csv        # Final predictions
│
├── 🖥️ app.py                       # Streamlit Dashboard
├── requirements.txt                # Python dependencies
└── README.md
```

---

## ⚙️ Features Used (17 Features)

| Feature | Description |
|---------|-------------|
| `conf_strength_vs_era` | Team strength relative to their era (🥇 most important) |
| `hist_consistency` | Consistency across tournaments |
| `hist_total_goals` | Total historical goals scored |
| `hist_goals_per_match` | Average goals per match |
| `hist_last3_avg_goals` | Average goals in last 3 tournaments |
| `hist_momentum` | Recent performance trend |
| `is_host` | Whether the team is the host nation |
| `year` | Tournament year |
| + 9 more... | Country encoding, confederation stats, etc. |

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/Mustafa-elsherif/worldcup2026-prediction.git
cd worldcup2026-prediction

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-red)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-ff4b4b?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75?logo=plotly)

---

## 📋 Competition Rules Compliance

- ✅ Only used the provided Fjelstul World Cup Database
- ✅ No external data, betting odds, or 2026 match results
- ✅ Open-source tools only (sklearn, XGBoost, LightGBM)
- ✅ No AutoML
- ✅ `random_state=42` set everywhere (reproducible results)

---

## 👤 Author

**Mustafa El-Sherif**  
Data Science & AI Student  
[GitHub](https://github.com/Mustafa-elsherif) · [LinkedIn](https://www.linkedin.com/in/mustafa-elsherif-77b74729a)

---

*Built for the [Zindi World Cup 2026 Goal Prediction Challenge](https://zindi.africa/competitions/world-cup-2026-goal-prediction-challenge)*
