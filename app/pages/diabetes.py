import streamlit as st
from app.utils.model_loader import get_diabetes_model
from app.utils.constants import DIABETES


def render_diabetes_page():
    """Render the diabetes prediction page."""
    st.title("Diabetes Prediction using ML")

    # Load model
    diabetes_model = get_diabetes_model()

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        blood_pressure = st.text_input("Blood Pressure value")

    with col1:
        skin_thickness = st.text_input("Skin Thickness value")
    with col2:
        insulin = st.text_input("Insulin Level")
    with col3:
        bmi = st.text_input("BMI value")

    with col1:
        diabetes_pedigree = st.text_input("Diabetes Pedigree Function value")
    with col2:
        age = st.text_input("Age of the Person")

    # Prediction
    diagnosis = ""

    if st.button("Diabetes Test Result"):
        try:
            user_input = [
                float(pregnancies),
                float(glucose),
                float(blood_pressure),
                float(skin_thickness),
                float(insulin),
                float(bmi),
                float(diabetes_pedigree),
                float(age),
            ]

            prediction = diabetes_model.predict([user_input])

            if prediction[0] == 1:
                diagnosis = "The person is diabetic"
            else:
                diagnosis = "The person is not diabetic"
        except ValueError:
            diagnosis = "Please enter valid numeric values for all fields"

    if diagnosis:
        st.success(diagnosis)
