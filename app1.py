import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


model = pickle.load(open('model_1.pkl', 'rb'))

def predict_weather(precipitation, wind, temp_max, temp_min):
    input_data = np.array([[precipitation, wind, temp_max, temp_min]])
    prediction = model.predict(input_data)
    return prediction


def main():
    st.title("Weather Prediction App")
    st.sidebar.header("Input Features")

    precipitation = st.sidebar.number_input("Precipitation", value=0.0)
    wind = st.sidebar.number_input("Wind Speed", value=0.0)
    temp_max = st.sidebar.number_input("Max Temperature", value=0.0)
    temp_min = st.sidebar.number_input("Min Temperature", value=0.0)

    if st.sidebar.button("Predict"):
        result = predict_weather(precipitation, wind, temp_max, temp_min)
        weather_conditions = {0: 'drizzle', 1: 'sun', 2: 'rain', 3: 'fog', 4: 'snow'}
        prediction_text = f"The predicted weather condition is: {weather_conditions[result[0]]}"
        
        st.success(prediction_text)
        
        
        if result[0] == 0:
            st.image(Image.open('drizzle.jpeg'), caption='Drizzly Weather', width=400)
        elif result[0] == 1:
            st.image(Image.open('sunny.jpeg'), caption='Sunny Weather', width=400)
        elif result[0] == 2:
            st.image(Image.open('rainy.jpeg'), caption='Rainy Weather', width=400)
        elif result[0] == 3:
            st.image(Image.open('fog.jpeg'), caption='Foggy Weather', width=400)
        elif result[0] == 4:
            st.image(Image.open('snow.jpeg'), caption='Snowy Weather', width=400)

if __name__ == "__main__":
    main()
