import os
import requests
import pandas as pd
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def fetch_google_search_results(query: str, num_results: int = 10):
    """
    Fetch top search results for a given query using Google CSE API.

    Args:
        query (str): Search term
        num_results (int): Number of results (max 10 per API call)

    Returns:
        pd.DataFrame: Results with title, url, snippet, and source
    """

    url = f"https://www.googleapis.com/customsearch/v1"
    
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results
    }

    results = []
    
    response = requests.get(url, params=params)
    items = response.json()

    now = pd.to_datetime(datetime.now(timezone.utc)).floor("s")
    
    results = []
    for item in items.get("items", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("link"),
            "snippet": item.get("snippet", ""),
            'publishedAt': now,  # fallback (Google doesn’t return pub date),
            "source": "Google Search"
        })

    return pd.DataFrame(results)