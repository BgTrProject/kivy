from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty

from kivy.clock import Clock
from credentials import *
import os

import tweepy as tw
import pandas as pd

import csv
from templates import *
from .eksi_scraper import *
from tweepy import *
import tweepy
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, ObjectProperty, BooleanProperty
import webbrowser

class EksiKV(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'social_media'
        self.manager.get_screen('login').resetForm()

    def disconnect2(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()

        
    def open_page(self):
        
        webbrowser.open('html_files\\eksi.html')

#********************* eksi ---------------------*********---------*******


    def update_label2(self, txt,filname,*args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname=desktop+"/"+filname+".csv"
        self.ids.deneme.text = txt
        print("-------")
        print(self.ids.deneme.text)
        print("*******")
        if (self.ids.deneme.text == "Succes."):
            print("girdi")
            self.ids.deneme.text = "finished successfully at PATH : {} ".format(filname)
            print(self.filname)
            self.function_interval.cancel()
        else:
            print("nanay")
            print(self.ids.deneme.text)
            self.ids.deneme.text = "finished . PATH: " + self.filname
            print(self.filname)
            self.function_interval.cancel()

    def update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Eksi information crawl Loading..."):
            print("girdi")
            self.function_interval.cancel()
            EksiKV.eksi_router2(self, self.search_word, self.filname)
            self.update_label2("Succes.",self.filname)


    def eksi_router(self,search_word,filname):  # eklenecek

        self.search_word = search_word
        self.filname = filname

        self.ids.deneme.text = "Eksi information crawl Loading..."
        self.function_interval = Clock.schedule_interval(self.update_label, 0.05)




#---------eksi button functions -------------------------------------------------

    def eksi_router2(self,search_word,filname):
        # self.search_word=search_word
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        filname2 = filname

        if (h.startswith("/home")):
            filname3 = desktop + "/" + filname+'.csv'
            url = "https://eksisozluk.com/"
            eksi = Eksi(url,filname)
            eksi.start(url,search_word,filname)
        else:
            filname4 = desktop + "//" + filname2+'.csv'
            url = "https://eksisozluk.com/"
            eksi = Eksi(url.filname)

            eksi.start(url, search_word, filname)

class P(FloatLayout):
    pass
def show_popup():
    show = P()

    popupWindow = Popup(title="Press on the screen to turn it off!", title_size=17, content=show,
                    size_hint=(None, None), size=(500, 700))
    popupWindow.open()

        # scrape the data
        # eksi.scrape_all_pages(keywords)

        # get json output
        # eksi.get_json_output(filname)

