import requests, os, sys, time
from twitch_client_id import client_id
from http_data import url, headers
from time import localtime, strftime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.db_call_procedure import call_procedure

# time
time = time.localtime()
year = time.tm_year
month = time.tm_mon
day = time.tm_mday
week = int(time.tm_yday/7)
createtime = strftime('%Y-%m-%d', localtime())

def bj_video(id, bj_num):
    res = requests.get(url + 'videos?user_id=' + id + '&first=100', headers=headers).json()
    try:
        all_video_view_cnt = 0
        for data in res['data']:
            video_title = data['title']
            video_num = data['id']
            video_view_cnt = data['view_count']
            video_cre_date = data['created_at'].split('T')[0]
            video_url = data['url']
            bj_video_data = (video_title, video_num, video_num, video_cre_date, createtime, 0, 0, 0, video_view_cnt, year, month, day, week, bj_num)
            call_procedure('video_saver',  bj_video_data)
            all_video_view_cnt += video_view_cnt
        return all_video_view_cnt

    except Exception as e:
        print(e)

bj_video('425968734' , 14221)