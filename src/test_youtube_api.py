import os 
import pandas as pd

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

# Create a connection to the YouTube Data API
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    forHandle="@penguinz0"
)

# Send the request
response = request.execute()

channel = response["items"][0]

channel_name = channel["snippet"]["title"]
channel_id = channel["id"]
subscribers_counts = channel["statistics"]["subscriberCount"]
view_count = channel["statistics"]["viewCount"]
video_count = channel["statistics"]["videoCount"]
uploads_playlist_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]\

print("Channel Name: ", channel_name)
print("Channel ID: ", channel_id)
print("Subscribers Count: ", subscribers_counts)
print("View Count: ", view_count)
print("Video Count: ", video_count)
print("Uploads Playlist ID: ", uploads_playlist_id)



video_ids = []

page_token = None

while True:
    playlist_request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=uploads_playlist_id,
        maxResults=50,
        pageToken=page_token
    )

    playlist_response = playlist_request.execute()

    for item in playlist_response["items"]:
        video_id = item["contentDetails"]["videoId"]
        video_ids.append(video_id)

    print("Videos collected:", len(video_ids))

    page_token = playlist_response.get("nextPageToken")

    if page_token is None:
        break

print("Finished collecting videos")
print("Total videos collected:", len(video_ids))

all_videos_data = []

for i in range(0, len(video_ids), 50):
    batch = video_ids[i:i+50]

    video_request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=",".join(batch)
    )

    video_response = video_request.execute()

    for video in video_response["items"]:

        video_data = {
            "video_id": video["id"],
            "title": video["snippet"]["title"],
            "published_at": video["snippet"]["publishedAt"],
            "view_count": video["statistics"].get("viewCount"),
            "like_count": video["statistics"].get("likeCount"),
            "comment_count": video["statistics"].get("commentCount"),
            "duration": video["contentDetails"]["duration"],
            "thumbnail_url": video["snippet"]["thumbnails"]["high"]["url"],

        }

        all_videos_data.append(video_data)

    print("Metadata collection completed", len(all_videos_data))

df = pd.DataFrame(all_videos_data)

print(df.head())

df.to_csv(
    "data/videos.csv",
    index=False
)

print("Saved to data/videos.csv")