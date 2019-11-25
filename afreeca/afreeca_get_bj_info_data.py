from http_data import url, headers
# from urllib.request import Request, urlopen
# import json
import requests

def bj_info_data(bj_id):
    try:
        bj_info = requests.get(url + bj_id + '/station', headers=headers).json()
        img = bj_info['profile_image'] # 이미지
        introduce = bj_info['station']['display']['profile_text'] # 소개
        name = bj_info['station']['user_nick'] # 닉네임
        fav_fan = bj_info['station']['upd']['fan_cnt'] # 즐찾 수
        t_view_cnt = bj_info['station']['upd']['total_view_cnt'] # 총 비디오 조회수
        signup = bj_info['station']['jointime'] # 생성일
        print(img, introduce, name, fav_fan, t_view_cnt, signup)
    except:
        pass