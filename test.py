import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("Explore Sample Datasets with Filtering")

# Dataset 1: City Residents
def generate_city_df():
    cities = ['New York', 'Los Angeles', 'Chicago', 'Austin']
    data = {
        'Name': [f'Resident {i}' for i in range(20)],
        'Age': np.random.randint(18, 80, size=20),
        'City': np.random.choice(cities, size=20)
    }
    return pd.DataFrame(data)

# Dataset 2: Middle School Students
def generate_school_df():
    grades = ['6th', '7th', '8th']
    subjects = ['Math', 'Science', 'History', 'English']
    data = {
        'Student Name': [f'Student {i}' for i in range(30)],
        'Grade': np.random.choice(grades, size=30),
        'Favorite Subject': np.random.choice(subjects, size=30)
    }
    return pd.DataFrame(data)

# Dataset 3: Tech Companies
def generate_company_df():
    companies = [f'Company {i}' for i in range(1, 16)]
    industries = ['AI', 'E-commerce', 'FinTech', 'Cybersecurity']
    countries = ['USA', 'Germany', 'India', 'Canada']
    data = {
        'Company': companies,
        'Industry': np.random.choice(industries, size=15),
        'Country': np.random.choice(countries, size=15)
    }
    return pd.DataFrame(data)

# Dataset 4: Book Library
def generate_books_df():
    genres = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Fantasy']
    authors = [f'Author {i}' for i in range(10)]
    data = {
        'Title': [f'Book {i}' for i in range(25)],
        'Author': np.random.choice(authors, size=25),
        'Genre': np.random.choice(genres, size=25)
    }
    return pd.DataFrame(data)

# Dataset 5: Environmental Sensors
def generate_sensors_df():
    locations = ['Forest', 'Desert', 'Mountain', 'Urban']
    data = {
        'Sensor ID': [f'Sensor-{i:03d}' for i in range(1, 21)],
        'Temperature (°C)': np.round(np.random.uniform(-10, 40, size=20), 1),
        'Location': np.random.choice(locations, size=20)
    }
    return pd.DataFrame(data)

# Dictionary of datasets and filter columns
datasets = {
    "City Residents": (generate_city_df(), "City"),
    "Middle School Students": (generate_school_df(), "Grade"),
    "Tech Companies": (generate_company_df(), "Industry"),
    "Library Books": (generate_books_df(), "Genre"),
    "Environmental Sensors": (generate_sensors_df(), "Location"),
}

# Select a dataset
dataset_name = st.selectbox("Select a dataset to explore", list(datasets.keys()))
df, filter_col = datasets[dataset_name]

# Multiselect filter
options = sorted(df[filter_col].unique())
selected_filters = st.multiselect(f"Filter by {filter_col}", options=options, default=options)

# Apply filter
filtered_df = df[df[filter_col].isin(selected_filters)]

# Show results
st.markdown(f"### Filtered Data: {dataset
