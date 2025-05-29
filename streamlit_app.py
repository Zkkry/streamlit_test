import streamlit as st
import requests

# Function to call WeatherAPI
def get_weatherapi_weather(city):
    api_key = "749ef7b6d061443ca12121812252905"  # Replace with your actual key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()

# Streamlit UI
st.title("Current Weather (via WeatherAPI)")

city = st.text_input("Enter a city name:")

if city:
    data = get_weatherapi_weather(city)

    if "current" in data:
        st.subheader(f"Weather in {data['location']['name']}, {data['location']['country']}")
        st.write(f"Temperature: {data['current']['temp_c']} °C")
        st.write(f"Feels Like: {data['current']['feelslike_c']} °C")
        st.write(f"Condition: {data['current']['condition']['text']}")
        st.image("https:" + data['current']['condition']['icon'])
        st.write(f"Humidity: {data['current']['humidity']}%")
        st.write(f"Wind: {data['current']['wind_kph']} kph {data['current']['wind_dir']}")
    else:
        st.error("City not found or API error. Please check the city name and try again.")
