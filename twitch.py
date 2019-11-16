client_id = 'gflzb7us8z6x634sd4fxsyg36qofi4'
headers = {'Client-ID' : client_id, 'referer' : 'https://twitch.tv'}
# referer란? Referer 요청 헤더는 현재 요청된 페이지의 링크 이전의 웹페이지 주소를 포함합니다. Referer 헤더는 사람들이 어디로부터 와서 방문 중인지를 인식할 수 있도록 해줍니다. 
# (https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Referer)

# bjinfo 가져오기
URL = 'https://api.twitch.tv/helix/users?id='+ bjID

req = Request(URL, headers = headers)
bjInfo = req.json()
        image_url = user['data'][0]['profile_image_url']
        user_name = user['data'][0]['display_name']
        user_info = user['data'][0]['description']