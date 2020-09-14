import requests
import re
import json
from urllib.parse import quote
import random
import threading

# Fixed Screen size as android screen
from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')
# remove both line when build App

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.label import MDLabel

proxy_list = open('proxy.txt', mode='r', encoding='utf-8').read().split('\n')


def checkProxy(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    try:
        requests.get('http://api.ipify.org/', proxies=proxies).text
        return True
    except:
        return False

class ProxyApp(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()

        global outputscreen
        outputscreen = Builder.load_file("ui//output.kv")

        screen_manager.add_widget(outputscreen)

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.primary_palette = "Red"
        print(Builder.load_file('ui//output.kv').ids)
        return screen_manager

    def show_data(self):
        output = outputscreen.ids.outputlist
        #thread = threading.Thread(target=self)
        #thread.start()

       # thread.join()

        while True:
            chosen = random.choice(proxy_list)
            output.add_widget(MDLabel(text="Using proxy: {}".format(chosen)))
            if checkProxy(chosen):
                output.add_widget(MDLabel(text="Proxy is up!"))
                break
            else:
                output.add_widget(MDLabel(text="Proxy is down, trying another!"))


if __name__ == "__main__":
    ProxyApp().run()