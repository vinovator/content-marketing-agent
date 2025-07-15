# 🚀 Content Marketing Agent

**Automate your entire content marketing pipeline** — from market research to polished articles — in one unified app.

> **Features:**
> ✅ Multi-platform data collection  
> ✅ Trend & sentiment analysis  
> ✅ AI-driven topic generation  
> ✅ Brief & content drafting  
> ✅ Content polishing  
> ✅ Export to multiple formats  
> ✅ Interactive Streamlit UI

---

## 📚 Project Overview

The Content Marketing Agent scrapes trending content from various platforms, analyzes it for topics and sentiment, and uses AI agents to:

- Propose new article topics
- Write content briefs
- Draft full articles
- Polish final drafts
- Export your work in Markdown, PDF, or text formats

Designed for content marketers, strategists, and SEO professionals who want **data-driven ideas and rapid content production.**

---

## 🎯 Workflow

Below is the **step-by-step workflow** as implemented in the UI:

### 1. Define Themes
- User inputs **broad themes** for research.
- E.g. `"AI Agents"`, `"Sustainable Marketing"`.

### 2. Select Platforms
- Pick from:
  - Google News
  - Reddit
  - Hacker News
  - YouTube
  - RSS Feeds
  - Web Search
- Enter platform-specific inputs (e.g. subreddits).

### 3. Collect & Analyze Trends
- Scrape content across selected platforms.
- Perform:
  - Text cleaning
  - TF-IDF vectorization
  - Topic modeling
  - Sentiment scoring
  - Clustering
- Visualize trends and keywords.

### 4. Generate Topics
- Generate 5 unique article topics:
  - Title
  - Short description
- User can select topics for content creation.

### 5. Write Briefs
- Create detailed content briefs:
  - Title
  - Description
  - Outline
  - Tone
  - Audience
  - Call-to-Action (CTA)

### 6. Draft Content
- Generate full article drafts from briefs.

### 7. Polish Content
- Refine drafts for:
  - Style and tone
  - Grammar
  - Readability

### 8. Export
- Download articles as:
  - **Markdown (.md)**
  - **PDF (.pdf)**
  - **Plain text (.txt)**

---

## 🗄️ Project Structure

```

content-marketing-agent/
│
├── data/
│   ├── combined\_data.csv
│   └── content\_data.db
│
├── guides/
│   ├── content-marketing-agent-notes.md
│   ├── google-api-setup-guide.md
│   ├── TECH\_DEBT.md
│   └── ui-planning-guide.md
│
├── src/
│   ├── app/
│   │   ├── ui.py
│   │   └── tabs/
│   │       ├── themes\_tab.py
│   │       ├── platforms\_tab.py
│   │       ├── analyze\_tab.py
│   │       ├── topics\_tab.py
│   │       ├── briefs\_tab.py
│   │       ├── draft\_tab.py
│   │       ├── polish\_tab.py
│   │       └── export\_tab.py
│   │
│   ├── analyzers/
│   │   ├── trend\_sentiment\_analyzer.py
│   │   └── trend\_viz.py
│   │
│   ├── agents/
│   │   ├── topic\_generator.py
│   │   ├── brief\_writer.py
│   │   ├── content\_drafter.py
│   │   └── content\_polisher.py
│   │
│   ├── scrapers/
│   │   ├── reddit\_scraper.py
│   │   ├── google\_search\_scraper.py
│   │   ├── youtube\_scraper.py
│   │   ├── hackernews\_scraper.py
│   │   ├── news\_scraper.py
│   │   └── rss\_scraper.py
│   │
│   ├── data\_collection/
│   │   └── collect\_data.py
│   │
│   ├── database/          # Currently empty - future DB helpers
│   └── utils/             # Currently empty - future utility functions
│
└── requirements.txt

````

---

## ✅ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/content-marketing-agent.git
cd content-marketing-agent
````

### 2. Set up your Python environment

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root with:

```
OPENAI_API_KEY=your_api_key_here
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_app_name
YOUTUBE_API_KEY=your_key
GOOGLE_API_KEY=your_key
GOOGLE_CSE_ID=your_cse_id
NEWS_API_KEY=your_key
```

Refer to:

* `guides/google-api-setup-guide.md`

---

## ▶️ Running the App

```bash
streamlit run src/app/ui.py
```

Your browser will open the Content Marketing Agent UI.

---

## 📦 Requirements

See:

* `requirements.txt`

---

## ⚠️ Technical Debt & Future Improvements

Tracked in:

* `guides/TECH_DEBT.md`

Highlights:

* Add exception handling in scrapers
* Refactor repeated navigation logic
* Implement testing
* Add logging

---

## 💡 Contributing

Contributions are welcome!

* Raise issues
* Suggest features
* Improve scrapers for new platforms

---

## License

[MIT License](LICENSE)
