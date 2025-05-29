import streamlit as st
import requests

# --- Config ---
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your real API key

# --- App Title ---
st.title("🌤️ Weather & Air Quality Dashboard")

# --- User Input ---
city = st.text_input("Enter city name", "Kuala Lumpur")

if city:
    # --- Get weather data ---
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_response = requests.get(weather_url)

    if weather_response.status_code == 200:
        weather_data = weather_response.json()

        # Extract weather info
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind = weather_data['wind']['speed']
        condition = weather_data['weather'][0]['description']
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']

        # Display current weather
        st.subheader(f"📍 Weather in {city.title()}")
        st.write(f"**Condition:** {condition.title()}")
        st.write(f"**Temperature:** {temp} °C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind} m/s")

        # --- Get air quality data ---
        aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        aqi_response = requests.get(aqi_url)

        if aqi_response.status_code == 200:
            aqi_data = aqi_response.json()
            aqi_index = aqi_data['list'][0]['main']['aqi']
            aqi_meaning = {
                1: "Good",
                2: "Fair",
                3: "Moderate",
                4: "Poor",
                5: "Very Poor"
            }

            st.subheader("🧭 Air Quality Index")
            st.write(f"**AQI Level:** {aqi_index} ({aqi_meaning.get(aqi_index, 'Unknown')})")

            # Optional: Show pollutant levels
            pollutants = aqi_data['list'][0]['components']
            st.markdown("**Pollutants (µg/m³):**")
            st.json(pollutants)
        else:
            st.error("Failed to retrieve air quality data.")
    else:
        st.error("City not found. Please try another.")
