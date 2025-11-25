import streamlit as st
import pandas as pd


st.title("Cha Selling Dashboard")


file = st.file_uploader("Upload your Cha selling data (CSV)", type=["csv"])


if file:
    data = pd.read_csv(file)
    st.subheader("Uploaded Data")
    st.dataframe(data)
    
if file:
    st.subheader("Sales Summary")
    st.write(data.describe())
    
if file:
    citys = data['City'].unique()
    selected_city = st.selectbox("Select City", citys)
    filtered_data = data[data["City"] == selected_city]
    st.dataframe(filtered_data)