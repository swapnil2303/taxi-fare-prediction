import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("taxi_fare_model.pkl")


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Taxi Fare Prediction",
    page_icon="🚕",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🚕 Taxi Fare Prediction")

st.write(
    "Enter the trip details below to predict the estimated taxi fare."
)


# -----------------------------
# User Inputs
# -----------------------------

passenger_count = st.number_input(
    "Passenger Count",
    min_value=1,
    max_value=6,
    value=2
)

pickup_longitude = st.number_input(
    "Pickup Longitude",
    value=-73.99
)

pickup_latitude = st.number_input(
    "Pickup Latitude",
    value=40.73
)

dropoff_longitude = st.number_input(
    "Drop-off Longitude",
    value=-73.97
)

dropoff_latitude = st.number_input(
    "Drop-off Latitude",
    value=40.75
)

hour = st.number_input(
    "Pickup Hour",
    min_value=0,
    max_value=23,
    value=18
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=5
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=10
)

day_of_week = st.number_input(
    "Day of Week",
    min_value=0,
    max_value=6,
    value=0
)

year = st.number_input(
    "Year",
    min_value=2009,
    max_value=2030,
    value=2010
)

trip_distance = st.number_input(
    "Trip Distance (KM)",
    min_value=0.1,
    value=3.2
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("🚕 Predict Fare"):

    input_data = pd.DataFrame({
        "passenger_count": [passenger_count],
        "pickup_longitude": [pickup_longitude],
        "pickup_latitude": [pickup_latitude],
        "dropoff_longitude": [dropoff_longitude],
        "dropoff_latitude": [dropoff_latitude],
        "hour": [hour],
        "day": [day],
        "month": [month],
        "day_of_week": [day_of_week],
        "year": [year],
        "trip_distance": [trip_distance]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Taxi Fare: ${prediction[0]:.2f}"
    )