from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
import re
import random

def youtube_crawler_module(bj_id):
    path = '/Users/sitaruta/Downloads/chromedriver'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    options.add_argument('lang=ko_KR')
    options.add_argument('--mute-audio')
    options.add_argument("autoplay-policy=no-user-gesture-required")
    # 이미지 없애기
    # prefs = {"media.autoplay.enabled" : False}
    prefs = {'profile.default_content_setting_values': {'images' : 2, 'media_stream': 2, 'media_stream_mic':2, 'media_stream_camera':2, 'mixed_script': 2, 'protected_media_identifier':2, 'stylesheet' :2, 'notifications' :2, 'popups' :2, 'plugins' :2 , 'app_banner':2}}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(path, chrome_options=options)


    delay = random.randrange(3,6)
    driver.implicitly_wait(delay)
    # 플러그인 속성 업데이트
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
    # lanuages 속성을 업데이트해주기
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.get('https://www.youtube.com/channel/'+ bj_id +'/videos?view=0&sort=dd&shelf_id=0')
    # driver.maximize_window()

    body = driver.find_element_by_tag_name('body')

    num_of_pagedowns = 2
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1.5)
        num_of_pagedowns -= 1

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    video_list0 = soup.find('div', {'id': 'contents'})
    video_list2 = video_list0.find_all('ytd-grid-video-renderer',{'class':'style-scope ytd-grid-renderer'})

    base_url = 'http://www.youtube.com'
    video_url = []
    for i in range(len(video_list2)):
        url = base_url+video_list2[i].find('a',{'id':'thumbnail'})['href']
        video_url.append(url)

    for i in range(len(video_url)):
        start_url = video_url[i]
        print(start_url)
        driver.implicitly_wait(delay)
        driver.get(start_url)
        driver.maximize_window()
        body = driver.find_element_by_tag_name('body')
        time.sleep(delay)

        # body.send_keys(Keys.SPACE)
        # driver.find_element_by_class_name('ytp-play-button ytp-button').click()

        num_of_pagedowns = 1
        while num_of_pagedowns:
            body.send_keys(Keys.SPACE)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1.5)
            num_of_pagedowns -= 1

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        video_title = soup.find('h1', 'title style-scope ytd-video-primary-info-renderer').string
        upload_date = soup.find('div', {'id' : 'date'}).find('yt-formatted-string', 'style-scope ytd-video-primary-info-renderer').string
        view_cnt = soup.find('span', 'view-count style-scope yt-view-count-renderer').string
        like_cnt = soup.find('yt-formatted-string',{'id':'text','class':'style-scope ytd-toggle-button-renderer style-text','aria-label':re.compile('좋아요')}).string
        unlike_cnt = soup.find('yt-formatted-string',{'id':'text','class':'style-scope ytd-toggle-button-renderer style-text','aria-label':re.compile('싫어요')}).string
        comment_cnt = soup.find('ytd-comments', {'id' : 'comments'}).find('yt-formatted-string', 'count-text style-scope ytd-comments-header-renderer').string
        

        print(video_title, upload_date, view_cnt, like_cnt, unlike_cnt, comment_cnt)

    driver.quit()