# app.py

import streamlit as st
import joblib
import pandas as pd
import numpy as np
model = joblib.load('./model_filename.pkl')

# Function to preprocess input data
def preprocess_input(make, model_name, year, mileage,city,Engine_displacement):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'Company_name': [make],
        'model': [model_name],
        'year': [year],
        'mileage': [mileage],
        'city': [city],
        'Engine_displacement': [Engine_displacement]
    })

    return input_data

# Streamlit app
def main():
    st.title("Car Price Prediction App")

    # Add some Streamlit elements
    st.write("Hello, this is a Streamlit app.")
    st.button("Click me")

    # Input interface
    make = st.text_input("Enter Make:")
    model_name = st.text_input("Enter Model:")
    year = st.number_input("Enter Year:")
    mileage = st.number_input("Enter Mileage:")
    city = st.text_input("Enter city:")
    Engine_displacement = st.number_input("Enter Engine_displacement:")

    # Preprocess input data
    input_data = preprocess_input(make, model_name, year, mileage,city,Engine_displacement)

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.write(f"Predicted Car Price: {prediction}")

    

if __name__ == "__main__":
    main()
