import json
import pandas as pd
import os

# Step 1: Get latest JSON file from data folder
folder = "data"
files = os.listdir(folder)
files.sort()

latest_file = files[-1]
file_path = os.path.join(folder, latest_file)

# Step 2: Load JSON data
with open(file_path, "r") as f:
    data = json.load(f)

print("Loaded", len(data), "records")

# Step 3: Convert to DataFrame
df = pd.DataFrame(data)

# Step 4: Clean Data

# Remove duplicate posts
df = df.drop_duplicates(subset="post_id")

# Fill missing values
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

# Clean title (remove extra spaces)
df["title"] = df["title"].str.strip()

# Remove empty titles
df = df[df["title"] != ""]

print("After cleaning:", len(df))

# Step 5: Save cleaned CSV
output_file = "data/cleaned_trends.csv"

df.to_csv(output_file, index=False)

print("✅ Clean CSV saved at:", output_file)