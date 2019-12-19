import requests, sys, os
from http_data import url, headers


def bj_info(id):
    bj_info_datas = {}
    res = requests.get(url + 'users?id=' + id, headers=headers).json()
    try:
        bj_name = res['data'][0]['display_name']
        bj_image = res['data'][0]['offline_image_url']
        bj_platform = 1
        bj_info_data = {'bj_name' : bj_name, 'bj_image': bj_image, 'bj_platform' : bj_platform}
        return bj_info_data

    except Exception as e:
        print(e)

