# src/app/tabs/briefs_tab.py

import streamlit as st
import sys
from pathlib import Path

# Ensure we can import from src/agents
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from src.agents.brief_writer import generate_brief

def render_briefs_tab():
    st.header("Step 5: Write Briefs")

    st.info("Generate detailed briefs for selected topics to guide content drafting.")

    # Load selected topics from previous step
    selected_topics = st.session_state.get("selected_topics", [])

    if not selected_topics:
        st.warning("⚠️ Please select topics in Step 4 before generating briefs.")
        return
    
    # Display selected topics
    st.subheader("📌 Selected Topics")
    for topic in selected_topics:
        st.markdown(f"**{topic['title']}** — {topic['description']}")

    st.markdown("---")

    # Temperature slider
    # temperature = st.slider("🎨 Creativity Level (LLM Temperature)", 0.0, 1.0, 0.7, 0.1)

    # Generate briefs
    if st.button("📝 Generate Briefs"):
        with st.spinner("Generating content briefs..."):
            generated_briefs = []
            for topic in selected_topics:
                brief = generate_brief(topic["title"], topic["description"], model_name="gpt-4o-mini")
                generated_briefs.append({
                    "title": topic["title"],
                    "description": topic["description"],
                    "brief": brief
                })

        st.session_state.generated_briefs = generated_briefs
        st.success(f"✅ {len(generated_briefs)} briefs generated.")

    # Display generated briefs
    generated_briefs = st.session_state.get("generated_briefs", [])
    if generated_briefs:
        st.markdown("---")
        st.subheader("📄 Generated Briefs")

        selected_briefs = []
        for i, brief_data in enumerate(generated_briefs):
            with st.expander(f"🧠 {brief_data['title']}"):
                st.markdown(f"**Topic Description:** {brief_data['description']}")
                st.markdown("**Brief:**")
                #st.markdown(brief_data["brief"])

                brief = brief_data["brief"]

                def format_key(keu):
                    return " ".join([w.capitalize() for w in keu.split("_")])

                if isinstance(brief, dict):
                    for key, value in brief.items():
                        st.markdown(f"**{format_key(key)}**:")
                        if isinstance(value, list):
                            for item in value:
                                st.markdown(f"- {item}")
                        else:
                            st.markdown(f"{value}")
                elif isinstance(brief, str):
                    try:
                        # Try parsing stringified JSON
                        import json
                        parsed = json.loads(brief)
                        for key, value in parsed.items():
                            st.markdown(f"**{format_key(key)}**:")
                            if isinstance(value, list):
                                for item in value:
                                    st.markdown(f"- {item}")
                            else:
                                st.markdown(f"{value}")
                    except Exception:
                        # Default to plain markdown
                        st.markdown(brief)
                else:
                    st.markdown(str(brief))

                if st.checkbox("Use this brief for content drafting", key=f"select_brief_{i}"):
                    selected_briefs.append(brief_data)

        st.session_state.selected_briefs = selected_briefs

        if selected_briefs:
            st.success(f"{len(selected_briefs)} brief(s) selected for drafting.")
        else:
            st.info("Select briefs you want to draft into articles.")
    else:
        st.info("No briefs generated yet.")