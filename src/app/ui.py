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
st.markdown("---")

# Sidebar navigation
st.sidebar.title("Workflow")

# Sidebar navigation
tabs = {
    "Step 1 - **Define Themes**": render_themes_tab,
    "Step 2 - **Select Platforms**": render_platforms_tab,
    "Step 3 - **Analyze Trends**": render_analyze_tab,
    "Step 4 - **Generate Topics**": render_topics_tab,
    "Step 5 - **Write Briefs**": render_briefs_tab,
    "Step 6 - **Draft Content**": render_draft_tab,
    "Step 7 - **Polish Content**": render_polish_tab,
    "Step 8 - **Export**": render_export_tab,
}

# Define tab order
tab_order = list(tabs.keys())

# Initialize tab order and current tab in session state
if "tab_order" not in st.session_state:
    st.session_state.tab_order = tab_order

if "current_tab" not in st.session_state:
    st.session_state.current_tab = tab_order[0]

# Sidebar tab selection
selected_tab = st.sidebar.radio(
    "🔎 Navigate Steps",
    tab_order,
    index=tab_order.index(st.session_state.current_tab),
    )

# Update session state with selection
st.session_state.current_tab = selected_tab

# === Render the tab content ===
tabs[selected_tab]()  # Call the appropriate tab render function

# === Navigation Buttons at the bottom ===
st.markdown("---")
col1, col2 = st.columns([1, 1])
current_index = tab_order.index(selected_tab)

with col1:
    if current_index > 0:
        if st.button("⬅️ Previous Step"):
            st.session_state.current_tab = tab_order[current_index - 1]
            st.rerun()

with col2:
    if current_index < len(tab_order) - 1:
        if st.button("Next Step ➡️"):
            st.session_state.current_tab = tab_order[current_index + 1]
            st.rerun()