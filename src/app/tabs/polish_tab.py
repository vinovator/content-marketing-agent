# src/app/tabs/polish_tab.py

import streamlit as st
import sys
from pathlib import Path

# Add src to sys.path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir / "src"))

from agents.content_polisher import polish_draft

def render_polish_tab():
    st.header("Step 7: Polish Content")

    st.info("Polish and optimize drafts for tone, clarity, and SEO using the Content Polisher agent.")

    selected_drafts = st.session_state.get("selected_drafts", [])

    if not selected_drafts:
        st.warning("⚠️ No drafts selected. Please complete Step 6: Draft Content.")
        return

    st.subheader("📝 Selected Drafts to Polish")

    # Polishing settings
    tone = st.selectbox("🎯 Choose desired tone for polishing", ["Professional", "Conversational", "Formal", "Friendly"], index=0)
    audience = st.text_input("👥 Target Audience", value="Business Decision Makers")

    if st.button("✨ Polish Drafts"):
        polished_outputs = []

        with st.spinner("Polishing drafts..."):
            for draft_data in selected_drafts:
                raw_draft = draft_data.get("draft", "")
                polished = polish_draft(
                    draft=raw_draft,
                    tone=tone,
                    audience=audience,
                    model_name="gpt-4o-mini"
                )
                polished_outputs.append({
                    "title": draft_data.get("title", "Untitled"),
                    "original": raw_draft,
                    "polished": polished
                })

            st.session_state.polished_drafts = polished_outputs
            st.success(f"✅ Polished {len(polished_outputs)} draft(s).")

    # Show polished drafts if available
    if "polished_drafts" in st.session_state:
        st.markdown("---")
        st.subheader("🔍 Polished Content Preview")

        final_selection = []

        for i, draft in enumerate(st.session_state.polished_drafts):
            with st.expander(f"📄 {draft['title']}"):
                st.markdown("**Original Draft:**")
                st.code(draft["original"], language="markdown")

                st.markdown("**✨ Polished Draft:**")
                st.markdown(draft["polished"])

                if st.checkbox("✅ Select this for export", key=f"select_polished_{i}"):
                    final_selection.append(draft)

        # Save selected drafts for export
        if final_selection:
            st.session_state.final_export_ready = final_selection
            st.success(f"{len(final_selection)} draft(s) marked for export.")
        else:
            st.info("No drafts selected for export yet.")


