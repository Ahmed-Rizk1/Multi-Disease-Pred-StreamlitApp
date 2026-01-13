import streamlit as st
from streamlit_option_menu import option_menu
from app.utils.constants import MENU_OPTIONS, MENU_ICONS, MENU_ICON

def render_sidebar():
    """Render the sidebar navigation menu."""
    selected = option_menu(
        'Multiple Disease Prediction System',
        MENU_OPTIONS,
        menu_icon=MENU_ICON,
        icons=MENU_ICONS,
        default_index=0
    )
    return selected
