from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty
from facebook_scraper import *
from facebook_scraper import get_posts
import pandas as pd
#import ast
import time
from kivy.clock import Clock
from datetime import datetime

import requests
import logging


from credentials import *
import os

import tweepy as tw
import pandas as pd

import csv
from templates import *
from tweepy import *
import tweepy
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, ObjectProperty, BooleanProperty
import webbrowser

class FacebookKV(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'social_media'
        self.manager.get_screen('login').resetForm()

    def disconnect2(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()

        
    def open_page(self):
        
        webbrowser.open('html_files\\facebook.html')

    start_url = None

    # def handle_pagination_url(url, ccid):
    #     global start_url
    #     start_url = url
    #     resq = []
    #     while True:
    #         try:
    #             post = next(
    #                 get_posts(
    #                     post_urls=ccid,
    #                     options={
    #                         "comments": "generator",
    #                         "comment_start_url": start_url,
    #                         "comment_request_url_callback": handle_pagination_url,
    #                     },
    #                 )
    #             )
    #             comments = post["comments_full"]
    #             for comment in comments:
    #                 print(comment)
    #                 resq.append(comment)
    #             print("All done")
    #             break
    #         except exceptions.TemporarilyBanned:
    #             print("Temporarily banned, sleeping for 10m")
    #             time.sleep(600)
    #     return resq

# button functionss************************************

    def fb_router2(self,search_word,filname):

        self.search_word = search_word
        self.filname = filname
        filname=filname+'.csv'
        posts = []
        count = 0
        enable_logging(logging.DEBUG)
        a_logger = logging.getLogger()
        start = time.time()
        res = []
        print(search_word)
        print("befffffffffffor ")
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
            h = os.getcwd()
            filname2 = filname
            if(h.startswith("/home")):

            # if search_word != None:

                print("in ifffffffffffffff")
                try:
                    filname = desktop + "/" + filname
                    for post in get_posts(search_word, cookies="/home/bilgi/cookies.txt", pages=100, timeout=60,
                                          options={"comments": True, "allow_extra_requests": False, "posts_per_page": 10}):
                        count += 1
                        posts.append(post)
                        df = post['post_url']
                        df2 = post['post_id']
                        print("rrrrrrrrrrrrrrrrrrrrrrrrr")
                        # hh=handle_pagination_url(df,df2)
                        print("ssssssssssssssssssssssssssss")
                        # print(hh)






                except:
                    print(
                        f"{len(posts)} posts retrieved in {round(time.time() - start)}s. Oldest post: {posts[-1].get('time')}")

                df1 = pd.DataFrame(posts)
                print(df1)
                df1.to_csv(filname, index=False, header=True)
                print("csv file filled")
                self.ids.deneme.text == "Succes."
                self.update_label2("Succes.")

                fbresult = "Facebook search completed with {} results successfully ".format(count)
            else:
                try:
                    filname2 = desktop + "//" + filname2
                    for post in get_posts(search_word, cookies="/home/bilgi/cookies.txt", pages=200, timeout=60,
                                          options={"comments": True, "allow_extra_requests": False, "posts_per_page": 200}):
                        count += 1
                        posts.append(post)
                        df = post['post_url']
                        df2 = post['post_id']
                        print("rrrrrrrrrrrrrrrrrrrrrrrrr")
                        # hh=handle_pagination_url(df,df2)
                        print("ssssssssssssssssssssssssssss")
                        # print(hh)





                except:
                    print(
                        f"{len(posts)} posts retrieved in {round(time.time() - start)}s. Oldest post: {posts[-1].get('time')}")

                df1 = pd.DataFrame(posts)
                print(df1)
                df1.to_csv(filname2, index=False, header=True)

                self.ids.deneme.text == "Succes."
                self.update_label2("Succes.")


                fbresult = "Facebook search completed with {} results successfully ".format(count)
        except:
            pass



#  spinner taggggggggggggggggggggggg

    def update_label2(self, txt, filname, *args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname = desktop + "/" + filname + ".csv"
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
#*********** trigger to button function----------------
    def update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Facebook crawl works Loading..."):
            print("girdi")
            self.function_interval.cancel()
            FacebookKV.fb_router2(self, self.search_word, self.filname)
            self.update_label2("Succes.", self.filname)


# getting .kv parameters
    def fb_router(self, search_word, filname):  # eklenecek

        self.search_word = search_word
        self.filname = filname

        self.ids.deneme.text = "Facebook crawl works Loading..."
        self.function_interval = Clock.schedule_interval(self.update_label, 0.05)





    