# 🧭 UI Planning Roadmap for Content Marketing Agent

This document outlines the UI structure, flow, and integration logic for the Streamlit frontend of the **Content Marketing Agent**. The app supports marketing content creation using AI and trend data, structured into 8 logical steps.

---

## 📁 File Location
- **Main UI script:** `src/app/ui.py`
- **Backend Modules:** under `src/`
- **Run with:** `streamlit run src/app/ui.py`

---

## 🧱 Overall Layout
- Use **Streamlit sidebar** for step-by-step navigation.
- Use **tabs/pages** or `radio` buttons for linear workflow.
- Use **session state** to track data selections across tabs.

---

## 🧭 8-Step Workflow & UI Plan

### 1. 🎯 Define Themes
**Purpose**: Capture broad marketing areas of interest.
- UI:
  - Textarea input for comma-separated themes (e.g. "AI Agents, Sustainable Tech")
  - Save to `st.session_state.themes`

---

### 2. 🌐 Select Platforms
**Purpose**: Let user choose platforms to scrape.
- UI:
  - Multi-select dropdown: ["Google", "HackerNews", "Reddit", "RSS", "News", "YouTube"]
  - For each platform:
    - If keyword-based: auto-fill from themes
    - If not (e.g. Reddit): ask user to enter subreddit names
- State:
  - Store config in `st.session_state.scraper_config`
  
| Platform    | User Input Required?                  |
| ----------- | ------------------------------------- |
| Google News | No (uses saved themes)                |
| Reddit      | Yes (list of subreddits)              |
| Hacker News | No (uses themes as tags/search terms) |
| YouTube     | Yes (search queries or channels)      |
| RSS Feeds   | Yes (URLs of feeds)                   |
| Web Search  | No (uses themes as keywords)          |


---

### 3. 📊 Collect & Analyze Trends
**Purpose**: Scrape platforms and analyze for trends and sentiment.
- Triggers `data_collection/collect_data.py`
- Backend uses:
  - Scrapers: `src/scrapers/*.py`
  - Database: SQLite (`data/content_data.db`)
  - Analyzer: `analyzers/trend_sentiment_analyzer.py`
- UI:
  - Button: “Collect & Analyze”
  - Display:
    - Sentiment distribution chart
    - Keyword clusters (via UMAP or KMeans)
    - WordCloud of trending terms
    - Table of extracted keywords

---

### 4. 🧠 Generate Article Topics
**Purpose**: Use top keywords to generate potential article titles + descriptions.
- Uses `agents/topic_generator.py`
- UI:
  - Multi-select trending keywords
  - Button: “Generate Topics”
  - Display list of suggested topics
  - Allow user to select favorites
- State:
  - Store selected topics in `st.session_state.selected_topics`

---

### 5. ✍️ Write Briefs
**Purpose**: Generate brief content outlines for selected topics.
- Uses `agents/brief_writer.py`
- UI:
  - Display selected topics
  - Button: “Generate Briefs”
  - Show formatted briefs (title + objective + target audience etc.)
  - Allow edit/approval
- State:
  - Store approved briefs in `st.session_state.selected_briefs`

---

### 6. 📝 Draft Content
**Purpose**: Generate full-length draft articles from briefs.
- Uses `agents/content_drafter.py`
- UI:
  - Show brief
  - Button: “Generate Draft”
  - Display draft with formatting
- State:
  - Store drafts in `st.session_state.selected_drafts`

---

### 7. 💄 Polish Content
**Purpose**: Enhance tone, grammar, SEO of drafts.
- Uses `agents/content_polisher.py`
- UI:
  - Select one or more drafts
  - Choose style (formal, casual, SEO, etc.)
  - Button: “Polish”
  - Show side-by-side comparison
- State:
  - Store polished version in `st.session_state.polished_drafts`

---

### 8. 📤 Export Content
**Purpose**: Export polished content to chosen formats.
- UI:
  - Select final content
  - Choose format:
    - .docx
    - .md (markdown)
    - Email copy
  - Button: “Export”
- Backend:
  - Use `python-docx` or Markdown conversion
  - Trigger file download

---

## 🧰 Technical Stack Summary

| Layer          | Tool / Lib              |
|----------------|-------------------------|
| Frontend       | Streamlit               |
| Storage        | SQLite (`content_data.db`) |
| Scrapers       | Custom Python scrapers in `src/scrapers` |
| Analysis       | NLP with `nltk`, `scikit-learn`, `pandas` |
| LLM Agents     | OpenAI via `langchain` agents |
| Visualization  | `matplotlib`, `seaborn`, `wordcloud`, `plotly` |
| Export         | `python-docx`, Markdown, `streamlit.download_button` |

---

## 🔁 State Management
Use `st.session_state` to store:
- `themes`
- `scraper_config`
- `trend_keywords`
- `selected_topics`
- `selected_briefs`
- `selected_drafts`
- `polished_drafts`

---

## 🗂 Folder References

```text
src/
│
├── app/
│   └── ui.py                     # Streamlit UI
│
├── analyzers/
│   ├── trend_sentiment_analyzer.py
│   └── trend_viz.py
│
├── agents/
│   ├── topic_generator.py
│   ├── brief_writer.py
│   ├── content_drafter.py
│   └── content_polisher.py
│
├── data_collection/
│   └── collect_data.py
│
├── scrapers/
│   ├── google_search_scraper.py
│   ├── hackernews_scraper.py
│   ├── news_scraper.py
│   ├── reddit_scraper.py
│   ├── rss_scraper.py
│   └── youtube_scraper.py

