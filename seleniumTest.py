from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = '/Users/sitaruta/Downloads/chromedriver'
driver = webdriver.Chrome(path)

delay = 3
driver.implicitly_wait(delay)
driver.get('https://www.youtube.com/channel/UCdUcjkyZtf-1WJyPPiETF1g/videos')
driver.maximize_window()


body = driver.find_element_by_tag_name('body')

num_of_pagedowns = 10
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')
# 비디오 타이틀
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]
# 채널명
chennel = soup.find('span','style-scope ytd-c4-tabbed-header-renderer').string
#구독자 수
sub_num = soup.find('yt-formatted-string','style-scope ytd-c4-tabbed-header-renderer').string
#조회수, 올린지 얼마나 되었는지(업로드 시점)
c = soup.find_all('span','style-scope ytd-grid-video-renderer')
view_num = [soup.find_all('span','style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(c))]


driver.close()