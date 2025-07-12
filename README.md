Content Marketing Assistant AI Agent

This project is an AI-powered agent that automates content marketing tasks like:
- Collecting news & trend data from Reddit, Hacker News, YouTube, NewsAPI, RSS, Google
- Analyzing text using NLP (NLTK, TF-IDF)
- Visualizing trends
- Generating content insights

Technologies Used
- Python, Pandas, NLTK, Scikit-learn, Matplotlib, SQLite

This project builds an AI agent that automates the full content marketing workflow:
- Collect trend and news data from multiple sources → Step 2
- Analyze keywords, sentiment, gaps → Step 3
- Generate topics from real-world content → Step 4.1: Topic Generator Agent
- Write briefs for those topics → Step 4.2: Brief Writer Agent
- Content drafting based on the brief. → Step 4.3 Content Drafting Agent
- Content polishing to improve tone and consistency → Step 4.4 Content Polisher Agent
- Data collection pipeline → Step 5
- Trend Analysis and Sentiment scoring - Trend Frequency, Sentiment → Step 6
- Feed enriched data in to AI Agent → Step 7
- Finalise the UI → Step 8
- Export, Save and notify → Step 9


# 🧠 Content Marketing Assistant (CMA)

A smart, AI-powered content ideation and generation assistant built to help marketing teams discover trending topics, generate structured content briefs, and produce high-quality drafts — all driven by real-world platform signals.

---

## 🚀 Purpose

The Content Marketing Assistant combines **real-time topic intelligence** with **generative AI** to automate and optimize the content creation workflow for marketers, strategists, and content teams.

This tool goes beyond prompt engineering. It enables:

- 🚨 **Trend mining** from Reddit, Hacker News, Google Search, YouTube, News APIs, and RSS feeds  
- 🧠 **AI-driven content ideation** grounded in real-world insights  
- 🧾 **Structured brief creation** with target audience, tone, outline, and CTA  
- ✍️ **Full content drafts** for blogs, newsletters, or thought leadership  
- 📈 (Planned) integration of analytics and performance feedback loops  

---

## 💡 What Makes It Unique?

Unlike generic AI writers, CMA:
- Starts with **real platform signals** (not random keywords)
- Analyzes content trends and sentiment from **6+ platforms**
- Generates **structured marketing briefs**
- Drafts **ready-to-publish content**
- Will evolve to integrate performance learning, internal linking, and SEO guidance

---

## 🧱 System Architecture

```

User Input
|
v
Platform Select + Query Input (UI)
|
v
🗞️ Data Collection (Reddit, Hacker News, RSS, Google, YouTube, News)
|
v
🧪 Preprocessing + Sentiment + Deduplication
|
v
🧠 Insight-Driven Content Agent
├── Topic Generator
├── Brief Generator
└── Draft Generator
|
v
🧾 Review + Edit + Export (Planned UI)

```

---

## 🧩 Current Modules

### 1. `src/scrapers/`
Web scraping + API ingestion for:
- `reddit_scraper.py`
- `hackernews_scraper.py`
- `rss_scraper.py`
- `google_search_scraper.py`
- `youtube_scraper.py`
- `news_api_scraper.py`

### 2. `src/data_collection/`
- `collect_data.py`: Aggregates, normalizes, and consolidates signals from all scrapers

### 3. `src/agents/`
- `topic_generator.py`: Generates trending topic ideas from content signals
- `brief_writer.py`: Converts topics into structured briefs
- `content_drafter.py`: Generates draft articles from briefs

---

## 🔧 How It Works

1. **User** selects platforms and enters optional keywords
2. **System** scrapes and aggregates data across platforms
3. **LLM Agents**:
   - Generate topics grounded in extracted trends
   - Convert them into structured briefs
   - Draft content using brief context
4. **Draft** is displayed for review/export (UI coming soon)

---

## 🔜 Planned Features

- ✅ SEO Optimizer & Internal Linking Assistant  
- ✅ Scheduled publishing (e.g. Ghost, Medium, WordPress)
- 📊 Engagement Feedback Loop
- 📎 Chrome Extension
- 🗂️ CMS Integration

---

## 📁 Folder Structure (Simplified)

```

content-marketing-agent/
│
├── src/
│   ├── agents/
│   ├── scrapers/
│   └── data\_collection/
│
├── assets/
│   └── mockups/           # UI Wireframes & Diagrams
│
├── .env                   # API keys
├── requirements.txt
└── README.md

```

---

## 🔐 Environment Variables (.env)

You will need:

```

OPENAI\_API\_KEY=your\_key\_here

# Reddit

REDDIT\_CLIENT\_ID=your\_id
REDDIT\_CLIENT\_SECRET=your\_secret
REDDIT\_USER\_AGENT=your\_app\_name

# Google

GOOGLE\_API\_KEY=your\_key
GOOGLE\_CSE\_ID=your\_custom\_search\_engine\_id

# YouTube

YOUTUBE\_API\_KEY=your\_key

# NewsAPI

NEWS\_API\_KEY=your\_key

````

---

## 👨‍💻 How to Run (Basic)

```bash
# Install dependencies
pip install -r requirements.txt

# Run topic + brief + draft pipeline
python src/run_pipeline.py  # (Coming soon)

# Or run individual components in notebooks or scripts
````

---

