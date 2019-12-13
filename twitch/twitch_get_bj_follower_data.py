import requests
from twitch_client_id import client_id
from http_data import url, headers
from twitch_bj_id_data import bj_ids_datas

def get_bj_fw_data(ids = bj_ids_datas):
    bj_fw_data = []
    if isinstance(ids, list):
        for id in ids:
            res = requests.get(url + 'users/follows?to_id=' + id, headers=headers).json()
            if res == {'data': []} or res is None:
                pass
            else:
                fw_cnt = res['total']
                print(fw_cnt)
    else:
        res = requests.get(url + 'users/follows?to_id=' + ids, headers=headers).json()
        if res == {'data': []} or res is None:
            pass
        else:
            fw_cnt = res['total']
            print(fw_cnt)
                