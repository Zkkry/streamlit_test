import streamlit as st
import requests

# Set the app title
st.title('💱 MYR Currency Converter')

# Add a welcome message
st.write('Welcome to my Streamlit app, BOSS! 🚀')

# Custom message input
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)

# API Call to get currency rates (base: MYR)
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Currency selection
    currencies = sorted(rates.keys())
    selected_currency = st.selectbox('Select a currency to convert from MYR:', currencies)

    # Amount input
    amount_myr = st.number_input('Enter amount in MYR:', min_value=0.0, value=1.0, step=0.1)

    # Calculate and display result
    exchange_rate = rates[selected_currency]
    converted_amount = amount_myr * exchange_rate

    st.success(f"{amount_myr:.2f} MYR = {converted_amount:.2f} {selected_currency} (Rate: {exchange_rate:.4f})")

    # Optional: View all rates
    with st.expander("🔎 Show all exchange rates"):
        st.json(rates)
else:
    st.error(f"API call failed with status code: {response.status_code}")
