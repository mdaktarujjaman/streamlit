import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Chai Sales Dashboard", layout="wide")

# Title
st.title("☕ Chai Sales Dashboard")

# Load Data
df = pd.read_csv("chai_sales.csv")

# Sidebar Filters
st.sidebar.header("Filter Sales Data")
city_filter = st.sidebar.multiselect(
    "Select City",
    options=df["City"].unique(),
    default=df["City"].unique()
)

chai_filter = st.sidebar.multiselect(
    "Select Chai Type",
    options=df["Chai_Type"].unique(),
    default=df["Chai_Type"].unique()
)

# Apply Filter
filtered_df = df[
    (df["City"].isin(city_filter)) &
    (df["Chai_Type"].isin(chai_filter))
]

# Layout Columns
col1, col2 = st.columns(2)

# Chart 1: Cups Sold by Date
with col1:
    st.subheader("Cups Sold Over Time")
    fig = px.line(
        filtered_df,
        x="Date",
        y="Cups_Sold",
        color="City",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

# Chart 2: Revenue by City
with col2:
    st.subheader("Revenue by City")
    fig2 = px.bar(
        filtered_df,
        x="City",
        y="Revenue",
        color="Chai_Type",
        barmode="group"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Show Data Table
st.subheader("Filtered Data")
st.dataframe(filtered_df)
