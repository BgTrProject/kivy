from django.shortcuts import render,HttpResponse
from credentials import *
import os
import tweepy as tw
import pandas as pd
import snscrape.modules.twitter as sntwitter




from django.http import HttpResponse

import csv
from templates import *
from tweepy import *
import tweepy
# from django.shortcuts import render

userID = "realDonaldTrump"
# auth=OAuth1UserHandler()
consumer_key="JglqaxdDIbqZb9NJTuCaL12Gc"
consumer_secret="t8qfyoaJkKbMjn9ihJ2TYKV0hYEefenSFLpab3S8HjyD2x6nHm"
access_token="1493319270-e4PxEbZxUQqy6tppWpwHvWW9aFJWiUxcuIVvuPt"
access_token_secret="cXS8sXl3TPcmSTI6xD9wcFiz8yp70Tp16W1z9ocS7WYyt"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
api.search_tweets

def home_view(request):
    data=request.POST.get('name')
    return render(request,'twhome.html',{'data':data})

def autho(request):
    key = request.GET.get("key")
    secret = request.GET.get("secret")
    atoken = request.GET.get("atoken")
    asecret = request.GET.get("asecret")

    if key != None and secret != None:
        login = OAuth1UserHandler(key, secret,atoken, asecret)
        auth=login
        print(auth)
        # api = tw.API(auth.get_authorization_url())
        # print(api)

        result = "You access your Authorization"
    else:
        pass
    return render(request, 'twhome.html', {"result": result})

api=tweepy.API(auth)
print(api)

def searctw(request):
    sword  = request.GET.get("sword")
    langu = request.GET.get("langu")
    sinctw = request.GET.get("sinctw")
    tweets = api.search_tweets(q=sword)
    tt=[]
    for t in tweets:
        txt=t.text
        txt=str(txt)
        if txt.count("LONGED")==1 or txt.count("SHORTED")==1:
            txt2=str(txt)
            h=txt2.split(' ')
            print(h[0:6])

        else:
            pass
    result2="ok "

    return render(request, 'twhome.html', {"result2": result2})



def snstw(request):#collect
    tweet_count=request.GET.get("tweet_count")
    since_date=request.GET.get("since_date")
    text_query=request.GET.get("text_query")
    fromuser = request.GET.get("fromuser")
    until_date=request.GET.get("until_date")
    lang=request.GET.get("lang")
    near=request.GET.get("near")
    filname=request.GET.get("filname")
    ff=str(filname)
    os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} from:{} until:{} lang:{}"> '
              'text-query-tweets2.json'.format(tweet_count, since_date, text_query, fromuser, until_date, lang))
    tweets_df2 = pd.read_json('text-query-tweets2.json', lines=True)
    result3="successfully completed with {} results".format(len(tweets_df2))
    return render(request, 'twhome.html', {"result3": result3})







def q_snstw(request):#query
    tweet_count2=request.GET.get("tweet_count2")
    since_date2=request.GET.get("since_date2")
    text_query2=request.GET.get("text_query2")
    filname4=request.GET.get("filname4")
    ff=str(filname4)
    os.system(
        "snscrape --jsonl --progress --max-results {} --since {} twitter-search '{}'> {}".format(
            tweet_count2, since_date2, text_query2,filname4))
    tweets_df4 = pd.read_json(filname4, lines=True,encoding='utf-8')
    result4="successfully completed with {} results".format(len(tweets_df4))
    return render(request, 'twhome.html', {"result4": result4})
