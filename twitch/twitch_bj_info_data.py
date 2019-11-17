import requests
from clientID import client_id
from http_data import url, headers
from twitch_bj_id_data import bj_ids_datas


def get_bj_info(ids = bj_ids_datas):
    bj_info_datas = {}
    if isinstance(ids, list):
        for id in ids:
            res = requests.get(url + 'users?id=' + id, headers=headers)
            bj_info = res.json()
            if bj_info == {'data': []} or bj_info is None:
                pass
            else:
                bj_name = bj_info['data'][0]['display_name']
                bj_image = bj_info['data'][0]['offline_image_url']
                bj_platform = 'twitch'
                bj_ids_datas = {'bj_name': bj_name, 'bj_image': bj_image, 'bj_platform' : bj_platform}
                print(bj_ids_datas)
    else:
        res = requests.get(url + 'users?id=' + ids, headers=headers)
        bj_info = res.json()
        if bj_info == {'data': []} or bj_info is None:
            pass
        else:
            bj_name = bj_info['data'][0]['display_name']
            bj_image = bj_info['data'][0]['offline_image_url']
            bj_platform = ''
            bj_ids_datas = {'bj_name' : bj_name, 'bj_image': bj_image, 'bj_platform' : bj_platform}
            print(bj_ids_datas)

get_bj_info()