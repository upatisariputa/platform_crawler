from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = '/Users/sitaruta/Downloads/chromedriver'
driver = webdriver.Chrome(path)


delay = 3
driver.implicitly_wait(delay)
driver.get('https://www.youtube.com/channel/UC3SyT4_WLHzN7JmHQwKQZww/videos')
driver.maximize_window()


body = driver.find_element_by_tag_name('body')

num_of_pagedowns = 1
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')


# 채널명
channel = soup.find('yt-formatted-string','style-scope ytd-channel-name').string

# url
# all_video_url = soup.find_all('a', 'yt-simple-endpoint inline-block style-scope ytd-thumbnail')
# video_url = all_video_url.find()

# 비디오 타이틀
all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]

#조회수, 올린지 얼마나 되었는지(업로드 시점)
c = soup.find_all('span','style-scope ytd-grid-video-renderer')
view_num = [soup.find_all('span','style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(c))]

# print('title : ', title, 'channel : ', channel, 'sub_num : ', sub_num, 'c : ', c, 'view_num : ', view_num)

# print(video_url)

driver.close()

# https://github.com/minyong-shin/self-study/blob/master/MY-study/.ipynb_checkpoints/MY%20-%20%EC%9C%A0%ED%8A%9C%EB%B8%8C%20info%20%EB%B0%8F%20%EB%8C%93%EA%B8%80%20%ED%81%AC%EB%A1%A4%EB%A7%81-checkpoint.ipynb 참고