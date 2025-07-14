# src/scrapers/rss_scraper.py

import feedparser
import pandas as pd
from bs4 import BeautifulSoup

def fetch_rss_articles(feed_urls, max_results: int = 10) -> pd.DataFrame:
    """
    Fetch articles from a list of RSS feed URLs.

    Args:
        feed_urls (List[str]): List of RSS feed URLs
        limit (int): Max number of articles per feed

    Returns:
        pd.DataFrame: Articles with title, url, publishedAt, and source
    """

    for url in feed_urls:
        feed = feedparser.parse(url)
        source_name = feed.feed.get("title", "RSS")

    articles = []

    for entry in feed.entries[:max_results]:

        published_at = pd.to_datetime(entry.get("published", ""), errors="coerce", utc=True)        
        articles.append(
            {
                "title": entry.get("title", "No Title"),
                "url": entry.get("link", ""),
                "publishedAt": published_at.floor("s"), # drop micro-seconds
                "summary": BeautifulSoup(entry.get("summary", ""), "html.parser").get_text(),
                "source": "RSS"
            }
        )

    return pd.DataFrame(articles)