import streamlit as st
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
})

# Filter by City
selected_city = st.selectbox("Filter by city", options=["All"] + df["City"].unique().tolist())

# Apply filter
if selected_city != "All":
    filtered_df = df[df["City"] == selected_city]
else:
    filtered_df = df

# Show the filtered table
st.dataframe(filtered_df)
