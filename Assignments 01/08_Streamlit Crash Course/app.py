import streamlit as st
import joblib

model = joblib.load('linear_regression_model.pkl')

st.title("Linear Regression Prediction App")
st.write("Enter the features to get the prediction.")

feature_value = st.number_input("Enter the feature value:", min_value=0, max_value=100, value=2)

if st.button("Predict"):
    prediction = model.predict([[feature_value]])[0][0].item()
    st.write(f"The predicted value is: {prediction:.2f}")