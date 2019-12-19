import os, sys, time
from twitch_bj_info import bj_info
from twitch_bj_follower import bj_fw_data
from twitch_bj_video import bj_video
from time import localtime, strftime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.bj_num_datas_xl import get_id_from_xl
from config.db_call_procedure import call_procedure

# time
time = time.localtime()
year = time.tm_year
month = time.tm_mon
day = time.tm_mday
week = int(time.tm_yday/7)
createtime = strftime('%Y-%m-%d', localtime())

twitch_id_list = get_id_from_xl('twitch.xlsx', 'twitch')

for num in range(0, len(twitch_id_list)):
    id_num = str(twitch_id_list[num]['bj_id_num'])
    bj_num = twitch_id_list[num]['bj_num']
    info_data = bj_info(id_num)
    follwer_data = bj_fw_data(id_num)

    bj_info_data_list = (bj_num, info_data['bj_name'], info_data['bj_image'], '0000-00-00', 1, twitch_id_list[num]['bj_name'] )
    call_procedure('info_saver', bj_info_data_list)

    all_video_view_cnt = bj_video(id_num, bj_num)

    bj_total_data_list = (createtime, all_video_view_cnt, 0, 0, 0, year, month, day, week, bj_num)
    bj_sub_data_list = (createtime, follwer_data['bj_follower'], year, month, day, week, bj_num )

    call_procedure('total_saver', bj_total_data_list)
    call_procedure('sub_saver', bj_sub_data_list)

