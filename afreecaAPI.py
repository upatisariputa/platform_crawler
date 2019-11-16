# bj 즐찾 수
URL = 'http://bjapi.afreecatv.com/api/'+bjID+'/station'
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
bj_info = json.load(response)

img = bj_info['profile_image'] # 이미지
introduce = bj_info['station']['display']['profile_text'] # 소개
name = bj_info['station']['user_nick'] # 닉네임
fav_fan = bj_info['station']['upd']['fan_cnt'] # 즐찾 수
t_view_cnt = bj_info['station']['upd']['total_view_cnt'] # 총 비디오 조회수
signup = bj_info['station']['jointime'] # 생성일

URL = 'http://bjapi.afreecatv.com/api/b13246/vods?page=' + page_number

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
vods_info = json.load(response)

last_page = vods_info['meta'][last_page] # 마지막페이지수
vods_name = [] # 비디오 이름
vods_readcnt = [] # 비디오 조회수
vods_likecnt = [] # 비디오 좋아요
vods_commentcnt = [] # 비디오 댓글수

for i in vods_info['data']:
    vods_name.append(i[title_name])
    vods_readcnt.append(i['count'][read_cnt])
    vods_likecnt.append(i['count'][like_cnt])
    vods_commentcnt.append(i['count'][comment_cnt])