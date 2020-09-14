import requests
import re
import json
from urllib.parse import quote
import random

proxy_list = open('proxy.txt', mode='r', encoding='utf-8').read().split('\n')

def checkProxy(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    try:
        requests.get('http://api.ipify.org/',proxies=proxies).text
        return True
    except:
        return False

s = requests.Session()
while True:
    chosen = random.choice(proxy_list)
    print("Using proxy: {}".format(chosen))
    if checkProxy(chosen):
        print("Proxy is up!")
        break
    else:
        print("Proxy is down! Trying one more ...")
