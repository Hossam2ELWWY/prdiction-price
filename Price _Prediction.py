import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image
# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report 
df = pd.read_csv(r"C:\Users\Maydoum\Downloads\Compressed\apartments_pl_2024_01.csv")
df.dropna(subset=[ 'schoolDistance' , 'hasElevator','pharmacyDistance',
                   'kindergartenDistance', 'postOfficeDistance' , 'floorCount' , 'clinicDistance',  
                    'poiCount']
           , inplace=True)
# df.drop(columns=['hasSecurity' , 'ownership' , 'hasParkingSpace'    
#                   , 'hasElevator' ,'hasStorageRoom' , 'hasBalcony'], inplace=True)  






# df['type'].fillna(df['type'].mode()[0] , inplace=True)
# df['floor'].fillna(df['floor'].mode()[0] ,inplace = True)
# df['floorCount'].fillna(df['floorCount'].mode()[0] ,inplace = True)
# df['buildYear'].fillna(df['buildYear'].mode()[0] , inplace=True)
# df['squareMeters_cat'] = pd.cut(df['squareMeters'] , bins = [0 , 50 , 100 ,150] , labels = ["<50" , "50-100" , ">100"])
# df.drop(columns=['condition' , 'id' , 'buildingMaterial' , 'collegeDistance' , 'restaurantDistance'], inplace=True)
# df = df[df['floor'] < 20]
st.title('Welcome to the Price Prediction Page 📈  ')
# #face = social_media[social_media['platform'] == 'Facebook']
# floor_user = st.selectbox('floor' , df['floor'].unique() )
# hasElevator = st.selectbox('hasElevator' , df['hasElevator'].unique() )
# security = st.selectbox('security' , df['hasSecurity'].unique() )
# balcony = st.selectbox('balcony' , df['hasBalcony'].unique() )
# rooms_user = st.selectbox('rooms' , df['rooms'].unique() )
# square_meters_user = st.selectbox('squareMeters' , df['squareMeters_cat'].unique() )
# filtered_data = df[
#     (df['floor'] == floor_user) &
#     (df['hasElevator'] == hasElevator) &
#     (df['hasSecurity'] == security) &
#     (df['hasBalcony'] == balcony) &
#     (df['rooms'] == rooms_user) &
#     (df['squareMeters_cat'] == square_meters_user)
# ]
# prediction = filtered_data['price'].mean()
# if st.button('Predict'):
#     try :
#         prediction.round(2)
#     except :
#         prediction = 'nan' 
#     if prediction == 'nan' :
#         st.warning('there is no apartement with your needs')
#     else:
#         st.markdown('<p style="font-size:24px; color:red;">The predicted price is.</p>', unsafe_allow_html=True)
#         st.success(int(filtered_data['price'].mean().round(0))) 
       

# # st.write('### Result')
# # if st.button('Predict'):
    
#load the model and preprocesor
import pickle
xgb = pickle.load(open('xgb.pkl', 'rb'))
preproceesor = pickle.load(open('preproceesor.pkl', 'rb')) 
city = st.selectbox('city' , df['city'].unique() )
floor = st.selectbox('floor' , df['floor'].sort_values().unique() )

square_meters_user = st.number_input('squareMeters' , min_value=0 , max_value=3000) 
floor_count = st.number_input('floorCount' , min_value=1 , max_value=41)
rooms_user = st.selectbox('rooms' , df['rooms'].sort_values().unique() )
school_user = st.number_input('schoolDistance km betwwen 0 - 5 ' , min_value=0 , max_value=5)
storage = st.selectbox('storage' , df['hasStorageRoom'].unique() )
elvator = st.selectbox('elvator' , df['hasElevator'].unique() )
build_year = st.selectbox('buildYear' , df['buildYear'].sort_values().unique() )
security = st.selectbox('security' , df['hasSecurity'].unique() )
balcony = st.selectbox('balcony' , df['hasBalcony'].unique() )
parking = st.selectbox('parking' , df['hasParkingSpace'].unique() )
pharmacy = st.number_input('pharmacyDistance KM  Between 0 - 5' , min_value=0 , max_value=5)
kinder = st.number_input('kinderDistance  KM  Between 0 - 5' , min_value=0 , max_value=5)
post = st.number_input('postDistance  KM  Between 0 - 5' , min_value=0 , max_value=5)
clinic = st.number_input('clinicDistance' , min_value=0 , max_value=5)
collage = st.number_input('collageDistance' , min_value=0 , max_value=5)
type = st.selectbox('type' , df['type'].unique() )





new_data = pd.DataFrame({
    'city': [city],
    'type': [type],
    'squareMeters': [square_meters_user],
    'rooms': [rooms_user],
    'floor': [floor],
    'floorCount': [floor_count],
    'buildYear': [build_year],
    'latitude': [51.7509],
    'longitude': [19.42446],
    'centreDistance': [3.99],
    'poiCount': [16.0],
    'schoolDistance': [school_user],
    'clinicDistance': [clinic],
    'postOfficeDistance': [post],
    'kindergartenDistance': [kinder],
    'restaurantDistance': [0.072],
    'collegeDistance': [collage],
    'pharmacyDistance': [pharmacy],
    'ownership': ['private'],
    'hasElevator': [elvator],
    'hasSecurity': [security],
    'hasBalcony': [balcony],
    'hasParkingSpace': [parking],
    'hasStorageRoom': [storage],


})


    # Transform the data using the preprocessor
transformed_data = preproceesor.transform(new_data)

    # Predict using the model
prediction = xgb.predict(transformed_data)
if st.button('Predict'):
    st.success(int(prediction[0]))
# print(prediction)
