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

import csv
from templates import *
from tweepy import *
import tweepy



class TweetQuery(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()
        
    def q_snstw(self, tweet_count2, since_date2, text_query2, filname4,userID,consumer_key,consumer_secret,access_token,access_token_secret):#query
        TweetQuery.deneme(userID,consumer_key,consumer_secret,access_token,access_token_secret)
        self.tweet_count2 = tweet_count2
        self.since_date2 = since_date2
        self.text_query2 = text_query2
        self.filname4 = filname4
        print(self.tweet_count2)
        print(self.since_date2)
        print(self.text_query2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        print(self.filname4)
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        filname5 = filname4
        
        
        try:
            ff=str(filname4)
            filname4=desktop+"\\"+filname4
            os.system(
                "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                    tweet_count2, since_date2, text_query2,filname4))
            # tweets_df4 = pd.read_json(filname4, lines=True,encoding='utf-8')
            warnings.filterwarnings("ignore")
            raw_tweets = pd.read_json(filname4, lines=True, encoding='utf-8')
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
            twts.to_csv(filname4)

            result4="successfully completed with {} results".format(len(twts))
            print(result4)
        except:
            desktop2 = desktop.replace("Desktop","Masaüstü")
            ff=str(filname5)
            filname5=desktop2+"\\"+filname5
            os.system(
                "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
                    tweet_count2, since_date2, text_query2,filname5))
            # tweets_df5 = pd.read_json(filname5, lines=True,encoding='utf-8')
            warnings.filterwarnings("ignore")
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
            twts.to_csv(filname5)
            result5="successfully completed with {} results".format(len(twts))
            print(result5)
        return "a"
    
    def deneme (userID,consumer_key,consumer_secret,access_token,access_token_secret):
        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        api.search_tweets
        print("Successfully")
