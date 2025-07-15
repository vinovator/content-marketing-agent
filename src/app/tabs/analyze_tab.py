# src/app/tabs/analyze_tab.py

import streamlit as st
import sys
from pathlib import Path

# Ensure we can import from src/analyzers
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from src.analyzers.trend_sentiment_analyzer import analyze_trends_and_sentiment
from src.analyzers.trend_viz import plot_sentiment_distribution, plot_top_keywords, plot_wordcloud, plot_clusters
from src.data_collection.collect_data import collect_data

import matplotlib.pyplot as plt
import seaborn as sns

def render_analyze_tab():
    st.header("Step 3: Collect & Analyze Trends")

    st.info("This section will scrape data, analyze sentiment, extract keywords, and visualize insights like sentiment distribution, keyword clouds, or clusters.")

    # Check theme and platform selection
    themes = st.session_state.get("themes", [])
    platforms = st.session_state.get("selected_platforms", [])
    platform_selections = st.session_state.get("platform_selections", {})

    if not themes or not platforms:
        st.warning("Please complete Steps 1 and 2 before analyzing trends.")
        return

    st.subheader("🎯 Selected Themes")
    st.write(", ".join(themes))

    st.subheader("📡 Selected Platforms")
    st.write(", ".join(platforms))

    # Run button
    if st.button("Run Trend & Sentiment Analysis"):
        with st.spinner("📥 Collecting fresh data from selected platforms..."):
            try:
                collect_data(themes, platform_selections)
                st.success("✅ Data collection completed.")
            except Exception as e:
                st.error(f"❌ Failed to collect data: {e}")
                return

        with st.spinner("Analyzing content and extracting insights..."):
            try:
                df, reduced_embeddings = analyze_trends_and_sentiment()
                if df.empty:
                    st.warning("⚠️ No content found after analysis.")
                    return
                
                # ✅ Store analyzed dataframe in session for next steps
                st.session_state.analyzed_df = df
                st.session_state.reduced_embeddings = reduced_embeddings

                st.success("✅ Analysis complete.")
            except Exception as e:
                st.error(f"❌ Failed to analyze data: {e}")
                return

            # Show preview table
            st.markdown("---")
            st.subheader("📄 Preview Analyzed Content")
            cols_to_display = ["title", "url", "source", "publishedAt", "sentiment_label", "top_keywords", "cluster"]
            st.dataframe(df[cols_to_display].sort_values(by="publishedAt", ascending=False), 
                         column_config={"url": st.column_config.LinkColumn()},
                         use_container_width=True
                         )

            # Visualizations
            st.markdown("---")
            st.subheader("📈 Sentiment Distribution")
            #fig1 = plt.figure()
            plot_sentiment_distribution(df)
            st.pyplot(plt.gcf())

            st.markdown("---")
            st.subheader("🔑 Top Keywords")
            #fig2 = plt.figure()
            plot_top_keywords(df)
            st.pyplot(plt.gcf())

            st.markdown("---")
            st.subheader("☁️ Keyword Word Cloud")
            #fig3 = plt.figure()
            plot_wordcloud(df)
            st.pyplot(plt.gcf())

            st.markdown("---")
            st.subheader("🧠 Topic Clusters")
            #fig4 = plt.figure()
            plot_clusters(df, reduced_embeddings)
            st.pyplot(plt.gcf())

    else:
        st.info("Click the button above to run trend and sentiment analysis.")

