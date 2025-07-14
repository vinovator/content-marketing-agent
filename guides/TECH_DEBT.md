# 🧱 Technical Debt Log — Content Marketing Agent

This document tracks known technical debt, UI inconsistencies, and system limitations that need to be addressed as the application evolves. Each entry includes a summary, reasoning, and actionable next steps.

---

## 1. 🧪 Analyze Tab: Preview Generated Topics with URLs

### ❗ Problem:
In the Analyze tab, we display trends and visualizations derived from collected content. However, the actual content titles, sources, and URLs used in the analysis are not previewed in the UI. This makes it difficult to trace insights back to their source and verify relevance.

### ✅ Next Steps:
- Add a collapsible "Preview Analyzed Content" section above the visualizations.
- Display a `st.dataframe()` or styled table showing:
  - `title`
  - `source`
  - `url` (clickable with markdown)
  - `publishedAt`
- Add this preview **after** data is fetched from `analyze_trends_and_sentiment()` and **before** the charts are displayed.

---

## 2. 🔁 Navigation: Add Previous & Next Buttons to Each UI Tab

### ❗ Problem:
The current UI only supports sidebar-based navigation. This can disrupt user flow, especially on small screens or during demos where linear navigation is preferred.

### ✅ Next Steps:
- At the bottom of each tab, add:
  ```python
  col1, col2 = st.columns([1, 1])
  with col1:
      if st.button("⬅️ Previous"):
          st.session_state.active_tab = "Tab Name"
  with col2:
      if st.button("Next ➡️"):
          st.session_state.active_tab = "Next Tab Name"
````

* Use a `st.session_state.active_tab` variable to manage stateful navigation.
* Update `ui.py` to reactively switch tabs based on `active_tab` session value.

---

## 3. 📝 Briefs Tab: Capitalize Brief Field Labels

### ❗ Problem:

Currently, brief data (title, description, brief content) is shown using raw dictionary keys, e.g., `"description"` or `"brief"`, which breaks the professional look of the UI.

### ✅ Next Steps:

* Create a utility function or dictionary to format keys:

  ```python
  def format_key(key):
      return " ".join([w.capitalize() for w in key.split("_")])
  ```
* Apply it when rendering keys:

  ```python
  st.markdown(f"**{format_key(key)}:** {value}")
  ```
* Avoid using raw keys directly in `st.markdown()` or `st.expander()` sections.

---

## 4. 🛡️ Scraper Functions: Add Robust Exception Handling

### ❗ Problem:

If any platform scraper fails (e.g., an invalid subreddit or unreachable RSS feed), it breaks the whole data collection pipeline. This prevents downstream analysis and results in a poor UX.

### ✅ Next Steps:

* Wrap each scraper function in `try-except` blocks inside `collect_all_data()`:

  ```python
  try:
      reddit_df = pd.DataFrame(fetch_reddit_posts(subreddit, keyword, max_results))
  except Exception as e:
      print(f"[Reddit] Skipping due to error: {e}")
      reddit_df = pd.DataFrame()
  ```
* Optionally, add logging or Streamlit warnings for partial failures.
* Ensure `all_df` is always returned with available data, even if some sources fail.

---
