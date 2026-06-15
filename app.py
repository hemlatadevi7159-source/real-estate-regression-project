import streamlit as st

st.title("Real Estate Price Prediction Project")

st.write("Minor AI Project")

area = st.number_input("Area (sq ft)", 500, 10000, 2000)
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)

if st.button("Predict"):
    # Replace with your trained model
    prediction = 150 * area + 10000 * bedrooms + 8000 * bathrooms
    st.success(f"Predicted Price: ${prediction:,.2f}")
