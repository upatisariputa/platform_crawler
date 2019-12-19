import requests
from http_data import url, headers

def bj_fw_data(id):
    bj_follwer_datas = {}
    res = requests.get(url + 'users/follows?to_id=' + id, headers=headers).json()
    try:
        fw_cnt = res['total']
        bj_follwer_datas = {'bj_follower': fw_cnt}
        return bj_follwer_datas
    except Exception as e:
        print(e)