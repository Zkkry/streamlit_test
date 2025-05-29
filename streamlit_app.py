import streamlit as st
import requests

st.title("🌤️ Weather App")

API_KEY = "cb367eaa6af232c7c8bca6a77714c7ca" 

city = st.text_input("Enter city name:", "Pahang")

if city:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city}")
        st.write("🌡️ Temp:", data["main"]["temp"], "°C")
        st.write("💧 Humidity:", data["main"]["humidity"], "%")
        st.write("🌬️ Wind:", data["wind"]["speed"], "m/s")
    else:
        st.error("City not found or API error.")
        st.code(response.text)
