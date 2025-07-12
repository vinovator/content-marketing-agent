# src/analyzers/trend_sentiment_analyser.py

import os
import sqlite3
import string
from collections import Counter
from pathlib import Path
from typing import Tuple, List, Dict

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF, PCA
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from sentence_transformers import SentenceTransformer

# --- Setup ---
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("vader_lexicon", quiet=True)

stop_words = set(stopwords.words("english"))
sentiment_analyzer = SentimentIntensityAnalyzer()


# === Step 1: Load Data ===
def load_content_data() -> pd.DataFrame:
    root = Path(__file__).resolve().parents[2]
    db_path = root / "data" / "content_data.db"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM content", conn)
    conn.close()

    df["publishedAt"] = pd.to_datetime(df["publishedAt"], utc=True)
    return df


# === Step 2: Clean Text ===
def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)


# === Step 3: TF-IDF Vectorization ===
def vectorize_text(text_series: pd.Series, max_features: int = 100) -> Tuple[pd.DataFrame, TfidfVectorizer]:
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(text_series)
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    return tfidf_df, vectorizer


# === Step 4: Topic Modeling ===
def extract_topics(tfidf_matrix, vectorizer, n_topics: int = 5) -> List[List[str]]:
    nmf = NMF(n_components=n_topics, random_state=42)
    nmf.fit(tfidf_matrix)
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic in nmf.components_:
        top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
        topics.append(top_words)
    return topics


# === Step 5: Extract Keywords Per Title ===
def extract_keywords(tfidf_df: pd.DataFrame, vectorizer, top_n: int = 3) -> List[List[str]]:
    feature_names = vectorizer.get_feature_names_out()
    keywords_per_title = []

    for row in tfidf_df.values:   # ✅ fixed here
        sorted_indices = row.argsort()[::-1][:top_n]
        keywords = [feature_names[i] for i in sorted_indices]
        keywords_per_title.append(keywords)

    return keywords_per_title


# === Step 6: Sentiment Analysis ===
def get_sentiment_label(score: float) -> str:
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"


def compute_sentiment_scores(df: pd.DataFrame) -> pd.DataFrame:
    df["sentiment_score"] = df["title"].apply(lambda x: sentiment_analyzer.polarity_scores(x)["compound"])
    df["sentiment_label"] = df["sentiment_score"].apply(get_sentiment_label)
    return df


# === Step 7: Semantic Clustering ===
def cluster_titles(df: pd.DataFrame, n_clusters: int = 5) -> Tuple[pd.DataFrame, List[int]]:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(df["title"].tolist(), show_progress_bar=False)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = kmeans.fit_predict(embeddings)
    return df, embeddings


# === Master Function ===
def analyze_trends_and_sentiment() -> pd.DataFrame:
    df = load_content_data()
    df["clean_title"] = df["title"].apply(clean_text)

    tfidf_df, vectorizer = vectorize_text(df["clean_title"])
    topics = extract_topics(tfidf_df.values, vectorizer)
    keywords = extract_keywords(tfidf_df, vectorizer)

    df["top_keywords"] = keywords
    df = compute_sentiment_scores(df)
    df, embeddings = cluster_titles(df)

    # Reduce dimensions for plotting (PCA)
    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embeddings)

    return df, reduced_embeddings # Enhanced DataFrame