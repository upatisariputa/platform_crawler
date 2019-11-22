import requests
from youtube_api_key import api_key_1

def get_from_youtube_api(id):
    name = id

    base_url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&part=statistics&id="

    key = api_key_1

    url = base_url + name + "&key=" + key

    data = requests.get(url,).json()
    subscriber_cnt = data['items'][0]['statistics']['subscriberCount']
    video_cnt = data['items'][0]['statistics']['videoCount']
    view_cnt = data['items'][0]['statistics']['viewCount']
    # info = []
    print(data)

get_from_youtube_api('UC3SyT4_WLHzN7JmHQwKQZww')

# https://github.com/skfn20/webscraping/blob/9a5147d9b312536b56afefda821c1a857f6c6459/youtubeScraper/youtube_Title_subscribe.py