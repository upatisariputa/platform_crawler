import os, time
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from http_data import url, headers
import requests
from db_config.db_call_procedure import call_procedure
from time import localtime, strftime

# time
time = time.localtime()
year = time.tm_year
month = time.tm_mon
day = time.tm_mday
week = int(time.tm_yday/7)
createtime = strftime('%Y-%m-%d', localtime())


def bj_videos_data(bj_id, key):
    bj_info_data_list = []
    bj_video = requests.get(url + bj_id + '/vods', headers=headers).json()
    last_page_num = bj_video['meta']['last_page']

    try:
        for page_num in range(1, last_page_num):
            bj_video = requests.get(url + bj_id + '/vods?page=' + str(page_num), headers=headers).json()
            video_data = bj_video['data']
            for data in video_data:
                call_procedure('video_saver', (data['title_name'], data['title_no'], data['title_no'], data['reg_date'].split(' ')[0], createtime, data['count']['like_cnt'], 0, data['count']['comment_cnt'], data['count']['read_cnt'], year, month, day, week, key))

    except:
        pass