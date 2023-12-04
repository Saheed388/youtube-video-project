import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# You should replace 'your_api_key' with your actual YouTube Data API key
api_key = 'put you api'
max_results = 50  # Adjust the number of results as needed

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from the YouTube API
    """
    search_url = "https://www.googleapis.com/youtube/v3/search"
    video_url = "https://www.googleapis.com/youtube/v3/videos"
    channels_url = "https://www.googleapis.com/youtube/v3/channels"

    video_data = []

    page_token = None
    total_videos = 0

    while True:
        search_params = {
            "key": api_key,
            "part": "snippet",
            "q": "Data",
            "type": "video",
            "maxResults": max_results,
            "pageToken": page_token
        }

        search_response = requests.get(search_url, params=search_params)

        if search_response.status_code == 200:
            search_results = search_response.json()
            video_ids = [item['id']['videoId'] for item in search_results['items']]
            channel_ids = [item['snippet']['channelId'] for item in search_results['items']]

            for i, (video_id, channel_id) in enumerate(zip(video_ids, channel_ids), total_videos):
                print(f"Downloading video {i + 1} of {total_videos + len(video_ids)}")

                video_params = {
                    "key": api_key,
                    "part": "snippet,statistics,contentDetails",
                    "id": video_id
                }
                video_response = requests.get(video_url, params=video_params)

                channel_params = {
                    "key": api_key,
                    "part": "snippet,statistics",
                    "id": channel_id
                }
                channel_response = requests.get(channels_url, params=channel_params)

                if video_response.status_code == 200 and channel_response.status_code == 200:
                    video_details = video_response.json()
                    channel_details = channel_response.json()
                    video_snippet = video_details['items'][0]['snippet']
                    video_statistics = video_details['items'][0]['statistics']
                    video_content_details = video_details['items'][0]['contentDetails']
                    channel_snippet = channel_details['items'][0]['snippet']
                    channel_statistics = channel_details['items'][0]['statistics']
                    video_duration = video_content_details['duration']
                    video_date_posted = video_snippet['publishedAt']
                    video_title = video_snippet['title']
                    view_count = video_statistics.get('viewCount', 0)
                    like_count = video_statistics.get('likeCount', 0)
                    comment_count = video_statistics.get('commentCount', 0)
                    subscriber_count = channel_statistics.get('subscriberCount', 0)
                    channel_name = channel_snippet['title']

                    video_data.append({
                        "Video Title": video_title,
                        "Channel Name": channel_name,
                        "Duration": video_duration,
                        "Date Posted": video_date_posted,
                        "Views": view_count,
                        "Likes": like_count,
                        "Comments": comment_count,
                        "Subscribers": subscriber_count
                    })

                else:
                    print(f"Error in video request for video {i + 1}: {video_response.status_code}")

            page_token = search_results.get('nextPageToken')
            if not page_token:
                break

        else:
            print("Error in search request:", search_response.status_code)

    df = pd.DataFrame(video_data)
    csv_filename = "youtube_data.csv"
    df.to_csv(csv_filename, index=False)

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
