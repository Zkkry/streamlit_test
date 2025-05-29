import streamlit as st
import requests

st.title("🌤️ Weather App")

API_KEY = "749ef7b6d061443ca12121812252905" 

city = st.text_input("Enter city name:", "Pahang")

if city:
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=749ef7b6d061443ca12121812252905&q=Penang")

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city}")
        st.write("🌡️ Temp:", data["main"]["temp"], "°C")
        st.write("💧 Humidity:", data["main"]["humidity"], "%")
        st.write("🌬️ Wind:", data["wind"]["speed"], "m/s")
    else:
        st.error("City not found or API error.")
        st.code(response.text)
