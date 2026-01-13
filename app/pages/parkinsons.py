import streamlit as st
from app.utils.model_loader import get_parkinsons_model


def render_parkinsons_page():
    """Render the Parkinson's disease prediction page."""
    st.title("Parkinson's Disease Prediction using ML")

    parkinsons_model = get_parkinsons_model()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col5:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        rap = st.text_input("MDVP:RAP")
    with col2:
        ppq = st.text_input("MDVP:PPQ")
    with col3:
        ddp = st.text_input("Jitter:DDP")
    with col4:
        shimmer = st.text_input("MDVP:Shimmer")
    with col5:
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")

    with col1:
        apq3 = st.text_input("Shimmer:APQ3")
    with col2:
        apq5 = st.text_input("Shimmer:APQ5")
    with col3:
        apq = st.text_input("MDVP:APQ")
    with col4:
        dda = st.text_input("Shimmer:DDA")
    with col5:
        nhr = st.text_input("NHR")

    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rpde = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        d2 = st.text_input("D2")
    with col2:
        ppe = st.text_input("PPE")

    diagnosis = ""

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [
                float(fo),
                float(fhi),
                float(flo),
                float(jitter_percent),
                float(jitter_abs),
                float(rap),
                float(ppq),
                float(ddp),
                float(shimmer),
                float(shimmer_db),
                float(apq3),
                float(apq5),
                float(apq),
                float(dda),
                float(nhr),
                float(hnr),
                float(rpde),
                float(dfa),
                float(spread1),
                float(spread2),
                float(d2),
                float(ppe),
            ]

            prediction = parkinsons_model.predict([user_input])

            if prediction[0] == 1:
                diagnosis = "The person has Parkinson's disease"
            else:
                diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            diagnosis = "Please enter valid numeric values for all fields"

    if diagnosis:
        st.success(diagnosis)
