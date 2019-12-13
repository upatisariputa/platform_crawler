from get_youtube_bj_info import video_url
from youtube_driver import options, driver, Keys, BeautifulSoup, delay
import time
import random
import re


def get_bj_video(video_url):
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
        like_cnt = soup.find('yt-formatted-string',{'id':'text','class':'style-scope ytd-toggle-button-renderer style-text','aria-label':re.compile('좋아요')})
        unlike_cnt = soup.find('yt-formatted-string',{'id':'text','class':'style-scope ytd-toggle-button-renderer style-text','aria-label':re.compile('싫어요')})
        comment_cnt = soup.find('ytd-comments', {'id' : 'comments'}).find('yt-formatted-string', 'count-text style-scope ytd-comments-header-renderer')

        if like_cnt is not None:
            like_cnt = like_cnt.string
        if unlike_cnt is not None:
            unlike_cnt = unlike_cnt.string
        if comment_cnt is not None:
            comment_cnt = comment_cnt.string


        print(video_title, upload_date, view_cnt, like_cnt, unlike_cnt, comment_cnt)
