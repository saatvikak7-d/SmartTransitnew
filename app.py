import streamlit as st
import pandas as pd
import requests

st.write("APP RUNNING")
from utils.timetable import (
    get_all_stations
)

from utils.map_view import (
    show_station_map
)

from utils.eta import (
    generate_eta_table
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SmartTransit Hyderabad",
    page_icon="🚆",
    layout="wide"
)

# =========================================================
# WEATHER FUNCTION
# =========================================================

def get_weather():

    API_KEY = st.secrets["WEATHER_API_KEY"]

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q=Hyderabad"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    return response.json()

# =========================================================
# TITLE
# =========================================================

st.title("🚆 SmartTransit Hyderabad")

st.markdown(
    """
    Intelligent MMTS Transit Prediction System

    Features:
    - ML-powered delay prediction
    - timetable traversal
    - live station visualization
    - weather-aware operational alerts
    """
)

# =========================================================
# WEATHER ALERTS
# =========================================================

st.subheader("🌤 Current Weather Conditions")

try:

    weather = get_weather()

    weather_main = weather["weather"][0]["main"]

    temperature = weather["main"]["temp"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Weather",
            weather_main
        )

    with col2:

        st.metric(
            "Temperature",
            f"{temperature} °C"
        )

    # WEATHER ALERTS

    if weather_main in ["Rain", "Thunderstorm"]:

        st.warning(
            "⚠ Rain detected. MMTS delays may increase."
        )

    elif weather_main in ["Mist", "Fog"]:

        st.warning(
            "⚠ Low visibility conditions detected."
        )

    else:

        st.success(
            "Weather conditions are favorable."
        )

except:

    st.info(
        "Unable to fetch weather data."
    )

# =========================================================
# SIDEBAR INPUTS
# =========================================================

st.sidebar.header("Journey Input")

stations = get_all_stations()

selected_station = st.sidebar.selectbox(
    "Select Departure Station",
    stations
)

selected_time = st.sidebar.text_input(
    "Current Time (HH:MM:SS)",
    "18:10:00"
)

find_train = st.sidebar.button(
    "Find Next Train"
)

# =========================================================
# STATION MAP
# =========================================================

st.subheader("🗺 MMTS Station Network")

show_station_map()

# =========================================================
# MAIN APP LOGIC
# =========================================================

# =========================================================
# MAIN APP LOGIC
# =========================================================

if find_train:

    st.write("BUTTON CLICKED")

    with st.spinner("Finding next train..."):

        st.write("CALLING ETA")

        results = generate_eta_table(
            selected_station,
            selected_time
        )

        st.write("ETA COMPLETE")

        st.write(results)

    # -----------------------------------------------------
    # NO TRAIN FOUND
    # -----------------------------------------------------

    if results is None:

        st.error(
            "No upcoming trains found."
        )

    else:

        st.subheader("🚆 Next Available Train")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                label="Train ID",
                value=results["train_id"]
            )

        with col2:

            st.metric(
                label="Predicted Delay",
                value=f'{results["predicted_delay"]:.2f} min'
            )

        st.subheader("📍 Predicted Arrival Times")

        eta_table = results["eta_table"].copy()

        eta_table["arrival_time"] = (
            eta_table["arrival_time"]
            .dt.strftime("%H:%M:%S")
        )

        eta_table["departure_time"] = (
            eta_table["departure_time"]
            .dt.strftime("%H:%M:%S")
        )

        eta_table["predicted_arrival"] = (
            eta_table["predicted_arrival"]
            .dt.strftime("%H:%M:%S")
        )

        eta_table["predicted_departure"] = (
            eta_table["predicted_departure"]
            .dt.strftime("%H:%M:%S")
        )

        st.dataframe(
            eta_table,
            use_container_width=True
        )

    # -----------------------------------------------------
    # NO TRAIN FOUND
    # -----------------------------------------------------

    if results is None:

        st.error(
            "No upcoming trains found."
        )

    else:

        # -------------------------------------------------
        # TRAIN INFO
        # -------------------------------------------------

        st.subheader("🚆 Next Available Train")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                label="Train ID",
                value=results["train_id"]
            )

        with col2:

            st.metric(
                label="Predicted Delay",
                value=f'{results["predicted_delay"]:.2f} min'
            )

        # -------------------------------------------------
        # ETA TABLE
        # -------------------------------------------------

        st.subheader("📍 Predicted Arrival Times")

        eta_table = results["eta_table"].copy()

        eta_table["arrival_time"] = (
            eta_table["arrival_time"]
            .dt.strftime("%H:%M:%S")
        )

        eta_table["departure_time"] = (
            eta_table["departure_time"]
            .dt.strftime("%H:%M:%S")
        )

        eta_table["predicted_arrival"] = (
            eta_table["predicted_arrival"]
            .dt.strftime("%H:%M:%S")
        )

        eta_table["predicted_departure"] = (
            eta_table["predicted_departure"]
            .dt.strftime("%H:%M:%S")
        )

        st.dataframe(
            eta_table,
            use_container_width=True
        )

        # -------------------------------------------------
        # DELAY INSIGHT
        # -------------------------------------------------

        if results["predicted_delay"] > 10:

            st.error(
                "⚠ High operational delay expected."
            )

        elif results["predicted_delay"] > 5:

            st.warning(
                "Moderate delays expected."
            )

        else:

            st.success(
                "Train expected to run near schedule."
            )

# =========================================================
# DEFAULT LANDING PAGE
# =========================================================

else:

    st.markdown(
        """
        ## How To Use

        1. Select your departure station  
        2. Enter the current time  
        3. Click **Find Next Train**  
        4. View predicted ETAs for downstream stations

        ---

        ### Technology Stack

        - GTFS timetable data
        - ML-based delay prediction
        - route traversal engine
        - live weather monitoring
        - interactive MMTS network visualization
        """
    )
