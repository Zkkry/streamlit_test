import streamlit as st
import requests

# App title
st.title("🌤️ Real-Time Weather App (WeatherAPI.com)")

# API Key
API_KEY = "749ef7b6d061443ca12121812252905"  # <-- Replace with your real WeatherAPI.com key

# User input
city = st.text_input("Enter a city name:", "Pahang")

if city:
    # API request
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract and display data
        location = data["location"]
        current = data["current"]

        st.subheader(f"📍 Weather in {location['name']}, {location['country']}")
        st.write(f"🕒 Local Time: {location['localtime']}")
        st.write(f"🌡️ Temperature: {current['temp_c']}°C")
        st.write(f"☁️ Condition: {current['condition']['text']}")
        st.write(f"💧 Humidity: {current['humidity']}%")
        st.write(f"🌬️ Wind: {current['wind_kph']} km/h")

        # Optional: Air Quality Index (AQI)
        if "air_quality" in current:
            st.subheader("🧪 Air Quality Index (AQI):")
            aqi = current["air_quality"]
            st.write(f"PM2.5: {aqi['pm2_5']:.2f}")
            st.write(f"PM10: {aqi['pm10']:.2f}")
            st.write(f"CO: {aqi['co']:.2f} μg/m³")
            st.write(f"O₃: {aqi['o3']:.2f} μg/m³")
    else:
        st.error("❌ Failed to retrieve data. Please check your API key and city name.")
        st.code(response.text)
