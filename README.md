# 🧠 Content Marketing Agent

An AI-powered platform that automates your entire **content marketing workflow** – from collecting trends across platforms to generating polished, export-ready articles using LLMs.

---

## 🚀 Features

- 🌐 Scrape real-time content from Google, Reddit, YouTube, News, Hacker News, RSS
- 🔍 Perform sentiment, keyword, and topic analysis
- 🧠 Generate article topics from trends
- 📝 Draft content briefs and long-form content
- ✨ Polish and optimize articles for tone and SEO
- 📤 Export results as Word, Markdown, or Email

---

## 🧭 Master Workflow

### Step 1: Enter Themes
- User provides one or more **themes** (e.g., "AI Agents", "Green Hydrogen")

### Step 2: Select Platforms
- Choose from 6 supported sources
- For each platform, UI allows custom input (e.g., subreddits for Reddit)

### Step 3: Collect Data
- Use scrapers to fetch recent data related to themes
- Save into `data/content_data.db`

### Step 4: Analyze Trends
- Extract keywords (TF-IDF), sentiment, clusters
- Visualize in Streamlit

### Step 5: Generate Article Topics
- From analyzed keywords, use LLM to suggest article titles and short descriptions

### Step 6: Generate Briefs
- For each selected topic, generate a structured content brief

### Step 7: Draft Long-form Content
- Create detailed articles from briefs using LLM agents

### Step 8: Polish Content
- Improve clarity, tone, SEO optimization

### Step 9: Export Final Output
- Download or copy final articles in `.docx`, `.md`, or formatted email

---

## 📂 Folder Structure

```bash
content-marketing-agent/
│
├── data/
│   └── content_data.db                  # SQLite DB storing scraped content
│
├── notebooks/
│   ├── 01_data_collection.ipynb         # Test and debug scraping flow
│   ├── 02_content_analysis.ipynb        # Visualizations and sentiment
│   ├── 03_ai_agent_core.ipynb           # LLM topic/brief/content generation
│   └── 04_ui_planning.ipynb             # UI and interaction logic drafts
│
├── src/
│   ├── scrapers/
│   │   ├── google_search_scraper.py
│   │   ├── reddit_scraper.py
│   │   ├── hackernews_scraper.py
│   │   ├── news_scraper.py
│   │   ├── rss_scraper.py
│   │   └── youtube_scraper.py
│   │
│   ├── data_collection/
│   │   └── collect_data.py              # Master data collector calling all scrapers
│   │
│   ├── database/
│   │   └── db_manager.py                # Functions to interact with SQLite
│   │
│   ├── analyzers/
│   │   ├── trend_sentiment_analyzer.py  # Keyword, sentiment, cluster logic
│   │   └── trend_viz.py                 # Wordclouds and charts
│   │
│   ├── agents/
│   │   ├── topic_generator.py           # LLM-powered topic suggestions
│   │   ├── brief_writer.py              # Generates briefs from topics
│   │   ├── content_drafter.py           # Writes articles from briefs
│   │   └── content_polisher.py          # Final cleanup and tone correction
│   │
│   ├── utils/
│   │   ├── text_cleaning.py             # Text pre-processing helpers
│   │   └── exporter.py                  # Word/Markdown/email output
│   │
│   └── app/
│       └── ui.py                        # Main Streamlit frontend
│
├── .env                                 # Store OPENAI_API_KEY
├── requirements.txt
└── README.md
````

---

## ⚙️ Setup Instructions

### 1. Clone and Setup

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

Create a `.env` file in root:

```
OPENAI_API_KEY=your-openai-api-key
```

---

## 🎨 UI Tabs (Planned in Streamlit)

| Tab # | Page             | Description                     |
| ----- | ---------------- | ------------------------------- |
| 1     | Define Themes    | Enter marketing themes          |
| 2     | Select Platforms | Choose scraping platforms       |
| 3     | Analyze Trends   | Visualizations + insights       |
| 4     | Generate Topics  | LLM topic generator             |
| 5     | Write Briefs     | LLM brief generator             |
| 6     | Draft Content    | Full article drafts             |
| 7     | Polish Content   | Fix tone and structure          |
| 8     | Export           | Export content to file or email |

---

## 🧪 Sample: Analyze Trends in Jupyter

```python
from src.analyzers.trend_sentiment_analyzer import analyze_trends_and_sentiment

df, embeddings = analyze_trends_and_sentiment()
df.head()
```

---

## 📊 Scrapers Summary

| Platform    | Script                     | Notes                 |
| ----------- | -------------------------- | --------------------- |
| Google      | `google_search_scraper.py` | SERP or BeautifulSoup |
| Reddit      | `reddit_scraper.py`        | Requires subreddits   |
| Hacker News | `hackernews_scraper.py`    | Scrapes top posts     |
| RSS         | `rss_scraper.py`           | Feedparser-based      |
| YouTube     | `youtube_scraper.py`       | Metadata scraping     |
| News        | `news_scraper.py`          | Uses News API         |

---

## 🧠 Tech Stack

* **Python 3.9**
* **Streamlit** – interactive UI
* **LangChain / OpenAI** – LLM agents
* **SQLite** – lightweight persistent DB
* **BeautifulSoup / feedparser / requests**
* **scikit-learn, NLTK, spaCy** – analysis
* **Matplotlib, WordCloud** – visuals

---

## 🔧 Roadmap

* [ ] Implement tabbed Streamlit UI
* [ ] Complete trend analyzer visualizations
* [ ] Add email & export capability
* [ ] Add user profiling & history saving (optional)

---

## 👤 Maintainer

**Vinoth Haldorai**
Connect on LinkedIn | GitHub |

---

## 📜 License

MIT License – free for personal and commercial use.

```

---

