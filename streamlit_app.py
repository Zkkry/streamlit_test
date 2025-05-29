import streamlit as st
import requests

# App title
st.title("🌊 Real-Time Marine Weather App")

# API Key
API_KEY = "bdcd10e4-3c83-11f0-89da-0242ac130006-bdcd1148-3c83-11f0-89da-0242ac130006"

# User input: coordinates
st.subheader("📍 Enter Coordinates")
lat = st.number_input("Latitude", value=5.4164)  # Default: Penang
lon = st.number_input("Longitude", value=100.3327)

if lat and lon:
    url = f"https://api.stormglass.io/v2/weather/point?lat={lat}&lng={lon}&params=waveHeight,swellHeight,windSpeed,airTemperature"
    headers = {
        "Authorization": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        hours = data.get("hours", [])

        if hours:
            current = hours[0]  # Get the most recent hour
            st.subheader(f"🌤️ Marine Weather Conditions")
            st.write(f"🌊 Wave Height: {current['waveHeight'].get('sg', 'N/A')} m")
            st.write(f"🌊 Swell Height: {current['swellHeight'].get('sg', 'N/A')} m")
            st.write(f"💨 Wind Speed: {current['windSpeed'].get('sg', 'N/A')} m/s")
            st.write(f"🌡️ Air Temperature: {current['airTemperature'].get('sg', 'N/A')} °C")
        else:
            st.warning("No hourly data available.")
    else:
        st.error("❌ Failed to retrieve data. Please check your API key and coordinates.")
        st.code(response.text)
