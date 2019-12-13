import requests
from http_data import url, headers

def request_fn(req_url):
    r = requests.get(url + req_url, headers=headers)
    