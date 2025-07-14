# src/app/tabs/themes_tab.py

import streamlit as st

def render_themes_tab():
    st.header("Step 1: Define Marketing Themes")
    st.markdown("""
        Use this step to define the broad **themes** you want to explore in your content strategy.
        These themes will guide scraping, analysis, and topic generation in later steps.
    """)

    themes_input = st.text_area("Enter one or more marketing themes (comma separated)", height=100)

    if st.button("Save Themes"):
        themes = [theme.strip() for theme in themes_input.split(",") if theme.strip()]
        if themes:
            st.session_state.themes = themes
            st.success(f"Saved themes: {themes}")
        else:
            st.warning("Please enter at least one theme.")

    # Display current themes if available
    if "themes" in st.session_state and st.session_state.themes:
        st.subheader("Current Saved Themes")

        for i, theme in enumerate(st.session_state.themes,1):
            st.markdown(f"{i}. **{theme}**")

        # Clear session button
        if st.button("Clear Themes"):
            st.session_state.themes = []
            st.rerun()  # Refreshes the UI