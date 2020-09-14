from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from threading import Thread

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

# Both Use to store data that we want tot show on screen
line1 = "None"
line2 = "None"

def check_fun():
    """
        Store proxy ip and msg in line1 and line2
    """
    while True:
            chosen = random.choice(proxy_list)
            global line1, line2
            line1 = "Using proxy: {}".format(chosen)
            print(line1)
            if checkProxy(chosen):
                line2 = "Proxy is up!"
                print(line2)
                break
            else:
                line2 = "Proxy is down! Trying one more ..."
                print(line2)

        
t1 = Thread(target= check_fun)  
class Home(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def start_checking(self):
        """
            Run This Method when play button press 
        """
        t1.start() 
        Clock.schedule_interval(self.update_, 0.5) # every time update screen in .5 sec
        print("it's work")
    
    def update_(self,dt):
        """
            Store data ip and msg in line1 and line2 
            and print it in console
        """
        global line1, line2
        print(line1,line2)
        self.ids.line1.text = line1
        self.ids.line2.text = line2




class MainApp(MDApp):
    def build(self):
        return Home()


if __name__ == "__main__":
    MainApp().run()
