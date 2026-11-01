import sqlite3 
import pandas as pd

df = pd.read_csv("data/videos.csv")

connection =sqlite3.connect("data/videos.db")

df.to_sql(
    "videos",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Database created successfully")