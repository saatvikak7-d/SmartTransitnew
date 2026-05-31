import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium


def show_station_map():

    # LOAD STATIONS
    stops = pd.read_csv("data/stops.txt")

    # CENTER MAP ON HYDERABAD
    m = folium.Map(
        location=[17.3850, 78.4867],
        zoom_start=11
    )

    # ADD STATION MARKERS
    for _, row in stops.iterrows():

        folium.Marker(
            location=[
                row["stop_lat"],
                row["stop_lon"]
            ],

            popup=f"""
            <b>{row['stop_name']}</b><br>
            Code: {row['stop_code']}
            """,

            tooltip=row["stop_name"]

        ).add_to(m)

    # DISPLAY MAP
    st_folium(
        m,
        width=1000,
        height=600
    )