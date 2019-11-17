import requests
from clientID import client_id
from http_data import url, headers
from twitch_bj_id_data import bj_ids_datas

def get_bj_video(id):
    bj_video_datas = {}
    res = requests.get(url + 'videos?user_id=' + id + '&first=100', headers=headers).json()
    if res == {'data': []} or res is None:
        pass
    else:
        all_video_view_cnt = 0
        for data in res['data']:
            video_title = data['title']
            video_view_cnt = data['view_count']
            video_url = data['url']
            bj_video_datas = {'video_title': video_title, 'video_view_cnt' : video_view_cnt, 'video_url': video_url}
            all_video_view_cnt += video_view_cnt
            print(bj_video_datas)
        print(all_video_view_cnt)
    # print(res)

get_bj_video('275644615')