import requests
import pandas as pd

def fetch_top_hackernews_posts(limit: int = 10):
    """
    Fetch top Hacker News posts using the public API.

    Args:
        limit (int): Number of posts to fetch (max 500)

    Returns:
        List[Dict]: List of post dictionaries with title, url, and publishedAt
    """
    
    base = "https://hacker-news.firebaseio.com/v0"
    headers = {"User-Agent": "ContentMarketingAgent/0.1"}
    
    response = requests.get(f"{base}/topstories.json", headers=headers)
    top_stories = response.json()[:limit]

    stories = []

    for story_id in top_stories:
        story = requests.get(f"{base}/item/{story_id}.json").json()

        if story and "title" in story:
            published_at = pd.to_datetime(story.get("time", 0), unit="s", utc=True)
            stories.append(
                {
                    "title": story["title"],
                    "score:": story.get("score", 0),
                    "url": story.get("url", ""),
                    "publishedAt": published_at.floor("s"), #drop micro-seconds
                    "source": "Hacker News"
                }
            )

    return pd.DataFrame(stories)