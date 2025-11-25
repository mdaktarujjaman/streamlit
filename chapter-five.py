import streamlit as st
import requests


st.title("Chapter Five: Making API Requests with Streamlit")
amount = st.number_input("Enter the amount of INR", min_value=1, )


tergated_currency = st.selectbox("Select the currency to convert to", ["USD", "EUR", "GBP", "JPY", "AUD"], key="currency")

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rete = data["rates"][tergated_currency]
        converted_amount = amount * rete
        st.success(f"{amount} INR is equal to {converted_amount:.2f} {tergated_currency}")
    else:
        st.error("Failed to retrieve data from the API.")
        st.stop()