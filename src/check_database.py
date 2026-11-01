import sqlite3

connection = sqlite3.connect("data/videos.db")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM videos")

result = cursor.fetchone()

print("Number of videos in database:", result[0])

connection.close()