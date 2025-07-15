# src/app/tabs/draft_tab.py

import streamlit as st
import sys
from pathlib import Path

# Add root directory to sys.path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from src.agents.content_drafter import generate_draft

def render_draft_tab():
    st.header("Step 6: Draft Content")

    st.info("Generate full content drafts from selected briefs using the Content Drafter agent.")

    # Check if briefs are available
    selected_briefs = st.session_state.get("selected_briefs", [])

    if not selected_briefs:
        st.warning("⚠️ No briefs selected. Please complete Step 5: Write Briefs.")
        return

    st.subheader("🧠 Selected Briefs")
    for i, brief_data in enumerate(selected_briefs):
        with st.expander(f"📌 {brief_data.get('title', 'Untitled')}"):
            st.markdown(f"**Description:** {brief_data.get('description', '-')}")

            brief = brief_data.get("brief", {})

            if isinstance(brief, dict):
                st.markdown("**Outline:**")
                for point in brief.get("outline", []):
                    st.markdown(f"- {point}")
                st.markdown(f"**Tone:** {brief.get('tone', '-')}")
                st.markdown(f"**Audience:** {brief.get('audience', '-')}")
                st.markdown(f"**Call to Action:** {brief.get('cta', '-')}")
            else:
                st.markdown(f"**Brief Summary:** {brief}")


    st.markdown("---")
    st.subheader("⚙️ Draft Generation Settings")
    #temperature = st.slider("🎨 Creativity Level (LLM Temperature)", 0.0, 1.0, 0.7, 0.1)

    if st.button("🚀 Generate Draft Content"):
        with st.spinner("Generating drafts..."):
            generated_drafts = []
            for brief in selected_briefs:
                brief_input = {
                    "title": brief.get("title"),
                    "description": brief.get("description"),
                    "brief": brief.get("brief"),
                    "tone": brief.get("tone"),
                    "audience": brief.get("audience"),
                    "outline": brief.get("outline"),
                    "cta": brief.get("cta"),
                }
                draft = generate_draft(brief_input, model_name="gpt-4o-mini")
                generated_drafts.append({**brief_input, "draft": draft})

            st.session_state.generated_drafts = generated_drafts
            st.success(f"✅ Generated {len(generated_drafts)} draft(s).")


    # Display generated drafts
    selected_draft_indices = []

    if "generated_drafts" in st.session_state:
        drafts = st.session_state.generated_drafts

        st.markdown("---")
        st.subheader("📝 Draft Articles")
        for i, draft in enumerate(drafts):
            with st.expander(f"📄 {draft['title']}"):
                
                #st.markdown(f"**Brief Summary:** {draft['brief']}")
                brief = brief_data.get("brief", {})

                if isinstance(brief, dict):
                    st.markdown("**Outline:**")
                    for point in brief.get("outline", []):
                        st.markdown(f"- {point}")
                    st.markdown(f"**Tone:** {brief.get('tone', '-')}")
                    st.markdown(f"**Audience:** {brief.get('audience', '-')}")
                    st.markdown(f"**Call to Action:** {brief.get('cta', '-')}")
                else:
                    st.markdown(f"**Brief Summary:** {brief}")

                st.markdown("**Draft Content:**")
                st.markdown(draft["draft"])
                if st.checkbox("✅ Select this draft for polishing", key=f"select_draft_{i}"):
                    selected_draft_indices.append(i)

    # Store selected drafts for polishing
    if selected_draft_indices:
        st.session_state.selected_drafts = [drafts[i] for i in selected_draft_indices]
        st.success(f"✅ {len(selected_draft_indices)} draft(s) selected for polishing.")
    else:
        st.info("No drafts selected for polishing.")