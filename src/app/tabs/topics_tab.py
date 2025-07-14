# src/app/tabs/topics_tab.py

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Ensure we can import from src/analyzers
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir / "src"))

from agents.topic_generator import generate_topics


def render_topics_tab():
    st.header("Step 4: Generate Article Topics")

    st.info("Use the analyzed insights to generate a list of potential article topics using the AI agent.")

    # Ensure analyzed data is available
    df = st.session_state.get("analyzed_df")
    if df is None:
        st.warning("⚠️ Please complete Step 3: Analyze Trends before generating topics.")
        return

    st.subheader("📊 Top Keywords Extracted")
    top_keywords_flat = [kw for sublist in df["top_keywords"] for kw in sublist]
    unique_keywords = sorted(set(top_keywords_flat))
    st.markdown(f"Detected **{len(unique_keywords)} unique keywords** from analyzed content.")

    # Allow user to choose keywords to use
    selected_keywords = st.multiselect(
        "✍️ Select keywords to base topic generation on:",
        options=unique_keywords,
        default=unique_keywords[:5]
    )

    # Optional temperature setting
    # temperature = st.slider("🎨 Creativity Level (LLM Temperature)", 0.0, 1.0, 0.7, 0.1)

    if st.button("🚀 Generate Topics"):
        if not selected_keywords:
            st.warning("Please select at least one keyword.")
            return

        with st.spinner("Generating article topics using LLM..."):
            topics = generate_topics(selected_keywords, model_name="gpt-4o-mini")

        if isinstance(topics, str):
            st.error("⚠️ Could not parse LLM output. Raw response:")
            st.code(topics)
            return

        st.session_state.generated_topics = topics

        st.success(f"✅ {len(topics)} topics generated.")

        st.markdown("---")
        st.subheader("📝 Suggested Topics")

        selected_topic_indices = []
        for idx, topic in enumerate(topics):
            with st.expander(f"📌 {topic['title']}"):
                st.write(topic["description"])
                if st.checkbox("Select this topic", key=f"select_topic_{idx}"):
                    selected_topic_indices.append(idx)

        # Store only selected topics
        st.session_state.selected_topics = [topics[i] for i in selected_topic_indices]

        if selected_topic_indices:
            st.markdown("---")
            st.success(f"{len(selected_topic_indices)} topic(s) selected for brief generation.")
        else:
            st.info("No topics selected yet.")

    elif "generated_topics" in st.session_state:
        
        topics = st.session_state.generated_topics

        st.markdown("---")
        st.subheader("📝 Suggested Topics (Previously Generated)")

        selected_topic_indices = []
        for idx, topic in enumerate(topics):
            with st.expander(f"📌 {topic['title']}"):
                st.write(topic["description"])
                if st.checkbox("Select this topic", key=f"select_topic_{idx}"):
                    selected_topic_indices.append(idx)

        st.session_state.selected_topics = [topics[i] for i in selected_topic_indices]

        if selected_topic_indices:
            st.markdown("---")
            st.success(f"{len(selected_topic_indices)} topic(s) selected for brief generation.")
        else:
            st.info("No topics selected yet.")

