import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

def plot_sentiment_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="sentiment_label", palette="coolwarm")
    plt.title("Sentiment Distribution of Content Titles", fontsize=14)
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.show()

def plot_top_keywords(df, top_n=15):
    all_keywords = [keyword for sublist in df["top_keywords"] for keyword in sublist]
    keyword_counts = Counter(all_keywords)
    top_keywords = keyword_counts.most_common(top_n)
    keywords, counts = zip(*top_keywords)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(counts), y=list(keywords), palette="Blues_d")
    plt.title("Top Keywords from Titles")
    plt.xlabel("Frequency")
    plt.ylabel("Keyword")
    plt.tight_layout()
    plt.show()

def plot_wordcloud(df):
    all_keywords = [keyword for sublist in df["top_keywords"] for keyword in sublist]
    keyword_counts = Counter(all_keywords)

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(keyword_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Keyword Word Cloud", fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_clusters(df, reduced_embeddings):
    plt.figure(figsize=(8, 6))
    plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=df["cluster"], cmap="tab10", s=30)
    plt.title("Title Clusters (PCA Projection)")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.tight_layout()
    plt.show()
