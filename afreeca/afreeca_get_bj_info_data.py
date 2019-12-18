from http_data import url, headers
# from urllib.request import Request, urlopen
# import json
import requests

# bj_info_data_list = []
def bj_info_data(bj_id):
    bj_info_data_dic={}
    try:
        bj_info = requests.get(url + bj_id + '/station', headers=headers).json()
        img = bj_info['profile_image'] # 이미지
        introduce = bj_info['station']['display']['profile_text'] # 소개
        name = bj_info['station']['user_nick'] # 닉네임
        fav_fan = bj_info['station']['upd']['fan_cnt'] # 즐찾 수
        t_view_cnt = bj_info['station']['upd']['total_view_cnt'] # 총 비디오 조회수
        t_ok_cnt = bj_info['station']['upd']['total_ok_cnt'] # 총 좋아요 수
        signup = bj_info['station']['jointime'].split(' ')[0] # 생성일
        bj_url = 'http://bj.afreecatv.com/' + bj_id # 주소
        bj_info_data_dic = {'bj_id': bj_id, 'bj_name': name, 'bj_img_url': img, 'bj_cre_date' : signup, 'bj_platform': 2, 'bj_url' : bj_url, 'total_view_cnt' : t_view_cnt, 'total_ok_cnt' : t_ok_cnt}
        return bj_info_data_dic
        # print(bj_info_data_list)
    except:
        pass