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

# Initialize PRAW Reddit client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_reddit_posts(subreddit_name: str, query: str, limit: int = 10) -> List[Dict]:
    """
    Fetch Reddit posts from a subreddit matching the given query.

    Args:
        subreddit_name (str): Name of the subreddit (e.g. 'marketing')
        query (str): Search query term
        limit (int): Number of posts to fetch

    Returns:
        List[Dict]: List of post metadata
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for submission in subreddit.search(query, limit=limit, sort="relevance"):
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
