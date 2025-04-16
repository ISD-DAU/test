import streamlit as st
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
})

# Multiselect for filtering by city
selected_cities = st.multiselect(
    "Filter by city (you can select multiple)", 
    options=df["City"].unique().tolist(),
    default=df["City"].unique().tolist()  # Show all by default
)

# Filter DataFrame based on selection
if selected_cities:
    filtered_df = df[df["City"].isin(selected_cities)]
else:
    filtered_df = pd.DataFrame(columns=df.columns)  # Empty DataFrame if none selected
st.title('city data')
# Show filtered DataFrame
st.dataframe(filtered_df)
