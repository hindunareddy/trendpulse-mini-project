import requests
import json
import os
from datetime import datetime

# Step 1: Get top 500 story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = requests.get(url).json()[:500]

# Step 2: Define categories
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

# Function to assign category
def get_category(title):
    title = title.lower()
    for cat, keywords in categories.items():
        for word in keywords:
            if word.lower() in title:
                return cat
    return None

# Function to fetch story safely
def get_story(id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    headers = {"User-Agent": "TrendPulse/1.0"}
    try:
        res = requests.get(url, headers=headers)
        return res.json()
    except:
        return None

# Step 3: Collect data
results = []
category_count = {cat: 0 for cat in categories}

for id in story_ids:
    print("Processing ID:", id)   

    story = get_story(id)
    story = get_story(id)

    # Skip invalid data
    if not story or "title" not in story:
        continue

    category = get_category(story["title"])

    # Skip if no category
    if category is None:
        continue

    # Limit 25 per category
    if category_count[category] >= 25:
        continue

    data = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    results.append(data)
    category_count[category] += 1

    # Stop when all categories filled
    if all(count >= 25 for count in category_count.values()):
        break

# Step 4: Save to JSON file
if not os.path.exists("data"):
    os.mkdir("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(results, f, indent=4)

print(f"✅ Collected {len(results)} stories. Saved to {filename}")