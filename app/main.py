import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
from app.components.sidebar import render_sidebar
from app.pages.diabetes import render_diabetes_page
from app.pages.heart_disease import render_heart_disease_page
from app.pages.parkinsons import render_parkinsons_page
from app.utils.constants import DIABETES, HEART_DISEASE, PARKINSONS


def main():
    """Main application entry point."""
    selected = render_sidebar()

    if selected == DIABETES:
        render_diabetes_page()
    elif selected == HEART_DISEASE:
        render_heart_disease_page()
    elif selected == PARKINSONS:
        render_parkinsons_page()


if __name__ == "__main__":
    main()
