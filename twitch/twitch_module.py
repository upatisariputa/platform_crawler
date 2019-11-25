from twitch_get_user_id import get_user_id, bj_ids_datas
from twitch_get_bj_videos_data import get_bj_video
from twitch_get_bj_info_data import get_bj_info
from twitch_get_bj_follower_data import get_bj_fw_data

get_user_id()

if len(bj_ids_datas) > 0:
    for id_data in bj_ids_datas:
        get_bj_info(id_data)
        get_bj_fw_data(id_data)
        get_bj_video(id_data)

