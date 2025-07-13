# src/app/tabs/platforms_tab.py

import streamlit as st

def render_platforms_tab():
    st.header("Step 2: Select Platforms to Scrape")

    st.info("This section will let users choose platforms like Google, Reddit, YouTube, etc., and enter any required parameters per platform (e.g., subreddits for Reddit).")

    st.markdown("""
    Select platforms you want to collect content from. Some platforms may require additional input.
    """)

    # 🔹 Display themes selected in Step 1
    themes = st.session_state.get("themes", [])
    if themes:
        st.subheader("🎯 Selected Themes")
        st.write(", ".join(themes))

        # Platform checkboxes
        platforms = {
            "Google News": {},
            "Reddit": {"subreddits": ""},
            "Hacker News": {},
            "YouTube": {"queries": ""},
            "RSS Feeds": {"rss_urls": ""},
            "Web Search": {}
        }

        selected = st.multiselect(
            "Select Platforms to Scrape",
            options=list(platforms.keys()),
            default=[]
        )

        # Collect inputs for selected platforms
        platform_inputs = {}

        if "Reddit" in selected:
            subreddits = st.text_area("Enter Subreddits (comma-separated)", help="e.g. ai, marketing, startups")
            platform_inputs["Reddit"] = [s.strip() for s in subreddits.split(",") if s.strip()]

        if "YouTube" in selected:
            queries = st.text_area("Enter YouTube search terms or channels (comma-separated)")
            platform_inputs["YouTube"] = [q.strip() for q in queries.split(",") if q.strip()]

        if "RSS Feeds" in selected:
            rss_urls = st.text_area("Enter RSS feed URLs (one per line)")
            platform_inputs["RSS Feeds"] = [url.strip() for url in rss_urls.splitlines() if url.strip()]

        # Save platform selection and inputs
        if st.button("Save Platform Selections"):
            st.session_state.selected_platforms = selected # List of selected platform names
            st.session_state.platform_inputs = platform_inputs # Dict of inputs per selected platform
            st.success("Platform selections saved.")

            st.markdown("---")
            st.subheader("Your Configuration Summary")

            st.markdown("### 🎯 Themes")
            st.write(", ".join(themes) if themes else "None")

            st.markdown("### Selected Platforms")
            for platform in selected:
                st.markdown(f"**{platform}**")
                inputs = platform_inputs.get(platform, None)
                if inputs:
                    st.write(inputs)
                else:
                    if themes:
                        st.markdown("Using themes as input:")
                        st.write(themes)
                    else:
                        st.write("_No input and no themes found_")

    else:
        st.warning("No themes found. Please go back to Step 1 and define themes.")

    st.markdown("---")

        