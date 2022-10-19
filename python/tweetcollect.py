from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty

from credentials import *
import os
import tweepy as tw
import pandas as pd
# import snscrape.modules.twitter as sntwitter

import csv
from templates import *
from tweepy import *
import tweepy
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

userID = "realDonaldTrump"
consumer_key="JglqaxdDIbqZb9NJTuCaL12Gc"
consumer_secret="t8qfyoaJkKbMjn9ihJ2TYKV0hYEefenSFLpab3S8HjyD2x6nHm"
access_token="1493319270-e4PxEbZxUQqy6tppWpwHvWW9aFJWiUxcuIVvuPt"
access_token_secret="cXS8sXl3TPcmSTI6xD9wcFiz8yp70Tp16W1z9ocS7WYyt"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
api.search_tweets

class TweetCollect(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()
    
    def disconnect2(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()
    
    def open(self):
        show_popup()

    def snstw(self, tweet_count, lang, since_date, until_date, text_query, near, fromuser, filname):#collect
        self.tweet_count = tweet_count
        self.lang = lang
        self.since_date = since_date
        self.until_date = until_date
        self.text_query = text_query
        self.near = near
        self.fromuser = fromuser
        self.filname = filname
        filname = filname + ".csv"
        lang = lang.lower()     
        print(lang)        
        print(filname)        
             
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
            
        filname2 = filname
        try:   
            ff=str(filname)
            filname=desktop+"//"+filname
            os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} until:{} lang:{}"> {}'
                    .format(tweet_count, since_date, text_query, fromuser, until_date, lang,filname))
            tweets_df2 = pd.read_json(filname, lines=True,encoding='utf-8')
            tweets_df2.to_csv(filname ,index=False)
            result3="successfully completed with {} results".format(len(tweets_df2))
            print(result3)
        except:   
            desktop2 = desktop.replace("Desktop","Masaüstü")
            ff=str(filname2)
            filname2=desktop2+"//"+filname2
            os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} until:{} lang:{}"> {}'
                    .format(tweet_count, since_date, text_query, fromuser, until_date, lang,filname2))
            tweets_df2 = pd.read_json(filname2, lines=True,encoding='utf-8')
            tweets_df2.to_csv(filname2 ,index=False)
            result3="successfully completed with {} results".format(len(tweets_df2))
            print(result3)
        return "a"

class P(FloatLayout):
    pass
def show_popup():
    show = P()
    popupWindow = Popup(title="Alert!",title_size=17,content=show,size_hint =(None, None),size=(400,400))
    popupWindow.open() 
    

