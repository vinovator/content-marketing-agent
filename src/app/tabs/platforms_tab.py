# src/app/tabs/platforms_tab.py

import streamlit as st

def render_platforms_tab():
    st.header("Step 2: Select Platforms to Scrape")

    st.info("Choose content platforms to scrape and provide any required parameters.")

    st.markdown("""
    Select platforms you want to collect content from. Some platforms may require additional input.
    """)

    # 🔹 Get previously defined themes
    themes = st.session_state.get("themes", [])

    if not themes:
        st.warning("⚠️ No themes found. Please go back to Step 1 and define themes first.")
        return

    st.subheader("🎯 Selected Themes")
    st.write(", ".join(themes))

    # Supported platforms and required input types
    platforms_with_inputs = {
        "Google News": {"type": "theme"},
        "Reddit": {"type": "custom", "label": "Enter Subreddits (comma-separated)", "help": "e.g. ai, marketing, startups"},
        "Hacker News": {"type": "theme"},
        "YouTube": {"type": "custom", "label": "Enter YouTube search queries (comma-separated)", "help": ""},
        "RSS Feeds": {"type": "custom", "label": "Enter RSS Feed URLs (one per line)", "help": ""},
        "Web Search": {"type": "theme"},
    }

    # Platform selection
    selected_platforms = st.multiselect(
        "Select Platforms to Scrape",
        options=list(platforms_with_inputs.keys()),
    )

    # Input collectors
    platform_inputs = {}

    for platform in selected_platforms:
        config = platforms_with_inputs[platform]
        if config["type"] == "custom":
            st.markdown(f"**{platform} Input**")
            if platform == "RSS Feeds":
                value = st.text_area(config["label"], help=config.get("help", ""))
                inputs = [line.strip() for line in value.splitlines() if line.strip()]
            else:
                value = st.text_area(config["label"], help=config.get("help", ""))
                inputs = [item.strip() for item in value.split(",") if item.strip()]
            platform_inputs[platform] = {"type": "custom", "value": inputs}
        else:
            # Use themes as default input
            platform_inputs[platform] = {"type": "theme", "value": themes}

    # Save state
    if st.button("✅ Save Platform Selections"):
        st.session_state.selected_platforms = selected_platforms
        st.session_state.platform_selections = platform_inputs
        st.success("Platform selections saved.")

        # Summary display
        st.markdown("---")
        st.subheader("📋 Configuration Summary")

        st.markdown("### 🎯 Themes")
        st.write(", ".join(themes))

        st.markdown("### ✅ Platforms and Inputs")
        for platform in selected_platforms:
            input_type = platform_inputs[platform]["type"]
            value = platform_inputs[platform]["value"]
            st.markdown(f"**{platform}** — Input Type: `{input_type}`")
            st.write(value)

