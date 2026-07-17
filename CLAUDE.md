# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (create/activate a venv first)
pip install -r requirements.txt

# Run the app (this IS the application — there is no CLI or test suite)
streamlit run app.py
```

The app serves on port 8501. NLTK corpora (`punkt`, `stopwords`, `vader_lexicon`) download automatically at import time in the analyzer; `nltk.txt` tells Streamlit Cloud to pre-fetch `punkt`. There are no automated tests, linters, or build steps configured — verify changes by running the Streamlit app and stepping through the workflow.

## Configuration

Copy `env-example.txt` to `.env` and fill in keys. `OPENAI_API_KEY` is required for all AI agents (Steps 4–7). Scraper keys (`REDDIT_CLIENT_ID/SECRET/USER_AGENT`, `YOUTUBE_API_KEY`, `GOOGLE_API_KEY`, `GOOGLE_CSE_ID`, `NEWS_API_KEY`) are each only needed for their platform. See `guides/google-api-setup-guide.md` for Google/YouTube setup.

## Architecture

An 8-step linear content pipeline exposed as a Streamlit multi-tab UI. The steps run in order, each consuming the previous step's output:

**Scrapers → collect_data → analyzer → agents → export**

### The pipeline

1. **Scrapers** (`src/scrapers/*.py`) — one module per platform (Reddit/PRAW, Hacker News, RSS, Google CSE, YouTube, NewsAPI). Each exposes a single `fetch_*` function returning records with the standard columns **`title, url, publishedAt, source`**. New scrapers must match this shape.
2. **`src/data_collection/collect_data.py`** — orchestrates scrapers based on user platform selections, concatenates results, dedupes on `title+url`, and persists to **both** `data/combined_data.csv` and `data/content_data.db` (SQLite table `content`, written with `if_exists="replace"`).
3. **`src/analyzers/trend_sentiment_analyzer.py`** — `analyze_trends_and_sentiment()` reads the `content` table back from SQLite (not the in-memory DataFrame), then runs: text cleaning → TF-IDF → NMF topic modeling → per-title keyword extraction → VADER sentiment → SentenceTransformer (`all-MiniLM-L6-v2`) embeddings → KMeans clustering → PCA to 2D. Returns `(df, reduced_embeddings)`. `trend_viz.py` renders the plots.
4. **Agents** (`src/agents/*.py`) — `generate_topics` → `generate_brief` → `generate_draft` → `polish_draft`, chained in that order. Each wraps LangChain `LLMChain` + `ChatOpenAI`, defaults to model `gpt-4o-mini`, and loads `OPENAI_API_KEY` via `dotenv` at module level. `generate_topics` expects the LLM to return a JSON array and falls back to returning the raw string if parsing fails — callers must handle both types.

### UI wiring

- `app.py` → `src/app/ui.py::main()`. `ui.py` owns the sidebar radio navigation and the ordered `tabs` dict mapping each step to its `render_*` function in `src/app/tabs/`. To add/reorder a step, edit that dict.
- **`st.session_state` is the data bus between tabs** — there is no other shared state. Each tab reads what earlier tabs wrote and gates on its presence (e.g. `analyzed_df` must exist before topics can be generated). Key handoff keys: `themes`, `selected_platforms` / `platform_selections`, `analyzed_df` / `reduced_embeddings`, `generated_topics` / `selected_topics`, `generated_briefs` / `selected_briefs`, `generated_drafts` / `selected_drafts`, `polished_*`, `final_export_ready`.
- Modules manipulate `sys.path` at runtime to import across the `src/` tree (`Path(__file__).resolve().parents[N]`). Imports are inconsistent — some use `from src.scrapers...`, others `from scrapers...` after a path append. Match the pattern already used in the file you are editing.

### Known gaps

`src/database/` and `src/utils/` are empty placeholders. `guides/TECH_DEBT.md` tracks open issues (notably: scrapers lack robust per-source error handling, so one failing platform can break a collection run). The `notebooks/` directory holds the original prototyping work that the `src/` modules were extracted from.
