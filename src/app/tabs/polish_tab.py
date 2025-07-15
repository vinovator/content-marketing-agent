# src/app/tabs/polish_tab.py

import streamlit as st
import sys
from pathlib import Path

# Add src to sys.path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from src.agents.content_polisher import polish_draft

def render_polish_tab():
    st.header("Step 7: Polish Content")
    st.info("Polish and optimize drafts for tone, clarity, and SEO using the Content Polisher agent.")

    selected_drafts = st.session_state.get("selected_drafts", [])

    if not selected_drafts:
        st.warning("⚠️ No drafts selected. Please complete Step 6: Draft Content.")
        return

    st.subheader("📝 Selected Drafts to Polish")

    polished_outputs = []
    polish_triggered = False

    for i, draft in enumerate(selected_drafts):
        with st.expander(f"📄 {draft.get('title', f'Draft {i+1}')}"):

            # Extract tone and audience from brief
            brief_data = draft.get("brief", {})
            default_tone = brief_data.get("tone", "Professional")
            default_audience = brief_data.get("audience", "Business Decision Makers")

            # 🆕 Show metadata used during generation
            st.markdown(f"**🎯 Original Tone:** {default_tone}")
            st.markdown(f"**👥 Original Audience:** {default_audience}")

            st.markdown("**📝 Original Draft:**")
            st.markdown(draft.get("draft", ""))

            # Allow override for polishing
            tone = st.selectbox(
                "🎯 Choose New Tone (Optional)",
                ["Professional", "Conversational", "Formal", "Friendly"],
                index=["Professional", "Conversational", "Formal", "Friendly"].index(default_tone),
                key=f"tone_{i}"
            )

            audience = st.text_input(
                "👥 Target Audience for Polish",
                value=default_audience,
                key=f"audience_{i}"
            )

            if st.button("✨ Polish This Draft", key=f"polish_{i}"):
                with st.spinner("Polishing..."):
                    polished = polish_draft(
                        draft=draft.get("draft", ""),
                        tone=tone,
                        audience=audience,
                        model_name="gpt-4o-mini"
                    )
                    polished_outputs.append({
                        "title": draft.get("title", f"Draft {i+1}"),
                        "original": draft.get("draft", ""),
                        "polished": polished,
                        "tone": tone,
                        "audience": audience,
                        "brief": {
                            **draft.get("brief", {}),
                            "tone": tone,
                            "audience": audience,
                        },
                    })
                    st.session_state[f"polished_{i}"] = polished
                    st.success("✅ Draft polished!")


    # Show polished drafts (either from current or session)
    final_selection = []
    st.markdown("---")
    st.subheader("🔍 Polished Content Preview")

    for i, draft in enumerate(selected_drafts):
        polished = st.session_state.get(f"polished_{i}")
        if polished:
            with st.expander(f"📄 {draft['title']} (Polished)"):
                #st.markdown("**Original Draft:**")
                #st.code(draft["draft"], language="markdown")

                st.markdown("**✨ Polished Draft:**")
                st.markdown(polished)

                if st.checkbox("✅ Select this for export", key=f"select_polished_{i}"):
                    final_selection.append({
                        "title": draft.get("title"),
                        "polished": polished,
                        "tone": tone,
                        "audience": audience,
                        "brief": {
                            **draft.get("brief", {}),
                            "tone": tone,
                            "audience": audience,
                        },
                    })

    # Save final export list
    if final_selection:
        st.session_state.final_export_ready = final_selection
        st.success(f"{len(final_selection)} draft(s) marked for export.")
    else:
        st.info("No drafts selected for export yet.")
