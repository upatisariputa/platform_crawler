import requests
from clientID import client_id
from http_data import url, headers
from twitch_bj_name_data import bj_names_datas
# from twitch_bj_id_data import bj_ids_datas

def get_user_id(names = bj_names_datas): #매개변수에 기본값을 정의하고 싶을 경우 '='을 사용하여 기본값을 정해준다.
    bj_ids_datas = []
    if isinstance(names, list): # 인자가 list인지 아닌지 판별하여 list 이면 반복문을 실행한다.
        for name in names:
            res = requests.get(url + 'users?login=' + name, headers=headers)
            bj_id = res.json()
            print(name)
            if bj_id == {'data': []} or bj_id is None:
                bj_ids_datas.append('none')
            else:
                id = bj_id['data'][0]['id']
                bj_ids_datas.append(id)
            print(bj_ids_datas)
    else:
        res = requests.get(url + 'users?login=' + names, headers=headers)
        bj_id = res.json()
        if bj_id == {'data': []} or bj_id is None:
            pass # if문에서 아무것도 안 하고 싶을 경우 pass를 사용한다.
        else:
            id = bj_id['data'][0]['id']
            bj_ids_datas.append(id)
    
get_user_id()