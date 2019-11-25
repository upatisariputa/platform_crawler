from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import random
import re

path = '/Users/sitaruta/Downloads/chromedriver'
delay = random.randrange(3, 6)


options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
options.add_argument('lang=ko_KR')
options.add_argument('--mute-audio')
# 자동재생 정책을 설정했지만 작동 안 함
options.add_argument('autoplay-policy=no-user-gesture-required')
# 기타 다른 옵션 (이미지 등)
prefs = {'profile.default_content_setting_values': {'images' : 2, 'media_stream': 2, 'media_stream_mic':2, 'media_stream_camera':2, 'mixed_script': 2, 'protected_media_identifier':2, 'stylesheet' :2, 'notifications' :2, 'popups' :2, 'plugins' :2 , 'app_banner':2}}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(path, chrome_options=options)
driver.implicitly_wait(delay)
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
# lanuages 속성을 업데이트해주기
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# driver.get('https://www.youtube.com/channel/'+bj_id+'/videos?view=0&sort=dd&shelf_id=0')
driver.maximize_window()

# youtube_chrm_driver_open('UC8qO5racajmy4YgPgNJkVXg')