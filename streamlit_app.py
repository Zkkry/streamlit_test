import streamlit as st 
import requests

# Set the app title 
st.title('SEA TIDE FORECAST !!') 

# Add a welcome message 
st.write('Welcome to my Streamlit app BOSS!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)


#API calls
response = requests.get('https://www.worldtides.info/api/v2?heights&lat=5.4204&lon=100.3436&key=YOUR_API_KEY')

if response.status_code == 200:
    data = response.json()
    st.write('Output:')
    st.json(data)  # nicely formatted JSON output
else:
    st.error(f"API call failed with status code: {response.status_code}")


