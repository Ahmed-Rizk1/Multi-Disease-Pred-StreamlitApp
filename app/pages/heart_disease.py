import streamlit as st
from app.utils.model_loader import get_heart_disease_model


def render_heart_disease_page():
    """Render the heart disease prediction page."""
    st.title("Heart Disease Prediction using ML")

    heart_model = get_heart_disease_model()

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain types")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")

    with col1:
        thal = st.text_input(
            "thal: 0 = normal; 1 = fixed defect; 2 = reversable defect"
        )

    diagnosis = ""

    if st.button("Heart Disease Test Result"):
        try:
            user_input = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal),
            ]

            prediction = heart_model.predict([user_input])

            if prediction[0] == 1:
                diagnosis = (
                    "The person is having heart disease , You should consult a doctor"
                )
            else:
                diagnosis = (
                    "The person does not have any heart disease, You can be healthy"
                )
        except ValueError:
            diagnosis = "Please enter valid numeric values for all fields"

    if diagnosis:
        st.success(diagnosis)
