import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image 
df = pd.read_csv("apartments_rent_pl_2024_01.csv")
df.drop(columns=['condition' , 'id' , 'buildingMaterial' , 'collegeDistance' , 'restaurantDistance'], inplace=True)
df.drop_duplicates(inplace=True)
df.dropna(subset=[ 'schoolDistance' , 'hasElevator','pharmacyDistance',
                  'kindergartenDistance', 'postOfficeDistance' , 'floorCount' , 'clinicDistance',  
                   'poiCount']
          , inplace=True) # drop rows with missing values

from sklearn.model_selection import train_test_split
x_train  = df.drop(columns=['price'])
y_train = df['price']

x_train , x_test , y_train , y_test = train_test_split(x_train , y_train , test_size=0.2 , random_state=42)

df['type'].fillna(x_train['type'].mode()[0] , inplace=True)           
df['floor'].fillna(x_train['floor'].mode()[0] ,inplace = True)
df['floorCount'].fillna(x_train['floorCount'].mode()[0] ,inplace = True)
df['buildYear'].fillna(x_train['buildYear'].mode()[0] , inplace=True)

c1, c33, c2 = st.columns([5, 1, 4])

# First Chart: The 5 most expensive apartments in any governorate
with c1:
    st.markdown(
        "<h3 style='text-align: left; color: white; font-family: Verdana, sans-serif;'>The 5 most expensive apartments in any governorate</h3>",
        unsafe_allow_html=True
    )

    max_price = df.groupby('city')['price'].max().reset_index().sort_values(by='price', ascending=False).head(5)
    st.plotly_chart(px.bar(
        max_price, 
        x='city', 
        y='price', 
        template='plotly_dark',
        labels={'city': 'City', 'price': 'Max Price'},
        color_discrete_sequence=px.colors.sequential.Electric_r, 
        title='Top 5 cities with highest price',
        width=500,  # Adjusted width for better alignment
        height=400
    ))

# Second Chart: The five cities with the most ancient buildings
with c2:
    st.markdown(
        "<h3 style='text-align: center; color: white; font-family: Arial, sans-serif; font-weight: bold;'>The five cities with the most ancient buildings</h3>",
        unsafe_allow_html=True
    )

    oldest = df.sort_values(by='buildYear').head(5)
    st.plotly_chart(px.bar(
        oldest, 
        x='city', 
        y='buildYear', 
        template='plotly_dark',
        labels={'city': 'City', 'buildYear': 'Build Year'},
        color_discrete_sequence=px.colors.sequential.Electric_r, 
        title='Oldest Cities',
        color='buildYear',
        width=500,  # Adjusted width for better alignment
        height=400
    ))

c1, c33, c2 = st.columns([4, 1, 4])

# First chart: Top 5 cities with the most amenities
with c1:
    st.markdown(
        "<h3 style='text-align: left; color: white; font-family: Verdana, sans-serif;'>Which cities have the most amenities</h3>",
        unsafe_allow_html=True
    )
    amenities_columns = ['hasParkingSpace', 'hasBalcony', 'hasElevator', 'hasSecurity', 'hasStorageRoom']

    for col in amenities_columns:
        df[col] = df[col].apply(lambda x: 1 if x.lower() == 'yes' else 0)

    df['amenities_count'] = df[amenities_columns].sum(axis=1)
    amenities_columns_group = df.sort_values(by='amenities_count', ascending=False).head(5)

    st.plotly_chart(px.bar(
        amenities_columns_group, 
        x='city', 
        y='amenities_count', 
        template='plotly_dark', 
        labels={'city': 'City', 'amenities_count': 'Number of amenities'},
        color_discrete_sequence=px.colors.sequential.Electric_r, 
        title='Top 5 cities with highest number of amenities',
        width=500, 
        height=400 ,
        
    ))

# Second chart: Top 5 cities with highest price per meter
with c2:
    st.markdown(
        "<h3 style='text-align: center; color: white; font-family: Arial, sans-serif; font-weight: bold;'>The five most expensive governorates with the highest price per meter</h3>",
        unsafe_allow_html=True
    )
    df['price_per_meter'] = df['price'] / df['squareMeters']

    price_per_meter_group = df.groupby('city')['price_per_meter'].mean().sort_values(ascending=False).head(5)
    
    st.plotly_chart(px.bar(
        price_per_meter_group.reset_index(), 
        x='city', 
        y='price_per_meter', 
        template='plotly_dark', 
        labels={'city': 'City', 'price_per_meter': 'Price per meter'},
        color_discrete_sequence=px.colors.sequential.Electric_r, 
        title='Top 5 cities with highest price per meter',
        width=500, 
        height=400
        , color='price_per_meter'
    ))
c1, c33, c2 = st.columns([4, 1, 4]) 

# Third chart: Top 5 cities with the highest number of rooms
# with c1:
#     st.markdown(
#         "<h3 style='text-align: left; color: white; font-family: Verdana, sans-serif;'> Which governorates have the highest average price for properties with more than three rooms?</h3>",
#         unsafe_allow_html=True
#     )
#     filtered_df = df[df['rooms'] > 3]

# # Group by 'city' (or 'governorate' if that's the actual column name) and calculate the mean price
# governorates_avg_price = filtered_df.groupby('city')['price'].mean().reset_index()

# # Sort by the highest average price
# top_5_governorates = governorates_avg_price.sort_values(by='price', ascending=False).head(5)

# # Draw a bar chart
# st.plotly_chart(px.bar(top_5_governorates, x='city', y='price', template='plotly_dark',
#        color_discrete_sequence=px.colors.sequential.Electric_r,
#          title='Top 5 Governorates with Highest Average Price'  ,width= 500 , height=400))





  







