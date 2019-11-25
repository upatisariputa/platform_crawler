from youtube_driver import options, driver, Keys, BeautifulSoup
import time
import random

video_url = []

def get_bj_info(bj_id):
    driver.get('https://www.youtube.com/channel/'+bj_id+'/videos?view=0&sort=dd&shelf_id=0')

    body = driver.find_element_by_tag_name('body')

    num_of_pagedowns = 2
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1.5)
        num_of_pagedowns -= 1

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    video_list0 = soup.find('div', {'id': 'contents'})
    if video_list0 is None:
        print('없는 주소입니다.')
    else:
        video_list2 = video_list0.find_all('ytd-grid-video-renderer',{'class':'style-scope ytd-grid-renderer'})

        base_url = 'http://www.youtube.com'
        for i in range(len(video_list2)):
            url = base_url+video_list2[i].find('a',{'id':'thumbnail'})['href']
            video_url.append(url)
        # return(video_url)

    # get_bj_info('UC8qO5racajmy4YgPgNJkVXg')