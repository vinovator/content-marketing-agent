# 🧠 Content Marketing Agent

An AI-powered platform that automates your **end-to-end content marketing workflow** – from trend collection to polished, export-ready articles using LLMs.

---

## 🚀 Features

- 🌐 Scrape content from Google, Reddit, YouTube, News, Hacker News, RSS
- 🔍 Analyze trends, keywords, sentiment, and semantic clusters
- 🧠 Generate article topics with LLMs
- 📝 Write structured briefs and long-form articles
- ✨ Polish content for tone, SEO, and clarity
- 📤 Export to Word (`.docx`), Markdown (`.md`), or email format

---

## 🧭 Master Workflow

1. **Define Themes** – Provide one or more marketing themes (e.g. "AI Agents", "Green Hydrogen")
2. **Select Platforms** – Choose one or more sources like Reddit, Google News, YouTube, etc.
3. **Scrape + Analyze** – Collect real-time data and extract sentiment, keywords, clusters
4. **Generate Topics** – Use LLMs to create clickable article ideas
5. **Write Briefs** – Turn each topic into a structured article brief
6. **Draft Content** – Generate long-form content
7. **Polish** – Refine tone, clarity, and structure
8. **Export** – Save articles in multiple formats

---

## 📂 Folder Structure

```bash
content-marketing-agent/
│
├── data/                             # Scraped + analyzed data storage
│   ├── content_data.db               # SQLite database for structured content
│   └── combined_data.csv             # Flattened snapshot of raw content
│
├── guides/                           # Internal documentation
│   ├── content-marketing-agent-notes.md
│   ├── google-api-setup-guide.md
│   ├── TECH_DEBT.md
│   └── ui-planning-guide.md
│
├── notebooks/                        # Development notebooks
│   ├── 01_data_collection.ipynb
│   ├── 02_content_analysis.ipynb
│   ├── 03_ai_agent_core.ipynb
│   └── 04_ui_planning.ipynb
│
├── src/
│   ├── agents/                       # LLM-powered automation
│   │   ├── topic_generator.py
│   │   ├── brief_writer.py
│   │   ├── content_drafter.py
│   │   └── content_polisher.py
│   │
│   ├── analyzers/                    # NLP logic and visualizations
│   │   ├── trend_sentiment_analyzer.py
│   │   └── trend_viz.py
│   │
│   ├── app/                          # Streamlit UI
│   │   ├── ui.py
│   │   └── tabs/
│   │       ├── themes_tab.py
│   │       ├── platforms_tab.py
│   │       ├── analyze_tab.py
│   │       ├── topics_tab.py
│   │       ├── briefs_tab.py
│   │       ├── draft_tab.py
│   │       ├── polish_tab.py
│   │       └── export_tab.py
│   │
│   ├── data_collection/             # Central scraping logic
│   │   └── collect_data.py
│   │
│   ├── database/                    # DB interactions (currently empty)
│   │   └── db_manager.py (planned)
│   │
│   ├── scrapers/                    # Source-specific scrapers
│   │   ├── google_search_scraper.py
│   │   ├── reddit_scraper.py
│   │   ├── hackernews_scraper.py
│   │   ├── news_scraper.py
│   │   ├── rss_scraper.py
│   │   └── youtube_scraper.py
│   │
│   └── utils/                       # Helper functions (currently empty)
│       ├── text_cleaning.py (planned)
│       └── exporter.py (planned)
│
├── requirements.txt
├── .env                             # API keys
└── README.md
````

---

## 🧪 Local Setup

### 1. Clone

```bash
git clone https://github.com/yourname/content-marketing-agent.git
cd content-marketing-agent
```

### 2. Create Environment

```bash
conda create -n cma python=3.9
conda activate cma
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your-api-key-here
```

---

## 🖥️ UI Tab Flow (Streamlit)

| Step | Tab Name         | Description                            |
| ---- | ---------------- | -------------------------------------- |
| 1    | Define Themes    | Enter broad content themes             |
| 2    | Select Platforms | Choose sources and scrape config       |
| 3    | Analyze Trends   | Extract keywords, sentiments, clusters |
| 4    | Generate Topics  | LLM topic suggestions                  |
| 5    | Write Briefs     | Generate structured briefs per topic   |
| 6    | Draft Content    | Long-form content from each brief      |
| 7    | Polish Content   | Refine tone, grammar, flow             |
| 8    | Export           | Save content as `.docx`, `.md`, email  |

---

## 📊 Scrapers Summary

| Platform   | Script                     | Notes                         |
| ---------- | -------------------------- | ----------------------------- |
| Google     | `google_search_scraper.py` | SERP-based scraping           |
| Reddit     | `reddit_scraper.py`        | Needs subreddit + keyword     |
| HackerNews | `hackernews_scraper.py`    | Top/Best stories              |
| RSS Feeds  | `rss_scraper.py`           | Simple feedparser integration |
| YouTube    | `youtube_scraper.py`       | Basic metadata + query search |
| NewsAPI    | `news_scraper.py`          | Requires NewsAPI key          |

---

## 🔧 Known Tech Debt

Refer [`guides/TECH_DEBT.md`](./guides/TECH_DEBT.md) for current limitations, UI inconsistencies, and cleanup priorities.

---

## 🧠 Tech Stack

* **Python 3.9**
* **Streamlit** – UI framework
* **OpenAI (via LangChain)** – LLM integration
* **SQLite** – Content persistence
* **scikit-learn / NLTK / spaCy** – NLP pipeline
* **Matplotlib / WordCloud / Seaborn** – Visuals
* **fpdf / python-docx** – Export generation

---

## 📈 Example: Run Analysis from Notebook

```python
from src.analyzers.trend_sentiment_analyzer import analyze_trends_and_sentiment

df, embeddings = analyze_trends_and_sentiment()
df.head()
```

---

## 🧑 Maintainer

**Vinoth Haldorai**
[LinkedIn](https://linkedin.com/in/...) • [GitHub](https://github.com/...)

---

## 📜 License

MIT License — free for personal + commercial use.

---