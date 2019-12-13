from get_from_youtube_api import get_from_youtube_api
from get_youtube_bj_info import video_url, get_bj_info
from get_youtube_bj_video import get_bj_video
from youtube_bj_data import bj_data
from youtube_driver import driver

# 멀티프로세싱, 멀티쓰레드 해보기

get_from_youtube_api('UCu750LH-nGQetXoosDwcWOg')

for data in bj_data:
    get_bj_info(data)
    print(video_url)

    if isinstance(video_url, list):
        get_bj_video(video_url)

driver.quit()