import streamlit as st
import pandas as pd
import requests

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
    ## Intelligent MMTS Transit Prediction System

    SmartTransit Hyderabad combines:
    - ML-powered delay prediction
    - GTFS timetable traversal
    - weather-aware operational intelligence
    - interactive station visualization
    - downstream ETA forecasting
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

    humidity = weather["main"]["humidity"]

    wind_speed = weather["wind"]["speed"]

    col1, col2, col3, col4 = st.columns(4)

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

    with col3:

        st.metric(
            "Humidity",
            f"{humidity}%"
        )

    with col4:

        st.metric(
            "Wind Speed",
            f"{wind_speed} m/s"
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
            "✅ Weather conditions are favorable."
        )

except:

    st.info(
        "Unable to fetch weather data."
    )

# =========================================================
# SIDEBAR INPUTS
# =========================================================

st.sidebar.header("🚉 Journey Input")

stations = get_all_stations()

selected_station = st.sidebar.selectbox(
    "Select Departure Station",
    stations
)

selected_time = st.sidebar.text_input(
    "Current Time (HH:MM:SS)",
    "16:00:00"
)

find_train = st.sidebar.button(
    "🚆 Find Next Train"
)

# =========================================================
# STATION MAP
# =========================================================

st.subheader("🗺 MMTS Station Network")

show_station_map()

# =========================================================
# MAIN APP LOGIC
# =========================================================

if find_train:

    with st.spinner("🚆 Finding next train..."):

        results = generate_eta_table(
            selected_station,
            selected_time
        )

    # -----------------------------------------------------
    # NO TRAIN FOUND
    # -----------------------------------------------------

    if results is None:

        st.error(
            "❌ No upcoming trains found for this station and time."
        )

        st.info(
            "Try selecting an earlier time or another station."
        )

    else:

        # -------------------------------------------------
        # TRAIN OVERVIEW
        # -------------------------------------------------

        st.subheader("🚆 Next Available Train")

        col1, col2, col3 = st.columns(3)

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

        with col3:

            punctuality = max(
                100 - results["predicted_delay"] * 5,
                50
            )

            st.metric(
                label="Punctuality Score",
                value=f"{punctuality:.0f}%"
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
                "⚠ Moderate delays expected."
            )

        else:

            st.success(
                "✅ Train expected to run near schedule."
            )

        # -------------------------------------------------
        # ETA TABLE
        # -------------------------------------------------

        st.subheader("📍 Predicted Arrival Timeline")

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
        # ROUTE SUMMARY
        # -------------------------------------------------

        st.subheader("🛤 Route Summary")

        final_stop = eta_table.iloc[-1]["stop_id"]

        final_arrival = eta_table.iloc[-1][
            "predicted_arrival"
        ]

        total_stops = len(eta_table)

        st.info(
            f"""
            🚉 Final Destination: {final_stop}

            ⏰ Estimated Final Arrival:
            {final_arrival}

            📍 Remaining Stops:
            {total_stops}
            """
        )

        # -------------------------------------------------
        # DOWNLOAD ETA FEATURE
        # -------------------------------------------------

        csv = eta_table.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇ Download ETA Predictions",
            data=csv,
            file_name="mmts_eta_predictions.csv",
            mime="text/csv"
        )

        # -------------------------------------------------
        # CROWD LEVEL ESTIMATION
        # -------------------------------------------------

        st.subheader("🚶 Estimated Crowd Density")

        if total_stops > 15:

            st.warning(
                "High passenger traffic expected."
            )

        elif total_stops > 8:

            st.info(
                "Moderate passenger traffic expected."
            )

        else:

            st.success(
                "Low passenger traffic expected."
            )

        # -------------------------------------------------
        # TRANSIT RELIABILITY INDEX
        # -------------------------------------------------

        st.subheader("📈 Transit Reliability Index")

        reliability_score = max(
            100
            - (
                results["predicted_delay"] * 4
                + total_stops * 1.2
            ),
            35
        )

        if reliability_score >= 85:

            reliability_status = "Excellent"

            st.success(
                f"Reliability Score: {reliability_score:.0f}/100 • {reliability_status}"
            )

        elif reliability_score >= 70:

            reliability_status = "Good"

            st.info(
                f"Reliability Score: {reliability_score:.0f}/100 • {reliability_status}"
            )

        elif reliability_score >= 50:

            reliability_status = "Moderate"

            st.warning(
                f"Reliability Score: {reliability_score:.0f}/100 • {reliability_status}"
            )

        else:

            reliability_status = "Poor"

            st.error(
                f"Reliability Score: {reliability_score:.0f}/100 • {reliability_status}"
            )

        # EXTRA INSIGHT

        if reliability_score < 60:

            st.info(
                "Consider planning buffer time due to operational uncertainty."
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
        4. View downstream ETA predictions

        ---

        ## Features

        - 🚆 Real-time train lookup
        - 🤖 ML-powered delay prediction
        - 🌤 Weather-aware alerts
        - 🗺 Interactive MMTS station map
        - 📊 ETA forecasting
        - 📥 Downloadable schedules
        - 🚶 Crowd density estimation
        - 📈 Transit reliability scoring

        ---

        Built using:
        - Streamlit
        - Pandas
        - GTFS transit data
        - Scikit-learn
        - Folium maps
        """
    )
