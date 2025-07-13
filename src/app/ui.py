# src/app/ui.py

import streamlit as st
from pathlib import Path
import sys

# Add the parent directory to the system path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir / "src"))

# Import tab modules
from app.tabs.themes_tab import render_themes_tab
from app.tabs.platforms_tab import render_platforms_tab
from app.tabs.analyze_tab import render_analyze_tab
from app.tabs.topics_tab import render_topics_tab
from app.tabs.briefs_tab import render_briefs_tab
from app.tabs.draft_tab import render_draft_tab
from app.tabs.polish_tab import render_polish_tab
from app.tabs.export_tab import render_export_tab

# set page configuration
st.set_page_config(
    page_title="Content Marketing Agent",
    layout="wide"
)

st.title("Content Marketing Agent")

# Sidebar navigation
st.sidebar.title("Navigation")
tabs = [
    "1. Define Themes",
    "2. Select Platforms",
    "3. Collect & Analyze Trends",
    "4. Generate Topics",
    "5. Write Briefs",
    "6. Draft Content",
    "7. Polish Content",
    "8. Export"    
]

selected_tab = st.sidebar.radio("Navigate Steps", tabs)

# Session state setup (extendable)
if "themes" not in st.session_state:
    st.session_state.themes = []

# Tab routing
if selected_tab == tabs[0]:
    render_themes_tab()
elif selected_tab == tabs[1]:
    render_platforms_tab()
elif selected_tab == tabs[2]:
    render_analyze_tab()
elif selected_tab == tabs[3]:
    render_topics_tab()
elif selected_tab == tabs[4]:
    render_briefs_tab()
elif selected_tab == tabs[5]:
    render_draft_tab()
elif selected_tab == tabs[6]:
    render_polish_tab()
elif selected_tab == tabs[7]:
    render_export_tab()

