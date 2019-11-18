from http_data import url, headers
from urllib.request import Request, urlopen
import json
import requests

def af_get_data(bjID):
    res = requests.get(url + bjID + '/station').json()
    print(res)

af_get_data('eunz1nara')