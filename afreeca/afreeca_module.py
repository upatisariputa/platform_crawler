import os, time
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from afreeca_get_bj_info_data import bj_info_data
from afreeca_id_datas import id_datas
from afreeca_get_bj_fan_cnt import get_bj_fan_cnt
from db_config.db_call_procedure import call_procedure
from time import localtime, strftime

# time
time = time.localtime()
year = time.tm_year
month = time.tm_mon
day = time.tm_mday
week = int(time.tm_yday/7)
createtime = strftime('%Y-%m-%d', localtime())

for key, id in id_datas.items():
    bj_info_data_list = []
    try:
        # Creater data api function
        bj_info_data_dic = bj_info_data(id)
        bj_fan_cnt = get_bj_fan_cnt(id)

        bj_info_data_dic['bj_num'] = key    #크리에이터 넘버

        # Creater info
        bj_info_data_list = (bj_info_data_dic['bj_num'], bj_info_data_dic['bj_name'], bj_info_data_dic['bj_img_url'], bj_info_data_dic['bj_cre_date'], bj_info_data_dic['bj_platform'], bj_info_data_dic['bj_url'])
        
        # Creater total
        bj_total_list = (createtime, bj_info_data_dic['total_view_cnt'], bj_info_data_dic['total_ok_cnt'], 0, 0, year, month, day, week, bj_info_data_dic['bj_num'], )

        # Creater sub
        bj_sub_list = (createtime, bj_fan_cnt['fanclub'], year, month, day, week, bj_info_data_dic['bj_num'])

        # call procedure
        call_procedure('info_saver', bj_info_data_list)
        call_procedure('total_saver', bj_total_list)
        call_procedure('sub_saver', bj_sub_list)


    except Exception as e:
        print(e)