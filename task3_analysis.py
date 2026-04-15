import pandas as pd

# Step 1: Load cleaned CSV
df = pd.read_csv("data/cleaned_trends.csv")

print("Total records:", len(df))

# Step 2: Average score
avg_score = df["score"].mean()
print("Average Score:", avg_score)

# Step 3: Total comments
total_comments = df["num_comments"].sum()
print("Total Comments:", total_comments)

# Step 4: Top 5 stories by score
top_stories = df.sort_values(by="score", ascending=False).head(5)

print("\nTop 5 Stories:")
print(top_stories[["title", "score"]])

# Step 5: Category-wise count
category_count = df["category"].value_counts()

print("\nStories per Category:")
print(category_count)