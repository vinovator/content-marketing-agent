# src/scrapers/reddit_scraper.py

import os
from dotenv import load_dotenv
import praw
from typing import List, Dict
import pandas as pd

# Load Reddit credentials
load_dotenv()
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "content-marketing-assistant")

# Cache the PRAW client so it is created only once, on first use.
_reddit_client = None


def get_reddit_client() -> praw.Reddit:
    """
    Lazily create and cache the PRAW Reddit client.

    The client is built on first use rather than at import time, so a missing
    or misconfigured credential set (e.g. no .env on Streamlit Cloud) fails only
    when Reddit is actually scraped instead of crashing the whole app on import.
    """
    global _reddit_client
    if _reddit_client is None:
        if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
            raise RuntimeError(
                "Reddit credentials are not configured. Set REDDIT_CLIENT_ID, "
                "REDDIT_CLIENT_SECRET and REDDIT_USER_AGENT (via .env locally or "
                "the Streamlit Cloud secrets manager)."
            )
        _reddit_client = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
        )
    return _reddit_client


def fetch_reddit_posts(subreddit: str, query: str, max_results: int = 10) -> List[Dict]:
    """
    Fetch Reddit posts from a subreddit matching the given query.

    Args:
        subreddit_name (str): Name of the subreddit (e.g. 'marketing')
        query (str): Search query term
        limit (int): Number of posts to fetch

    Returns:
        List[Dict]: List of post metadata
    """
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit)
    posts = []

    for submission in subreddit.search(query, limit=max_results, sort="relevance"):
        created_at = pd.to_datetime((submission.created_utc), unit="s", utc=True)
        posts.append({
            "title": submission.title,
            "score": submission.score,
            "url": submission.url,
            "publishedAt": created_at,
            "num_comments": submission.num_comments,
            "permalink": f"https://reddit.com{submission.permalink}",
            "source": "Reddit"
        })

    return pd.DataFrame(posts)
