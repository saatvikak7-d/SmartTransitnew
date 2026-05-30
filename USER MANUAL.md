# USER MANUAL

# 🚆 SmartTransit Hyderabad User Manual

Welcome to SmartTransit Hyderabad — an AI-powered MMTS train ETA prediction system.

This application helps commuters:

* find the next available MMTS train,
* estimate operational delays,
* and view predicted arrival times for downstream stations.

---

# 🖥️ Launching the Application

Run the application locally using:

```bash
streamlit run app.py
```

The app will open in your browser automatically.

---

# 📍 Using the Application

## Step 1 — Select Departure Station

Use the dropdown menu to choose your current MMTS station.

Example:

```text
BMT (Begumpet)
```

---

## Step 2 — Enter Current Time

Enter the current time in:

```text
HH:MM:SS
```

Example:

```text
18:10:00
```

---

## Step 3 — Find Next Train

Click:

```text
Find Next Train
```

The application will:

1. identify the next available train,
2. predict operational delay,
3. generate ETA estimates for downstream stations.

---

# 📊 Understanding the Output

The application displays:

## 🚆 Train Information

* Train ID
* Predicted operational delay

---

## 📍 ETA Table

| Column              | Meaning               |
| ------------------- | --------------------- |
| stop_id             | MMTS station code     |
| arrival_time        | scheduled arrival     |
| predicted_arrival   | ML-adjusted ETA       |
| departure_time      | scheduled departure   |
| predicted_departure | ML-adjusted departure |

---

# ⚠️ Delay Predictions

Delay predictions are generated using:

* timetable information,
* historical railway operational patterns,
* and machine learning estimation.

Predictions are probabilistic and intended for demonstration purposes.

---

# 🛠️ Troubleshooting

## No trains found

* ensure the time format is correct,
* try another station/time.

---

## App does not launch

Ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

---

# 📌 Notes

* This application currently uses static GTFS schedule data.
* Live MMTS telemetry is not currently integrated.
* ETA predictions are generated using historical railway delay behavior.
