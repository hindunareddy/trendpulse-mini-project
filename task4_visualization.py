import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/cleaned_trends.csv")

# 1. Category distribution (bar chart)
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# 2. Top 5 stories by score
top_stories = df.sort_values(by="score", ascending=False).head(5)

plt.figure()
plt.bar(top_stories["title"], top_stories["score"])
plt.title("Top 5 Stories by Score")
plt.xticks(rotation=45)
plt.ylabel("Score")
plt.show()