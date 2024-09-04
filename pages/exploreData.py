import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("apartments_rent_pl_2024_01.csv")
df.drop(columns=['condition', 'id', 'buildingMaterial', 'collegeDistance', 'restaurantDistance'], inplace=True)

# Page Title
st.title('Real Estate Market Overview in Poland 📈')

# Section: Average Price
st.header('Average Apartment Prices in Poland')
st.plotly_chart(
    px.box(df, x='price', template='plotly_dark', color_discrete_sequence=px.colors.sequential.Electric_r),
    use_container_width=True
)

# Layout for Two Columns
c1, c2 = st.columns(2)

# Square Meters vs Price
with c1:
    st.subheader('Square Meters vs Price')
    st.plotly_chart(px.scatter(df, x='squareMeters', y='price', template='plotly_dark',
                               color_discrete_sequence=px.colors.sequential.Electric_r, width=600, height=400))
    st.markdown('<p style="font-size:20px; color:orange;">More square meters generally mean a higher price.</p>', unsafe_allow_html=True)

# City vs Price
with c2:
    st.subheader('City vs Average Price')
    city_price_df = df.groupby('city')['price'].mean().reset_index()
    st.plotly_chart(px.bar(city_price_df, x='price', y='city', template='plotly_dark',
                           color_discrete_sequence=px.colors.sequential.Electric_r, color='price', width=600, height=400))
    st.markdown('<p style="font-size:20px; color:orange;">The highest average real estate prices are found in Warszawa.</p>', unsafe_allow_html=True)

# New Row for Next Two Plots
c1, c2 = st.columns(2)

# Rooms vs Price
with c1:
    st.subheader('Rooms vs Price')
    rooms_price_df = df.groupby('rooms')['price'].median().reset_index()
    st.plotly_chart(px.bar(rooms_price_df, x='rooms', y='price', template='plotly_dark',
                           color_discrete_sequence=px.colors.sequential.Electric_r, color='rooms'))
    st.markdown('<p style="font-size:20px; color:orange;">More rooms generally mean a higher price.</p>', unsafe_allow_html=True)

# Floor vs Price
with c2:
    st.subheader('Floor vs Price')
    floor_price_df = df.groupby('floor')['price'].sum().reset_index().sort_values(by='floor')
    st.plotly_chart(px.line(floor_price_df, x='floor', y='price', template='plotly_dark',
                            color_discrete_sequence=px.colors.sequential.Electric_r))
    st.markdown('<p style="font-size:20px; color:orange;">The highest prices are found on the ground floor.</p>', unsafe_allow_html=True)

# New Row for Final Two Plots
c1, c2 = st.columns(2)

# Building Year vs Price
with c1:
    st.subheader('Building Year vs Price')
    bins = [1850, 1900, 2000, 2024]
    labels = ['Old', 'Medium', 'Modern']
    df['year_group'] = pd.cut(df['buildYear'], bins=bins, labels=labels)
    year_group_price_df = df.groupby('year_group')['price'].sum().reset_index().sort_values(by='price')
    st.plotly_chart(px.bar(year_group_price_df, x='year_group', y='price', template='plotly_dark',
                           color_discrete_sequence=px.colors.sequential.Electric_r, color='year_group'))
    st.markdown('<p style="font-size:20px; color:orange;">The highest prices are found in modern buildings.</p>', unsafe_allow_html=True)

# Ownership vs Price
with c2:
    st.subheader('Ownership vs Price')
    ownership_price_df = df.groupby('ownership')['price'].sum().reset_index().sort_values(by='price')
    st.plotly_chart(px.bar(ownership_price_df, x='ownership', y='price', template='plotly_dark',
                           color_discrete_sequence=px.colors.sequential.Electric_r, color='ownership'))
    st.markdown('<p style="font-size:20px; color:orange;">Condominium ownership typically has the highest prices.</p>', unsafe_allow_html=True)


