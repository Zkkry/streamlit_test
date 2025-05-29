import streamlit as st
import requests

# Set the app title
st.title('🌐 Universal Currency Converter')

# Welcome message
st.write('Welcome to the most flexible currency converter, BOSS! 💱')

# Custom message
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)

# --- Get the list of currencies first ---
# Use a known currency like USD to fetch all supported currencies
initial_response = requests.get('https://api.vatcomply.com/rates?base=USD')

if initial_response.status_code == 200:
    initial_data = initial_response.json()
    currencies = sorted(initial_data.get('rates', {}).keys())

    # Let user select both base and target currencies
    base_currency = st.selectbox('Select your base currency:', currencies, index=currencies.index("MYR") if "MYR" in currencies else 0)
    target_currency = st.selectbox('Select currency to convert to:', currencies, index=currencies.index("USD") if "USD" in currencies else 0)

    # Enter amount
    amount = st.number_input(f'Enter amount in {base_currency}:', min_value=0.0, value=1.0, step=0.1)

    # Fetch conversion rate based on user base currency
    response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')

    if response.status_code == 200:
        data = response.json()
        rates = data.get('rates', {})
        
        if target_currency in rates:
            exchange_rate = rates[target_currency]
            converted_amount = amount * exchange_rate

            st.success(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency} (Rate: {exchange_rate:.4f})")
        else:
            st.warning(f"Currency '{target_currency}' not found in rates.")
        
        # Optional: Show all exchange rates from base currency
        with st.expander(f"📊 Show all exchange rates from {base_currency}"):
            st.json(rates)
    else:
        st.error(f"API call failed for base currency '{base_currency}' with status code: {response.status_code}")
else:
    st.error("Failed to load currency list. Please try again later.")
