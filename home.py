import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image


# Load the dataset
df = pd.read_csv("apartments_rent_pl_2024_01.csv")
df.drop(columns=['condition', 'id', 'buildingMaterial', 'collegeDistance', 'restaurantDistance', 'longitude', 'latitude'], inplace=True)
df.dropna(subset=['schoolDistance', 'hasElevator', 'pharmacyDistance', 'kindergartenDistance', 'postOfficeDistance', 
                  'floorCount', 'clinicDistance', 'poiCount'], inplace=True)
df['type'].fillna(df['type'].mode()[0], inplace=True)
df['floor'].fillna(df['floor'].mode()[0], inplace=True)
df['floorCount'].fillna(df['floorCount'].mode()[0], inplace=True)
df['buildYear'].fillna(df['buildYear'].mode()[0], inplace=True)

# Page title with style
st.markdown("<h1 style='text-align: center; color: #f63366; font-family: Georgia, serif;'>Welcome to the Home Page 🤓</h1>", unsafe_allow_html=True)

# Header image with custom size
st.image(r"city-paris-france-building-wallpaper-preview.jpg", use_column_width=True)

# Subheader with style
st.markdown("<h2 style='color: #f63366; font-family: Verdana, sans-serif;'>This EDA App is for Apartments in Poland</h2>", unsafe_allow_html=True)

# Data link with styled button
st.write("<span style='color: red; font-family: Arial, sans-serif; font-size: 20px;'>Data link <a style='text-decoration: none; color: #2a9df4;' href='https://www.kaggle.com/datasets/krzysztofjamroz/apartment-prices-in-poland/data'>here</a></span>", unsafe_allow_html=True)

# Checkbox to show sample data
sample = st.checkbox("Show Sample of Data")  
if sample:
    st.write(df.sample())

# Checkbox to show the head of the data
head = st.checkbox("Show Head of Data")
if head:
    st.write(df.head())    


# Checkbox to show detailed information about columns
about = st.checkbox("Show Information About All Columns")
if about:
    st.markdown("""
    - **City**: The name of the city where the property is located
    - **Type**: Type of the building
    - **Square Meters**: The size of the apartment in square meters
    - **Rooms**: Number of rooms in the apartment
    - **Floor / Floor Count**: The floor where the apartment is located and the total number of floors in the building
    - **Build Year**: The year when the building was built
    - **Centre Distance**: Distance from the city center in km
    - **POI Count**: Number of points of interest in 500m range from the apartment (schools, clinics, post offices, kindergartens, restaurants, colleges, pharmacies)
    - **Ownership**: The type of property ownership
    - **Has Features**: Whether the property has key features such as an assigned parking space, balcony, elevator, security, storage room
    """)
