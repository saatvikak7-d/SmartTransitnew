# 🚆 SmartTransit Hyderabad
/*a*/

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

Daily MMTS commuters in Hyderabad face persistent unpredictability regarding real-time train arrivals, cascading operational delays, and downstream ETAs. This information gap disrupts travel planning and causes unnecessary station crowding.

Because official transit channels rely strictly on static, ideal-world timetables, they lack the predictive operational intelligence required to account for live railway dynamics. **SmartTransit Hyderabad** directly addresses this problem by introducing a lightweight, data-driven engine designed to:
* **Instantly isolate** the next optimal chronological train departure based on commuter timelines.
* **Quantify and forecast** expected operational delays using historical network constraints.
* **Project adaptive ETAs** across all downstream stations to restore commuter certainty.

---

# 💡 Solution Overview

SmartTransit Hyderabad bridges the gap between theoretical timetables and real-world execution by introducing an integrated, multi-tiered data processing pipeline:

1. **Static Baseline Ingestion:** Leverages official GTFS (General Transit Feed Specification) data streams to map precise MMTS station geometries, stop sequences, and scheduled timetables.
2. **Operational Delay Modeling:** Analyzes historical railway punctuality trends, cancellation metrics, and performance patterns to establish localized bottleneck baselines.
3. **Machine Learning Inference:** Deploys a trained Random Forest Regression model to dynamically calculate precise, context-aware delay parameters.
4. **Dynamic ETA Propagation:** Employs an algorithmic route-traversal engine to superimpose ML-generated delays onto structural schedules, projecting real-time sequential arrival estimates for all downstream waypoints.

---

# 🧠 Core Features

### ✅ Next Train Discovery
Provides an intuitive interface for commuters to input an origin station and timestamp to immediately identify the nearest upcoming valid transit connection.

### ✅ Predictive ETA Generation
Computes real-time timeline metrics that account for ongoing operational variations, generating accurate estimations for adjusted arrival times, adjusted departure times, and downstream arrival windows.

### ✅ ML-Powered Delay Estimation
Utilizes an optimized Random Forest Regressor that evaluates complex, multi-dimensional inputs—such as peak-hour traffic conditions, historical line punctuality, specific route characteristics, and station density—to output granular delay forecasts.

### ✅ Route Traversal Intelligence
Features a robust pathing algorithm that automatically traces a train's forward route matrix, indexing downstream sequences to cascade runtime modifications sequentially across every remaining stop.


---

# 🏗️ System Architecture

### 1. Timetable Engine (`timetable.py`)
The foundational data parsing layer of the application, responsible for structural network navigation, schedule retrieval, and geometric route mapping.

* **Core Responsibilities:**
  * Executing deterministic database lookups for upcoming rail assets.
  * Dynamically processing spatial route trajectories and sequential station arrays.
  * Interrogating static GTFS parameters to build reliable timetable matrices.

* **Key API Functions:**
  * `get_next_train()` – Filters and extracts the immediate chronological service relative to user timestamps.
  * `get_remaining_stops()` – Maps downstream tracking configurations by indexing the remaining station sequence.
  * `get_train_schedule()` – Populates comprehensive baseline timing arrays for a specific train identifier.
  * `get_all_stations()` – Resolves and sorts unique station identifiers to populate interface filter inputs dynamically.

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
  # /
  ///aaa


THIS IS THE WEBSITE LINK: https://smarttransithyderabad-mxfbhc8r4axxe4qsaryalj.streamlit.app/
