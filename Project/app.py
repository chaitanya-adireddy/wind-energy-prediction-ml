import streamlit as st
import joblib
import numpy as np
import requests
import os

# Load trained model
model = joblib.load("wind_energy_model.pkl")

st.set_page_config(page_title="Wind Energy Prediction", layout="wide")

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- WELCOME PAGE ----------
if st.session_state.page == "home":

    st.markdown("<h1 style='text-align:center;'>🌬 Wind Mill Power Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Predict the energy output of windmills using Machine Learning</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.info("🌤 Weather Forecast\n\nGet real-time weather data for selected cities")

    with col2:
        st.info("⚡ Power Prediction\n\nPredict wind turbine energy output using ML")

    if st.button("Get Started ➜"):
        st.session_state.page = "weather"

# ---------- WEATHER PAGE ----------
elif st.session_state.page == "weather":

    st.header("🌤 Weather & ⚡ Power Prediction")

    city_list = [
        "Mumbai", "Delhi", "Hyderabad", "Chennai", "Bangalore",
        "Kolkata", "Pune", "Ahmedabad", "Visakhapatnam", "Vijayawada",
        "Tirupati", "Kakinada", "Rajahmundry", "London", "New York", "Tokyo"
    ]

    col_left, col_right = st.columns(2)

    # -------- LEFT: WEATHER --------
    with col_left:
        st.subheader("🌤 Weather Forecast")

        city = st.selectbox("Select City", city_list)

        if st.button("Get Weather"):

            API_KEY = os.getenv("OPENWEATHER_API_KEY")
            if not API_KEY:
              st.error("API key not found. Please set environment variable.")
              st.stop()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

            try:
                response = requests.get(url, timeout=10)
                data = response.json()

                if response.status_code == 200:

                    temp = data["main"]["temp"]
                    humidity = data["main"]["humidity"]
                    pressure = data["main"]["pressure"]
                    wind_speed = data["wind"]["speed"]
                    wind_direction = data["wind"]["deg"]  # ✅ FIXED

                    st.success(f"Weather Data for {city}")

                    st.metric("🌡 Temperature", f"{temp} °C")
                    st.metric("💧 Humidity", f"{humidity} %")
                    st.metric("ضغط Pressure", f"{pressure} hPa")
                    st.metric("🌬 Wind Speed", f"{wind_speed} m/s")
                    st.metric("🧭 Wind Direction", f"{wind_direction} °")

                    # Save values for prediction
                    st.session_state.wind_speed = wind_speed
                    st.session_state.wind_direction = wind_direction

                else:
                    st.error(data.get("message", "Weather data not found"))

            except Exception as e:
                st.error("API request failed")
                st.write(e)

    # -------- RIGHT: PREDICTION --------
    with col_right:
        st.subheader("⚡ Wind Power Prediction")

        wind_speed = st.number_input(
            "Wind Speed (m/s)",
            value=st.session_state.get("wind_speed", 5.0)
        )

        wind_direction = st.number_input(
            "Wind Direction (°)",
            value=st.session_state.get("wind_direction", 0.0)
        )

        if st.button("Predict Power"):

            input_data = np.array([[wind_speed, wind_direction]])
            prediction = model.predict(input_data)

            st.success(f"Predicted Power Output: {prediction[0]:.2f} kW")

    st.markdown("---")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
