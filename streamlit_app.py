import streamlit as st
import requests

st.title("🌦️ Weather Checker")

city = st.text_input("Enter a city name:", "Penang")

if city:
    API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace this with your real key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city.title()}")
        st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
        st.write(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        st.write(f"🌥️ Condition: {data['weather'][0]['description'].title()}")
    else:
        st.error("City not found or API error.")
