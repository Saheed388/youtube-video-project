import json
import requests
import os
import pandas as pd
from datetime import datetime, timedelta
from refresh_token import Refresh
from confluent_kafka import Producer
import time
import logging
from secret_file import spotify_user_id
import functions_framework

# Configure logging
logging.basicConfig(filename='spotify_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@functions_framework.http
class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.tracks = ""

    def get_recently_played(self):
        today = datetime.now()
        past_7_days = today - timedelta(days=8)
        past_7_days_unix_timestamp = int(past_7_days.timestamp()) * 1000

        endpoint = "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(
            time=past_7_days_unix_timestamp)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        }
        r = requests.get(endpoint, headers=headers, params={"limit": 50})
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def call_refresh(self):
        logging.info("Refreshing token")
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()

    def push_to_kafka(self, topic, message):
        kafka_config = {
            'bootstrap.servers': '34.42.19.194:9092',
        }

        producer = Producer(kafka_config)
        producer.produce(topic, value=message)
        producer.flush()

    def save_to_csv(self, data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        logging.info(f"Data has been successfully saved to CSV file: {filename}")

    def push_csv_to_kafka(self, topic, filename):
        with open(filename, 'r') as file:
            csv_data = file.read()

        self.push_to_kafka(topic, csv_data)
        logging.info(f"CSV data has been successfully pushed to Kafka topic: {topic}")

    def push_json_to_kafka(self, topic, json_data):
        self.push_to_kafka(topic, json_data)
        logging.info(f"JSON data has been successfully pushed to Kafka topic: {topic}")

if __name__ == "__main__":
    a = SaveSongs()

    while True:
        a.call_refresh()

        data = a.get_recently_played()

        logging.info("Key-Value pairs in data:")
        for key, value in data.items():
            logging.info(f"{key}: {value}")

        song_list = []

        for song_item in data["items"]:
            track_info = song_item["track"]
            song_data = {
                "song_name": track_info["name"],
                "artist_name": track_info["artists"][0]["name"],
                "featured_artists": [artist["name"] for artist in track_info["artists"][1:]],
                "played_at": song_item["played_at"],
                "timestamp": song_item["played_at"][0:10],
                "popularity": track_info["popularity"],
                "album_or_single": track_info["album"]["album_type"]
            }
            song_list.append(song_data)

        csv_filename = 'spotify_data.csv'
        a.save_to_csv(song_list, csv_filename)

        df = pd.DataFrame(song_list)
        json_data = df.to_json(orient="records")

        topic_csv = 'my2_topic'
        a.push_csv_to_kafka(topic_csv, csv_filename)

        topic_json = 'my1_topic'
        a.push_json_to_kafka(topic_json, json_data)

        logging.info("Data has been successfully pushed to Kafka topics: %s, %s", topic_csv, topic_json)

        # Sleep for 3 minutes
        time.sleep(30)
    if __name__ == "__main__":
    functions_framework.start()