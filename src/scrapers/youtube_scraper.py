# src/scrapers/youtube_scraper.py

import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_youtube_videos(query: str, max_results: int = 10):
    """
    Search YouTube for videos matching the query.
    Use the YouTube Data API v3 to search for videos related to a keyword or topic, and return structured metadata (title, URL, published date, etc.) in a DataFrame.

    Args:
        query (str): Search term
        max_results (int): Number of results to fetch

    Returns:
        pd.DataFrame: DataFrame with title, url, publishedAt, and source
    """

    url = f"https://www.googleapis.com/youtube/v3/search"
    
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': max_results
    }

    videos = []

    response = requests.get(url, params=params)
    items = response.json().get("items", [])
    
    for item in items:
        published_at = pd.to_datetime(item["snippet"]["publishedAt"], errors="coerce", utc=True)
        videos.append(
            {
                "title": item["snippet"]["title"],
                "channel": item["snippet"]["channelTitle"],
                "url": f"https://youtube.com/watch?v={item['id']['videoId']}", 
                "publishedAt": published_at.floor("s"), # drop micro-seconds
                "source": "YouTube"
            }        
        )

    return pd.DataFrame(videos)