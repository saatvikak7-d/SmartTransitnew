# AGENTS.md

# SmartTransit Hyderabad — Agent Overview

This document describes the major software agents/modules used in SmartTransit Hyderabad.

---

# 🚆 Timetable Agent (`timetable.py`)

## Purpose

Responsible for:

* MMTS schedule retrieval,
* route traversal,
* train lookup,
* downstream station discovery.

## Responsibilities

* identify next train,
* retrieve station schedules,
* provide route information.

## Core Functions

* `get_next_train()`
* `get_remaining_stops()`
* `get_train_schedule()`
* `get_all_stations()`

---

# 🤖 Delay Prediction Agent (`delay_model.py`)

## Purpose

Responsible for:

* operational delay estimation,
* ML inference,
* railway behavior simulation.

## ML Model

Random Forest Regressor

## Inputs

* hour of day,
* station load,
* route complexity,
* operational assumptions.

## Outputs

* predicted delay in minutes.

## Core Functions

* `generate_delay_features()`
* `predict_delay()`

---

# ⏱️ ETA Generation Agent (`eta.py`)

## Purpose

Responsible for:

* combining timetable information with delay predictions,
* generating commuter-facing ETAs.

## Responsibilities

* apply delay adjustments,
* generate predicted arrival/departure times,
* create final ETA tables.

## Core Functions

* `adjust_arrival_times()`
* `generate_eta_table()`

---

# 🖥️ UI Agent (`app.py`)

## Purpose

Responsible for:

* user interaction,
* Streamlit interface rendering,
* displaying ETA results.

## Responsibilities

* collect user input,
* trigger backend pipelines,
* render ETA tables and train information.

---

# 📊 Data Sources

## GTFS MMTS Dataset

Used for:

* train schedules,
* routes,
* station sequences.

## Railway Delay Dataset

Used for:

* historical operational delay behavior,
* ML model training.

---

# 🔄 Agent Workflow

```text
User Input
    ↓
Timetable Agent
    ↓
Delay Prediction Agent
    ↓
ETA Generation Agent
    ↓
UI Agent
```

---

# 🎯 System Goal

Provide Hyderabad MMTS commuters with:

* smarter ETA estimation,
* operational delay awareness,
* and improved public transit accessibility.
