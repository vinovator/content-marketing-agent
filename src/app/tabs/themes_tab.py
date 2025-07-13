# src/app/tabs/themes_tab.py

import streamlit as st

def render_themes_tab():
    st.header("Step 1: Define Marketing Themes")
    themes_input = st.text_area("Enter one or more marketing themes (comma separated)", height=100)

    if st.button("Save Themes"):
        themes = [theme.strip() for theme in themes_input.split(",") if theme.strip()]
        st.session_state.themes = themes
        st.success(f"Saved themes: {themes}")
