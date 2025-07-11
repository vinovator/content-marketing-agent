# src/data_collection/collect_data.py

import os
import sys
import pandas as pd

# Ensure the scrapers folder is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import scraper functions
from scrapers.reddit_scraper import fetch_reddit_posts
from scrapers.hackernews_scraper import fetch_top_hackernews_posts
from scrapers.rss_scraper import fetch_rss_articles
from scrapers.google_search_scraper import fetch_google_search_results
from scrapers.youtube_scraper import fetch_youtube_videos
from scrapers.news_scraper import fetch_news_articles

def collect_all_data(
    keyword: str,
    subreddit: str = "marketing",
    rss_feeds: list = [],
    max_results: int = 10
) -> pd.DataFrame:
    """
    Collect content from all sources and return a single combined DataFrame.

    Args:
        keyword (str): Search keyword
        subreddit (str): Subreddit to use for Reddit scraper
        rss_feeds (list): List of RSS feed URLs
        max_results (int): Number of results per source

    Returns:
        pd.DataFrame: Combined content DataFrame
    """

    # Collect data from all sources
    print("Fetching Reddit posts...")
    reddit_df = pd.DataFrame(fetch_reddit_posts(subreddit, keyword, max_results))

    print("Fetching HackerNews posts...")
    hn_df = pd.DataFrame(fetch_top_hackernews_posts(max_results))

    print("Fetching RSS articles...")
    rss_df = pd.DataFrame(fetch_rss_articles(rss_feeds, max_results))

    print("Fetching Google search results...")
    google_df = pd.DataFrame(fetch_google_search_results(keyword, max_results))

    print("Fetching YouTube videos...")
    youtube_df = pd.DataFrame(fetch_youtube_videos(keyword, max_results))

    print("Fetching NewsAPI articles...")
    news_df = pd.DataFrame(fetch_news_articles(keyword, max_results))

    # Combine all
    all_df = pd.concat([reddit_df, hn_df, rss_df, google_df, youtube_df, news_df], ignore_index=True)
    return all_df[["title", "url", "publishedAt", "source"]]


if __name__ == "__main__":
    keyword = "AI in content marketing"
    rss_urls = [
        "https://moz.com/blog/rss",
        "https://feeds.feedburner.com/TechCrunch/"
    ]
    df = collect_all_data(keyword, subreddit="marketing", rss_feeds=rss_urls, max_results=5)
    print(df.head())