# src/data_collection/collect_data.py

import os
import sys
import pandas as pd
import sqlite3
from typing import List, Dict

# Ensure the scrapers folder is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import scraper functions
from scrapers.reddit_scraper import fetch_reddit_posts
from scrapers.hackernews_scraper import fetch_top_hackernews_posts
from scrapers.rss_scraper import fetch_rss_articles
from scrapers.google_search_scraper import fetch_google_search_results
from scrapers.youtube_scraper import fetch_youtube_videos
from scrapers.news_scraper import fetch_news_articles

def collect_data(themes: List[str], platform_selections: Dict, max_results: int = 10) -> pd.DataFrame:
    """
    Collect data based on user-selected platforms and input values.
    Args:
        themes (List[str]): List of themes selected by the user.
        platform_selections (Dict): Platform-specific input info from session state.
        max_results (int): Max number of results per scraper.
    Returns:
        pd.DataFrame: Combined cleaned DataFrame with columns: title, url, publishedAt, source
    """

    dfs = []

    for platform, config in platform_selections.items():
        input_type = config["type"]
        values = config["value"]

        # Use themes if input_type is "theme"
        queries = themes if input_type == "theme" else values

        if platform == "Reddit":
            for subreddit in queries:
                for theme in themes:
                    print(f"Fetching Reddit posts from r/{subreddit} on '{theme}'...")
                    df = pd.DataFrame(fetch_reddit_posts(subreddit=subreddit, query=theme, max_results=max_results))
                    dfs.append(df)

        elif platform == "Hacker News":
            print("Fetching HackerNews posts...")
            df = pd.DataFrame(fetch_top_hackernews_posts(max_results=max_results))
            dfs.append(df)

        elif platform == "Google News":
            for theme in queries:
                print(f"Fetching Google News for theme '{theme}'...")
                df = pd.DataFrame(fetch_google_search_results(query=theme, max_results=max_results))
                dfs.append(df)

        elif platform == "YouTube":
            for query in queries:
                print(f"Fetching YouTube results for '{query}'...")
                df = pd.DataFrame(fetch_youtube_videos(query=query, max_results=max_results))
                dfs.append(df)

        elif platform == "RSS Feeds":
            for rss_url in queries:
                print(f"Fetching RSS articles from {rss_url}...")
                df = pd.DataFrame(fetch_rss_articles([rss_url], max_results=max_results))
                dfs.append(df)

        elif platform == "Web Search":
            for theme in queries:
                print(f"Fetching Web search results for '{theme}'...")
                df = pd.DataFrame(fetch_news_articles(query=theme, max_results=max_results))
                dfs.append(df)

        else:
            print(f"⚠️ Unknown platform: {platform}. Skipping.")

    # Combine all and drop duplicates/nulls
    if not dfs:
        return pd.DataFrame(columns=["title", "url", "publishedAt", "source"])

    all_df = pd.concat(dfs, ignore_index=True)
    all_df = all_df.dropna(subset=["title", "url"]).drop_duplicates(subset=["title", "url"])
    all_df = all_df[["title", "url", "publishedAt", "source"]]  # standard format

    # Save to SQLite-compatible CSV for analysis
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    os.makedirs(os.path.join(root, "data"), exist_ok=True)

    # Save to SCV
    output_path = os.path.join(root, "data", "combined_data.csv")
    all_df.to_csv(output_path, index=False)

    #Save to SQLite database
    sqlite_path = os.path.join(root, "data", "content_data.db")
    #Connect to (or create) SQLite database
    conn = sqlite3.connect(sqlite_path)

    # Export to table name "content"
    all_df.to_sql("content", conn, if_exists="replace", index=False)

    # Close the connection
    conn.close()

    return all_df