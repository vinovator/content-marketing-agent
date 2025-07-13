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
st.sidebar.title("Workflow")

# Sidebar navigation
tabs = {
    "1. Define Themes": render_themes_tab,
    "2. Select Platforms": render_platforms_tab,
    "3. Analyze Trends": render_analyze_tab,
    "4. Generate Topics": render_topics_tab,
    "5. Write Briefs": render_briefs_tab,
    "6. Draft Content": render_draft_tab,
    "7. Polish Content": render_polish_tab,
    "8. Export": render_export_tab,
}

selected_tab = st.sidebar.radio("🔎 Navigate Steps", list(tabs.keys()))
tabs[selected_tab]()  # Call the appropriate tab render function