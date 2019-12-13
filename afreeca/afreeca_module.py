from afreeca_get_bj_info_data import bj_info_data
from afreeca_id_datas import id_datas
from afreeca_get_bj_fan_cnt import get_bj_fan_cnt
from db_connector import db, cursor

for id in id_datas:
    bj_info_data_list = bj_info_data(id)
    bj_fan_cnt = get_bj_fan_cnt(id)
    bj_info_data_list.append(bj_fan_cnt['fanclub'])
    bj_info_data_list.append(bj_fan_cnt['supporter'])

    print(bj_info_data_list)
    with db.cursor() as cursor:
        sql = 'INSERT INTO'

