import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import re

def duration_to_minutes(duration):
    pattern = r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?"
    match = re.match(pattern, duration)

    if not match:
        return None

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)

    total_minutes = hours * 60 +minutes + seconds / 60

    return total_minutes

connection = sqlite3.connect("data/videos.db")

query = """
SELECT COUNT(*) AS total_videos
FROM videos
"""

result = pd.read_sql_query(query, connection)

print("\nTOTAL VIDEOS")
print(result)

query = """
SELECT SUM(view_count) AS total_views
FROM videos
"""

result = pd.read_sql_query(query, connection)

print("\nTOTAL VIEWS")
print(result)


query = """
SELECT AVG(view_count) AS average_views
FROM videos
"""

result = pd.read_sql_query(query, connection)

print("\nAVERAGE VIEWS")
print(result)

query = """
SELECT
    title,
    view_count
FROM videos
ORDER BY view_count DESC
LIMIT 10
"""

top_videos = pd.read_sql_query(query, connection)

print("\nTOP 10 MOST VIEWED VIDEOS")
print(top_videos)

query = """
SELECT title, view_count
FROM videos
ORDER BY view_count DESC
"""

views_df = pd.read_sql_query(query, connection)

total_views = views_df["view_count"].sum()

views_df["cumulative_views"] = views_df["view_count"].cumsum()

views_df["cumulative_percentage"] = (
    views_df["cumulative_views"] / total_views
)

threshold_row = views_df[
    views_df["cumulative_percentage"] >= 0.80
].iloc[0]

videos_needed = threshold_row.name + 1

percentage_of_catalog = (
    videos_needed / len(views_df)
) * 100

print("\n80% OF TOTAL VIEWS")
print("Videos needed:", videos_needed)
print(
    "Percentage of catalog:",
    round(percentage_of_catalog, 2),
    "%"
)
# -----------------------------
# Cumulative view distribution graph
# -----------------------------

views_df["video_percentage"] = (
    (views_df.index + 1) / len(views_df)
) * 100

views_df["cumulative_view_percentage"] = (
    views_df["cumulative_views"] / total_views
) * 100

plt.figure(figsize=(10, 6))

plt.plot(
    views_df["video_percentage"],
    views_df["cumulative_view_percentage"]
)

plt.axhline(
    y=80,
    linestyle="--",
    label="80% of total views"
)

plt.axvline(
    x=percentage_of_catalog,
    linestyle="--",
    label=f"{percentage_of_catalog:.2f}% of videos"
)

plt.xlabel("Percentage of Videos")
plt.ylabel("Percentage of Total Views")
plt.title("Cumulative View Distribution - penguinz0")

plt.legend()
plt.grid()

plt.show()

query = """
SELECT published_at 
FROM videos
"""

upload_df = pd.read_sql_query(query, connection)

upload_df["published_at"] = pd.to_datetime(upload_df["published_at"])

upload_df["year"] = upload_df["published_at"].dt.year

uploads_per_year = (
    upload_df["year"]
    .value_counts()
    .sort_index()
)

print("\nUPLOADS PER YEAR")
print(uploads_per_year)

plt.figure(figsize=(10, 6))

plt.plot(
    uploads_per_year.index,
    uploads_per_year.values,
    marker="o"
)

plt.xlabel("Year")
plt.ylabel("Number of Videos Uploaded")

plt.grid()

plt.show()

query = """
SELECT title, view_count, duration
FROM videos
"""

duration_df = pd.read_sql_query(query, connection)

duration_df["duration_minutes"] = duration_df["duration"].apply(
    duration_to_minutes
)

normal_duration_df = duration_df[
    duration_df["duration_minutes"] <= 60
]

print("\nDURATION DATA")
print(
    duration_df[
        ["title", "duration", "duration_minutes", "view_count"]
    ].head()
)

plt.figure(figsize=(10, 6))

plt.scatter(
    duration_df["duration_minutes"],
    duration_df["view_count"],
    alpha=0.3
)

plt.xlabel("Video Duration (minutes)")
plt.ylabel("Views")
plt.title("Video Duration vs Views - penguinz0")

plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

plt.scatter(
    normal_duration_df["duration_minutes"],
    normal_duration_df["view_count"],
    alpha=0.3
)

plt.xlabel("Video Duration (minutes)")
plt.ylabel("Views")
plt.title("Video Duration vs Views - Videos Under 60 Minutes")

plt.grid()
plt.show()

bins = [0, 5, 10, 15, 20, 30, 60]

labels = [
    "0-5",
    "5-10",
    "10-15",
    "15-20",
    "20-30",
    "30-60"
]

normal_duration_df = normal_duration_df.copy()

normal_duration_df["duration_group"] = pd.cut(
    normal_duration_df["duration_minutes"],
    bins=bins,
    labels=labels
)

average_views_by_duration = (
    normal_duration_df
    .groupby("duration_group", observed=True)["view_count"]
    .mean()
)

print("\nAVERAGE VIEWS BY VIDEO DURATION")
print(average_views_by_duration)

plt.figure(figsize=(10, 6))

average_views_by_duration.plot(
    kind="bar"
)

plt.xlabel("Video Duration (minutes)")
plt.ylabel("Average Views")
plt.title("Average Views by Video Duration - penguinz0")

plt.xticks(rotation=0)

plt.grid(axis="y")
plt.show()

# -----------------------------------
# Title length analysis
# -----------------------------------

query = """
SELECT title, view_count
FROM videos
"""

title_df = pd.read_sql_query(query, connection)

title_df["title_length"] = title_df["title"].str.len()

print("\nTITLE LENGTH DATA")
print(
    title_df[
        ["title", "title_length", "view_count"]
    ].head()
)

plt.figure(figsize=(10, 6))

plt.scatter(
    title_df["title_length"],
    title_df["view_count"],
    alpha=0.3
)

plt.xlabel("Title Length (characters)")
plt.ylabel("Views")
plt.title("Title Length vs Views - penguinz0")

plt.grid()
plt.show()

title_bins = [0, 20, 30, 40, 50, 60, 80, 120]

title_labels = [
    "0-20",
    "20-30",
    "30-40",
    "40-50",
    "50-60",
    "60-80",
    "80-120"
]

title_df["title_group"] = pd.cut(
    title_df["title_length"],
    bins=title_bins,
    labels=title_labels
)

average_views_by_title = (
    title_df
    .groupby("title_group", observed=True)["view_count"]
    .mean()
)

print("\nAVERAGE VIEWS BY TITLE LENGTH")
print(average_views_by_title)

plt.figure(figsize=(10, 6))

average_views_by_title.plot(
    kind="bar"
)

plt.xlabel("Title Length (characters)")
plt.ylabel("Average Views")
plt.title("Average Views by Title Length - penguinz0")

plt.xticks(rotation=0)
plt.grid(axis="y")

plt.show()


connection.close()