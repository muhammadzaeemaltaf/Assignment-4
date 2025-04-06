import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Height (cm)", 100, 250, 170)
weight = st.slider("Weight (kg)", 30, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is: {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("1. Underweight: BMI < 18.5")
st.write("2. Normal weight: 18.5 ≤ BMI < 24.9")
st.write("3. Overweight: 25 ≤ BMI < 29.9")
st.write("4. Obesity: BMI ≥ 30")
