import pandas as pd
import streamlit as st

# Title
st.title("📊 AI-Based Real Estate Growth Prediction Dashboard")

# File Upload Feature
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Load Data
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("data.csv")

# Show Dataset
st.subheader("📂 Dataset")
st.write(data)

# Weighted Growth Score Calculation (Smart Logic)
data['Growth Score'] = (
    0.5 * data['Price'] +
    0.3 * data['Rent'] +
    0.2 * data['Listings']
)

# Show Updated Data
st.subheader("📈 Growth Score Calculation")
st.write(data)

# Filter Feature
st.subheader("🔍 Filter by Area")
area = st.selectbox("Select Area", data['Area'])
filtered_data = data[data['Area'] == area]
st.write(filtered_data)

# Top Performing Areas
st.subheader("🏆 Top Performing Areas")
top_areas = data.sort_values(by='Growth Score', ascending=False)
st.write(top_areas.head(3))

# Graph
st.subheader("📊 Growth Comparison Chart")
st.bar_chart(top_areas.set_index('Area')['Growth Score'])