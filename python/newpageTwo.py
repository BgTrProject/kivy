from pickle import GLOBAL
from turtle import clear
from xmlrpc.client import boolean
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty
import sys
from credentials import *
import os
import webbrowser
import tweepy as tw
import pandas as pd
# from socialmedia.dtale import dtale
from pandas.io.json import json_normalize
# from dtale import *
import dtale
import csv
import time
from templates import *
from tweepy import *
import tweepy
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from pandas.io.json import json_normalize
import warnings

from kivy.clock import Clock

# class asa(Screen):
#     def __init__(self,lang1):
#         self.lang1=lang1
#
#     def on_spinner_select(self, text):
#         print(text)
#         self.lang1=text
#         return self.lang1


class NewPageTwo(Screen):

    ## *****  Dropdown function **********
    ll=""

    def on_spinner_select(self, ll):
        ll=ll
        return self.ll


#**********page arrangement function --------------------------
    
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'social_media'
        self.manager.get_screen('login').resetForm()
    
    def disconnect2(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()
    
    def open_page(self):
        
        webbrowser.open('html_files\\newpagetwo.html')
##---------------------- pop-up click function **********************************
    def language_webb(self):
        webbrowser.open("https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages")

    def search_web(self):
        webbrowser.open("https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query")

####**************** Complex Search Button Functions**********************************************

    def snstw(self, tweet_count, lang, since_date,until_date,text_query, fromuser, filname):#collect
        self.function_interval = Clock.schedule_interval(self.update_label, 0.05)
        self.tweet_count = tweet_count
        self.lang =lang
        self.since_date = since_date
        self.until_date = until_date
        self.text_query = text_query
        self.fromuser = fromuser
        self.filname = filname
        # lang = lang.lower()
        filname = filname + ".csv"
        print(self.tweet_count)        
        print(self.lang)
        print(type(self.lang))

        print(self.since_date)        
        print(self.text_query)        
        print(self.fromuser)        
        print(self.filname)   
             
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        filname2 = filname
        if str(self.lang)=='en' and str(self.until_date) !="":

            if (h.startswith("/home")):  # linux

                try:
                    ff = str(filname)
                    filname = desktop + "/" + filname
                    os.system(
                        'snscrape --jsonl --progress --max-results {} twitter-search  "its the elephant  --since:{}  until:{} twitter-search:{} from:{} lang:{}"> {}'
                        .format(tweet_count, since_date,until_date, text_query, fromuser, lang, filname))
                    # 'snscrape --jsonl --progress --max-results {} twitter-search   --since:{}  until:{} twitter-search:{} from:{} lang:{}> {}'
                    # .format(tweet_count, since_date, until_date, text_query, fromuser, lang, filname))
                    raw_tweets = pd.read_json(filname, lines=True, encoding='utf-8')
                    users = json_normalize(raw_tweets['user'])
                    users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
                    users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
                    # Create DataFrame and remove duplicates
                    users = pd.DataFrame(users)
                    # users.drop_duplicates(subset=['userId'], inplace=True)
                    # Transform 'raw_tweets' DataFrame
                    # Add column for 'userId'
                    user_id = [user['id'] for user in raw_tweets['user']]
                    raw_tweets['userId'] = user_id
                    # Remove less important columns
                    cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                            'quoteCount']
                    tweets = raw_tweets[cols]
                    tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
                    cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                            'location']
                    use = users[cols]
                    twts = use.merge(tweets, on='userId')
                    twts.to_csv(filname, index=False)
                    # tweets_df4.to_csv(filname4 ,index=False)
                    result4 = "successfully completed with {} results".format(len(twts))
                    print(result4)
                    df = pd.read_csv(filname)
                    d = dtale.show(df)
                    d.open_browser()
                    print("cccccccccccccccccccccccccc")
                    self.ids.deneme.text == "Succes."
                    self.update_lab2("Succes.")

                except:
                    print("pathway problem occurred for complex search . Please check your pathway")
                    pass
            else:  # windos için
                desktop2 = desktop.replace("Masaüstü", "Desktop")
                ff = str(filname2)
                filname2 = desktop2 + "\\" + ff
                os.system(
                    'snscrape --jsonl --progress --max-results {} --since {} --until {}twitter-search "{} from:{} lang:{}"> {}'
                    .format(tweet_count, since_date, until_date,text_query, fromuser, lang, filname2))
                # tweet_count, since_date, text_query, fromuser, lang, filname
                # (tweet_count.text, spinner.text, since_date.text, text_query.text, fromuser.text, filname.text)

                print(filname2)
                print("f222222222222222222222")
                raw_tweets = pd.read_json(filname2, lines=True, encoding='utf-8')
                # raw_tweets=tweet
                users = json_normalize(raw_tweets['user'])
                users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
                users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)

                users = pd.DataFrame(users)

                user_id = [user['id'] for user in raw_tweets['user']]
                raw_tweets['userId'] = user_id

                cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                        'quoteCount']
                tweets = raw_tweets[cols]
                tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
                cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                        'location']
                use = users[cols]
                twts = use.merge(tweets, on='userId')
                twts.to_csv(filname2, index=False)

                # tweets_df5.to_csv(filname5 ,index=False)
                result4 = "successfully completed with {} results".format(len(twts))
                print(result4)
                dfc = pd.read_csv(filname2)
                dc = dtale.show(dfc)
                dc.open_browser()

                return "a"
        else:
            if (h.startswith("/home")): #linux


                try:
                    ff=str(filname)
                    filname=desktop+"/"+filname
                    os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
                            .format(tweet_count, since_date, text_query, fromuser, lang,filname))
                    raw_tweets = pd.read_json(filname, lines=True, encoding='utf-8')
                    users = json_normalize(raw_tweets['user'])
                    users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
                    users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
                    # Create DataFrame and remove duplicates
                    users = pd.DataFrame(users)
                    # users.drop_duplicates(subset=['userId'], inplace=True)
                    # Transform 'raw_tweets' DataFrame
                    # Add column for 'userId'
                    user_id = [user['id'] for user in raw_tweets['user']]
                    raw_tweets['userId'] = user_id
                    # Remove less important columns
                    cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                            'quoteCount']
                    tweets = raw_tweets[cols]
                    tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
                    cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                            'location']
                    use = users[cols]
                    twts = use.merge(tweets, on='userId')
                    twts.to_csv(filname, index=False)
                    # tweets_df4.to_csv(filname4 ,index=False)
                    result4 = "successfully completed with {} results".format(len(twts))
                    print(result4)
                    df = pd.read_csv(filname)
                    d = dtale.show(df)
                    d.open_browser()
                    print("cccccccccccccccccccccccccc")
                    self.ids.deneme.text == "Succes."
                    self.update_lab2("Succes.")

                except:
                    print("pathway problem occurred for complex search . Please check your pathway")
                    pass
            else: #windos için
                desktop2 = desktop.replace( "Masaüstü","Desktop")
                ff = str(filname2)
                filname2 = desktop2 + "\\" + ff
                os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} lang:{}"> {}'
                          .format(tweet_count, since_date, text_query, fromuser, lang, filname2))
                # tweet_count, since_date, text_query, fromuser, lang, filname
                # (tweet_count.text, spinner.text, since_date.text, text_query.text, fromuser.text, filname.text)

                print(filname2)
                print("f222222222222222222222")
                raw_tweets = pd.read_json(filname2, lines=True, encoding='utf-8')
                # raw_tweets=tweet
                users = json_normalize(raw_tweets['user'])
                users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
                users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
                # Create DataFrame and remove duplicates
                users = pd.DataFrame(users)
                # users.drop_duplicates(subset=['userId'], inplace=True)
                # Transform 'raw_tweets' DataFrame
                # Add column for 'userId'
                user_id = [user['id'] for user in raw_tweets['user']]
                raw_tweets['userId'] = user_id
                # Remove less important columns
                cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                        'quoteCount']
                tweets = raw_tweets[cols]
                tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
                cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                        'location']
                use = users[cols]
                twts = use.merge(tweets, on='userId')
                twts.to_csv(filname2, index=False)

                # tweets_df5.to_csv(filname5 ,index=False)
                result4 = "successfully completed with {} results".format(len(twts))
                print(result4)
                dfc = pd.read_csv(filname2)
                dc = dtale.show(dfc)
                dc.open_browser()





                #
                # raw_tweets = pd.read_json(filname2, lines=True, encoding='utf-8')
                # users = json_normalize(raw_tweets['user'])
                # users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
                # users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
                # # Create DataFrame and remove duplicates
                # users = pd.DataFrame(users)
                # # users.drop_duplicates(subset=['userId'], inplace=True)
                # # Transform 'raw_tweets' DataFrame
                # # Add column for 'userId'
                # user_id = [user['id'] for user in raw_tweets['user']]
                # raw_tweets['userId'] = user_id
                # # Remove less important columns
                # cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                #         'quoteCount']
                # tweets = raw_tweets[cols]
                # tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
                # cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                #         'location']
                # use = users[cols]
                # twts = use.merge(tweets, on='userId')
                # twts.to_csv(filname2, index=False)
                # # tweets_df4.to_csv(filname4 ,index=False)
                # result4 = "successfully completed with {} results".format(len(twts))
                # print(result4)
                # df = pd.read_csv(filname2)
                # d = dtale.show(df)
                # d.open_browser()
                # print("cccccccccccccccccccccccccc")
                # self.ids.deneme.text == "Succes."
                # self.update_lab2("Succes.")
                return "a"


    # ***************  Simple Search Button Function *******************************************

    def snstw2(self, tweet_count2, since_date2, text_query2, filname4):#query
        self.tweet_count2 = tweet_count2
        self.since_date2 = since_date2
        self.text_query2 = text_query2
        self.filname4 = filname4
        filname4 = filname4 + ".csv"
        print(self.tweet_count2)
        print(self.since_date2)
        print(self.text_query2)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
        print(filname4)

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        filname5 = filname4
        if (h.startswith("/home")):

            try:
                ff=str(filname4)
                filname4=desktop+"/"+filname4
                os.system(
                    "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                        tweet_count2, since_date2, text_query2,filname4))

                raw_tweets = pd.read_json(filname4, lines=True, encoding='utf-8')
                users = json_normalize(raw_tweets['user'])
                users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
                users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
                # Create DataFrame and remove duplicates
                users = pd.DataFrame(users)
                # users.drop_duplicates(subset=['userId'], inplace=True)
                # Transform 'raw_tweets' DataFrame
                # Add column for 'userId'
                user_id = [user['id'] for user in raw_tweets['user']]
                raw_tweets['userId'] = user_id
                # Remove less important columns
                cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                        'quoteCount']
                tweets = raw_tweets[cols]
                tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
                cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                        'location']
                use = users[cols]
                twts = use.merge(tweets, on='userId')
                twts.to_csv(filname4, index=False)
                # tweets_df4.to_csv(filname4 ,index=False)
                result4="successfully completed with {} results".format(len(twts))
                print(result4)
                df = pd.read_csv(filname4)
                d = dtale.show(df)
                d.open_browser()
                print("cccccccccccccccccccccccccc")
                self.ids.deneme.text == "Succes."
                self.update_label2("Succes.")

            except:
                print("pathway problem occurred for simple search. Please check your pathway")
                pass
        else:
            desktop2 = desktop.replace("Masaüstü","Desktop")
            ff=str(filname5)
            print("-----------------------")
            print(ff)
            print(filname5)
            print("-----------------------")
            filname5=desktop2+"\\"+ff
            print("*****************************")
            print(filname5)
            print("*****************************")
            os.system(
                "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                    tweet_count2, since_date2, text_query2,filname5))
            # tweets_df5 = pd.read_json(filname5, lines=True,encoding='utf-8')

            raw_tweets = pd.read_json(filname5, lines=True, encoding='utf-8')
            # raw_tweets=tweet
            users = json_normalize(raw_tweets['user'])
            users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
            users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
            # Create DataFrame and remove duplicates
            users = pd.DataFrame(users)
            # users.drop_duplicates(subset=['userId'], inplace=True)
            # Transform 'raw_tweets' DataFrame
            # Add column for 'userId'
            user_id = [user['id'] for user in raw_tweets['user']]
            raw_tweets['userId'] = user_id
            # Remove less important columns
            cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
                    'quoteCount']
            tweets = raw_tweets[cols]
            tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
            cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
                    'location']
            use = users[cols]
            twts = use.merge(tweets, on='userId')
            twts.to_csv(filname5, index=False)

            # tweets_df5.to_csv(filname5 ,index=False)
            result5="successfully completed with {} results".format(len(twts))
            print(result5)
            df = pd.read_csv(filname5)
            d = dtale.show(df)
            d.open_browser()
        return "a"



    #******************   complex search  functions   ------------------------------------------

    def update_lab2(self, txt,filname,*args):  # eklenecek
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

    def update_lab(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            NewPageTwo.snstw(self, self.tweet_count,self.lang, self.since_date,self.until_date, self.text_query,self.fromuser, self.filname)
            self.update_lab2("Succes.",self.filname)
            # self.ids.deneme.text = "Loading..."

    def rout(self, tweet_count, lang ,since_date,until_date, text_query, fromuser, filname):  # eklenecek

        self.tweet_count = tweet_count
        self.lang=lang
        self.since_date = since_date
        self.until_date=until_date
        self.text_query = text_query
        self.fromuser = fromuser
        self.filname = filname
        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.update_lab, 0.04)



    #### *********************** simple search functions .......................................................

    def update_label2(self, txt,filname4,*args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname4=desktop+"/"+filname4+".csv"
        self.ids.deneme.text = txt
        print("-------")
        print(self.ids.deneme.text)
        print("*******")
        if (self.ids.deneme.text == "Succes."):
            print("girdi")
            self.ids.deneme.text = "finished successfully at PATH : {} ".format(filname4)
            print(self.filname4)
            self.function_interval.cancel()
        else:
            print("nanay")
            print(self.ids.deneme.text)
            self.ids.deneme.text = "finished . PATH: " + self.filname4
            print(self.filname4)
            self.function_interval.cancel()

    def update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            NewPageTwo.snstw2(self, self.tweet_count2, self.since_date2, self.text_query2, self.filname4)
            self.update_label2("Succes.",self.filname4)


    def router(self, tweet_count2, since_date2, text_query2, filname4):  # eklenecek

        self.tweet_count2 = tweet_count2
        self.since_date2 = since_date2
        self.text_query2 = text_query2
        self.filname4 = filname4

        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.update_label, 0.05)

    def finish(self, filename):  # eklenecek
        self.ids.deneme.text = "Succes. PATH:" + filename
        print(filename + "tsfgfduygd")

        return True


 
    

