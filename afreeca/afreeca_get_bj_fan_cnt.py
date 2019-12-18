from http_data import url, headers
import requests

def get_bj_fan_cnt(bj_id):
    fan_cnt = ''
    try:
        bj_info = requests.get(url + bj_id + '/station/detail', headers=headers).json()
        fan_cnt = bj_info['count']
        return fan_cnt
        # print(fan_cnt)
    except:
        pass