# 🚆 SmartTransit Hyderabad

## AI-Powered MMTS Train ETA Prediction System

SmartTransit Hyderabad is a civic-tech web application designed to improve the daily commuting experience for Hyderabad MMTS passengers.

The platform combines:

* GTFS timetable intelligence,
* route traversal logic,
* machine learning delay estimation,
* and predictive ETA generation

to provide commuters with smarter and more reliable train arrival information.

---

# 🌍 Problem Statement

MMTS commuters in Hyderabad often face uncertainty regarding:

* train arrival timings,
* operational delays,
* downstream ETAs,
* and route planning.

Public timetable information only provides scheduled timings and lacks predictive operational intelligence.

SmartTransit Hyderabad addresses this problem by building a lightweight predictive transit system capable of:

* identifying the next available train,
* estimating operational delays,
* and generating predicted ETAs for downstream stations.

---

# 💡 Solution Overview

The application uses:

1. Official GTFS timetable data for MMTS schedules and routes.
2. Historical railway delay patterns for operational delay modeling.
3. Machine Learning (Random Forest Regression) for delay estimation.
4. Dynamic ETA generation for downstream stations.

---

# 🧠 Core Features

## ✅ Next Train Detection

Users can:

* select a departure station,
* enter the current time,
* and instantly find the next available MMTS train.

---

## ✅ Predictive ETA Generation

The system predicts:

* adjusted arrival times,
* adjusted departure times,
* downstream ETAs,
* and expected operational delay.

---

## ✅ ML-Powered Delay Estimation

A Random Forest Regressor predicts likely delays using:

* historical punctuality patterns,
* route characteristics,
* peak-hour assumptions,
* station traffic density.

---

## ✅ Route Traversal Intelligence

The application dynamically:

* traverses train routes,
* identifies downstream stations,
* computes sequential ETAs.

---

# 🏗️ System Architecture

## 1. Timetable Engine (`timetable.py`)

Responsible for:

* train lookup,
* route traversal,
* schedule retrieval,
* station querying.

### Key Functions

* `get_next_train()`
* `get_remaining_stops()`
* `get_train_schedule()`
* `get_all_stations()`

---

## 2. Delay Prediction Engine (`delay_model.py`)

Responsible for:

* operational feature generation,
* ML inference,
* delay estimation.

### ML Model

* Random Forest Regressor

### Inputs

* peak-hour conditions,
* station load,
* route speed,
* route complexity.

### Output

* predicted delay in minutes.

---

## 3. ETA Engine (`eta.py`)

Responsible for:

* combining timetable data with ML predictions,
* generating commuter-facing ETAs.

### Output

| Station | Scheduled Arrival | Predicted Arrival |
| ------- | ----------------- | ----------------- |

---

## 4. Streamlit UI (`app.py`)

Responsible for:

* user interaction,
* displaying ETAs,
* rendering train information.

---

# 📊 Datasets Used

## MMTS GTFS Dataset

Contains:

* train schedules,
* stop sequences,
* station information,
* route metadata.

### Files

* `stop_times.txt`
* `trips.txt`

---

## Railway Delay Dataset

Scraped railway operational dataset containing:

* historical delay patterns,
* punctuality percentages,
* cancellation rates.

### Features Used

* `pct_right_time`
* `pct_slight_delay`
* `pct_significant_delay`
* `pct_cancelled_unknown`

---

# 🤖 Machine Learning

## Model

Random Forest Regressor

## Target Variable

`average_delay_minutes`

## Why Random Forest?

* robust on tabular data,
* handles nonlinearity,
* interpretable,
* effective on small datasets,
* suitable for hackathon-scale deployment.

---

# 📂 Project Structure

```plaintext
MMTSWebApp/
│
├── app.py
│
├── data/
│   ├── stop_times.txt
│   ├── trips.txt
│   └── etrain_delays.csv
│
├── models/
│   └── delay_predictor.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── utils/
│   ├── timetable.py
│   ├── delay_model.py
│   └── eta.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1. Clone Repository

```bash
git clone <repo-url>
cd MMTSWebApp
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Application

```bash
streamlit run app.py
```

---

# 🧪 User Manual

# Home Screen

Users are presented with:

* station selector,
* current time input,
* train prediction button.

---

# Step 1 — Select Departure Station

Choose any MMTS station from the dropdown menu.

Example:

```text
BMT (Begumpet)
```

---

# Step 2 — Enter Current Time

Enter the current time in:

```text
HH:MM:SS
```

Example:

```text
18:10:00
```

---

# Step 3 — Find Next Train

Click:

```text
Find Next Train
```

The application will:

1. identify the next scheduled train,
2. estimate operational delay,
3. generate predicted ETAs.

---

# Step 4 — View Results

The application displays:

* Train ID
* Predicted Delay
* Scheduled Arrival Times
* Predicted Arrival Times

Example:

| Station | Scheduled | Predicted |
| ------- | --------- | --------- |
| BMT     | 18:23     | 18:28     |
| HTCY    | 18:34     | 18:40     |
| LPI     | 18:49     | 18:56     |

---

# 🛠️ Future Improvements

## Potential Extensions

* live GPS integration,
* real-time railway APIs,
* crowding estimation,
* route optimization,
* interactive maps,
* multilingual support,
* commuter notifications.

---

# ⚠️ Limitations

* Current ETA predictions are based on historical operational patterns and simulated conditions.
* No live MMTS telemetry is currently available.
* Predictions are intended for research and prototype demonstration purposes.

---

# 🎯 Civic-Tech Impact

SmartTransit Hyderabad demonstrates how:

* open transit datasets,
* machine learning,
* and lightweight web systems

can improve public transportation accessibility and commuter experience in Indian cities.

---

# 👥 Team

Hackathon Project — Civic Tech Theme

Built using:

* Python
* Pandas
* Scikit-learn
* Streamlit
* GTFS Transit Data
