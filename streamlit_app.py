import streamlit as st
import requests

st.title("🌤️ Weather App")

city = st.text_input("Enter a city name:", "Penang")
API_KEY = "4a801bd757d1677a8c5a3af8ec080464"

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.write(f"Weather in {city}")
        st.write("Temperature:", data["main"]["temp"], "°C")
        st.write("Description:", data["weather"][0]["description"])
    else:
        st.error("City not found or API error.")
        st.code(response.text)  # This shows the actual API error
