import streamlit as st
import requests

# Set the app title
st.title('🌍 Currency Exchange Viewer')

# Add a welcome message
st.write('Welcome to my Streamlit app, BOSS! 💼')

# Create a text input
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)

# --- API Call to Get Currency Rates (Base: MYR) ---
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Dropdown for currency selection
    currencies = sorted(rates.keys())  # sorted list for better UX
    selected_currency = st.selectbox('Select a currency to convert from MYR:', currencies)

    # Show exchange rate
    exchange_rate = rates[selected_currency]
    st.success(f"1 MYR = {exchange_rate:.4f} {selected_currency}")

    # Optional: Show all rates in expandable JSON view
    with st.expander("Show all exchange rates"):
        st.json(rates)
else:
    st.error(f"API call failed with status code: {response.status_code}")
