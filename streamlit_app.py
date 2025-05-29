import streamlit as st
import requests
import datetime

# Function to call WeatherAPI
def get_weatherapi_weather(city):
    api_key = "749ef7b6d061443ca12121812252905"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()

# Function to call Stormglass API (uses lat/lon)
def get_stormglass_weather(lat, lon):
    api_key = "bdcd10e4-3c83-11f0-89da-0242ac130006-bdcd1148-3c83-11f0-89da-0242ac130006"
    end_time = datetime.datetime.utcnow().isoformat()

    url = f"https://api.stormglass.io/v2/weather/point"
    params = {
        'lat': lat,
        'lng': lon,
        'params': 'airTemperature,humidity,windSpeed',
        'source': 'noaa',
        'end': end_time,
    }

    headers = {
        'Authorization': api_key
    }

    response = requests.get(url, params=params, headers=headers)
    return response.json()

# Streamlit UI
st.title("Weather from WeatherAPI and Stormglass")

city = st.text_input("Enter a city name:")

if city:
    # Call WeatherAPI
    weatherapi_data = get_weatherapi_weather(city)
    
    if "current" in weatherapi_data:
        st.subheader("WeatherAPI Data")
        st.write(f"Temperature: {weatherapi_data['current']['temp_c']} °C")
        st.write(f"Condition: {weatherapi_data['current']['condition']['text']}")
        lat = weatherapi_data['location']['lat']
        lon = weatherapi_data['location']['lon']

        # Call Stormglass
        stormglass_data = get_stormglass_weather(lat, lon)

        st.subheader("Stormglass Data (NOAA Source)")
        try:
            hour_data = stormglass_data['hours'][0]
            st.write(f"Air Temperature: {hour_data['airTemperature']['noaa']} °C")
            st.write(f"Humidity: {hour_data['humidity']['noaa']} %")
            st.write(f"Wind Speed: {hour_data['windSpeed']['noaa']} m/s")
        except (KeyError, IndexError):
            st.error("Stormglass data not available for this location right now.")
    else:
        st.error("City not found or WeatherAPI error.")
