import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import emoji
import os
import squarify
df= pd.read_csv("Us_comments.csv", on_bad_lines="skip", sep="\t")
print(df.head(5))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.duplicated())
print(df.info())
print(df.describe())
print(df.nunique())
print(df["comment_text"].unique()[:10])
df.dropna()
print(df.isnull().sum())
df = df.dropna(subset=["comment_text"])
df["comment_text"] = df["comment_text"].astype(str)

print(df["video_id"].value_counts())
print(df["video_id"].value_counts().head(5))

sia = SentimentIntensityAnalyzer()

def compound_analyzer(comment):

    compound = sia.polarity_scores(comment)["compound"]

    if compound > 0.05:
        label = "positive 😊"

    elif compound < -0.05:
        label = "negative 😞"

    else:
        label = "neutral 😐"

    return {
        "label": label,
        "score": compound
    }

result = compound_analyzer("This video is amazing and very helpful")

print(result)

print(df["comment_text"].isnull().sum())
print(df["comment_text"].apply(type).value_counts())

comment = "This video is amazing 😍🔥"

emoji_list = []

for char in comment:
    if char in emoji.EMOJI_DATA:
        emoji_list.append(char)

print(emoji_list)

all_emojis_list = []

for comment in df["comment_text"].dropna():
    for char in str(comment):
        if char in emoji.EMOJI_DATA:
            all_emojis_list.append(char)

print(all_emojis_list[:10])

emojis_count = Counter(all_emojis_list).most_common(10)
print(emojis_count)

for emoji, count in emojis_count:
    print(emoji, count)

emojis = [emoji for emoji, count in emojis_count]
counts = [count for emoji, count in emojis_count]
plt.bar(emojis, counts)
plt.xlabel("emojis")
plt.ylabel("counts")
plt.xticks(rotation=45)
plt.title("most used emojis in youtube comments")
plt.savefig("visuals/most used emojis.png")
plt.show()

import warnings
from warnings import filterwarnings
filterwarnings("ignore")

path= ( r"C:\Users\admin\Downloads\additional_data-20260913T063118Z-1-001\additional_data")
files_csv = os.listdir(path)
full_df= pd.DataFrame()
for file in files_csv:
    df = pd.read_csv(
        path + "/" + file,
        encoding="ISO-8859-1",
        on_bad_lines="skip"
    )
    full_df = pd.concat([full_df, df], ignore_index=True)
full_df["trending_date"] = pd.to_datetime(
    full_df["trending_date"],
    format="%y.%d.%m",
    errors="coerce"
)
print(full_df["trending_date"].dtype)
print(full_df["trending_date"].isnull().sum())
full_df = full_df.dropna(subset=["trending_date"])
print(full_df["trending_date"].isnull().sum())
print(full_df["trending_date"].dtype)
print(full_df["trending_date"].head(5))
import json
path = r"C:\Users\admin\Downloads\additional_data-20260913T063118Z-1-001\additional_data\US_category_id.json"
with open(path, "r", encoding="utf-8") as f:
     data = json.load(f)
print(data)
print(data["items"][0]['snippet'] ["title"])
dict_items = {}

for item in data["items"]:
    dict_items[int(item["id"])] = item["snippet"]["title"]

print(dict_items)
full_df["category_name"] = full_df["category_id"].map(dict_items)
result= full_df.groupby(["trending_date", "category_name"])["views"].sum().unstack()
plt.figure(figsize=(12, 6))

result.plot.area()

plt.xlabel("Trending Date")
plt.ylabel("Total Views")
plt.title("Total Views by Category Over Time")
plt.legend(title="Category")
plt.savefig("visuals/totalviews by category")
plt.show()

top5_category = full_df.groupby("category_name")["views"].sum().nlargest(5)
plt.bar(top5_category.index, top5_category.values)
plt.xlabel("Category_Name")
plt.ylabel("Total views")
plt.title("Top 5 Categories by Total Views")
plt.xticks(rotation=45)
plt.savefig("visuals/total views by category.png")
plt.show()

full_df["engagement_rate"] = (
    (full_df["likes"] + full_df["comment_count"])
    / full_df["views"].replace(0, np.nan)
) * 100
plt.scatter(full_df["views"], full_df["engagement_rate"])
plt.xlabel("Views")
plt.ylabel("Engagement Rate")
plt.title("Views vs Engagement Rate")
plt.savefig("visuals/engagment rate.png")
plt.show()


category_engagement = full_df.groupby("category_name")["engagement_rate"].mean()
category_engagement = category_engagement.sort_values(ascending=False)
plt.bar(category_engagement.index, category_engagement.values)
plt.xlabel("Category Name")
plt.ylabel("Average engagement rate")
plt.title("Average Engagement Rate by Category")
plt.savefig("visuals/avg engagement rate")
plt.show()

full_df["engagement_rate"].describe()

category_views= full_df.groupby("category_name")["views"].sum()
category_views= category_views.sort_values(ascending=False)
squarify.plot(
    sizes=category_views.values,
    label=category_views.index,
    alpha=0.8
)
plt.title("Total Views by Category")
plt.axis("off")
plt.savefig("visuals/category_treemap.png")
plt.show()

result = full_df.groupby("category_name")["engagement_rate"].describe()
print(result)

plt.boxplot(full_df["views"].dropna())
plt.ylabel("Views")
plt.title("Distribution of Views")
plt.savefig("visuals/distribution_of_views.png")
plt.show()