from afreeca_get_bj_info_data import bj_info_data
from afreeca_id_datas import id_datas
from afreeca_get_bj_fan_cnt import get_bj_fan_cnt


for id in id_datas:
    bj_info_data(id)
    get_bj_fan_cnt(id)