# src/scrapers/news_scraper.py

import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API key
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news_articles(query: str, max_results: int = 10):
    """
    Fetch news articles matching the query using NewsAPI.

    Args:
        query (str): Search term
        max_results (int): Number of articles to return

    Returns:
        pd.DataFrame: DataFrame with title, url, publishedAt, and source
    """

    url = "https://newsapi.org/v2/everything"
    
    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": max_results
    }

    results = []

    response = requests.get(url, params=params)

    articles = response.json().get("articles", [])

    for article in articles:
        published_at = pd.to_datetime(article.get("publishedAt", ""), errors="coerce", utc=True)
        
        results.append(
            {
                "title": article.get("title", ""),
                "articleSource": article.get("source", {}).get("name", ""),
                "url": article.get("url", ""),
                "publishedAt": published_at.floor("s"), # drop micro-seconds
                "source": "NewsAPI"
            }
        )

    return pd.DataFrame(results)