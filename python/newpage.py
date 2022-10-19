from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

import dtale
import sqlite3 as lite

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty

from credentials import *
import os
import webbrowser
import tweepy as tw
import pandas as pd
# import dtale
from pandas.io.json import json_normalize

import csv
import time

from tweepy import *
import tweepy
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from pandas.io.json import json_normalize
import warnings

from kivy.clock import Clock

class NewPage(Screen):
    search_for_tooltip = ObjectProperty(opacity=0)
    language_tooltip = ObjectProperty(None)
    filename_tooltip = ObjectProperty(None)
    maxresult_tooltip = ObjectProperty(None)
    geo_code_tooltip = ObjectProperty(None)

    search_for_label = ObjectProperty(None)
    search_for_textinput = ObjectProperty(None)

    language_label = ObjectProperty(None)
    spinner = ObjectProperty(None)

    filename_label = ObjectProperty(None)
    filname_text_input = ObjectProperty(None)

    max_result_label = ObjectProperty(None)
    max_result_text_input = ObjectProperty(None)

    fuct_one_button = ObjectProperty(opacity=0)
    fuct_two_button = ObjectProperty(None)
    fuct_three_button = ObjectProperty(None)

    geo_code_label = ObjectProperty(None)
    geo_code_text_input = ObjectProperty(None)





    ## *****Dropdown function **********
    ll = ""
    def build(self):

        return self
    def on_spinner_select(self, ll):
        print(ll)
        ll = ll
        print("kkkkkkkkkkkkkkkkkkkkkkk")
        print(ll)
        print("kkkkkkkkkkkkkkkkkkkkkkk")
        return self.ll

    # **********page arrangement function --------------------------
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'social_media'
        self.manager.get_screen('login').resetForm()
    
    def disconnect2(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('login').resetForm()
    
    def open_page(self):
        
        webbrowser.open('html_files\\newpage.html')

#---------popup click function--------------------------
    def search_for_web(self):
        webbrowser.open('https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query')
    def language_web(self):
        webbrowser.open("https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages")





    ############# Tweepy Search Button Function *************************
    def autho(self,key,secret,atoken,asecret,sword,langu,max_result,filname):
        self.key=key
        self.secret=secret
        self.atoken=atoken
        self.asecret=asecret
        self.sword=sword
        self.langu=langu
        # self.since=since
        self.max_result=max_result
        self.filname = filname
        filname = filname + ".csv"
        print("***************************")
        print(self,max_result,self.key)
        print("***************************")


        auth = tw.OAuthHandler(self.key, self.secret)
        auth.set_access_token(self.atoken, self.asecret)
        # api = tw.API(auth, wait_on_rate_limit=True)
        api = tw.API(auth, wait_on_rate_limit=True, parser=tw.parsers.JSONParser())

        # auth = tw.OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_token, access_token_secret)

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h=os.getcwd()
        filname2 = filname
        header = ["user_id", "user_name", "text", "tweet_id", "created_at", "language"]
        if(h.startswith("/home")):
            try:
                ff = str(filname)
                filname = desktop + "/" + filname
                print("aaaaaaaaaaaa")
                print(sword)
                print(self.sword)
                print("???????????????????????????")
                print(filname)
                print(self.max_result)
                print(self.langu)
                print(self.sword)
                print(self.asecret)
                print(filname2)
                tweets = api.search_tweets(q=self.sword, lang=self.langu, count=self.max_result)
                print("sssssssssssssssssssssssssssssssssssss")
                d = pd.DataFrame(tweets['statuses'])
                y = pd.json_normalize(d.user)
                print("????????????*****************????????????")
                print(filname)
                print("111111111111111111111111111111111111111111111")
                print("????????????*****************????????????")
                y.to_csv(filname, index=False)
                df = pd.read_csv(filname)
                ddf = dtale.show(df)
                ddf.open_browser()
                #
                # top_trends = api.get_place_trends(self.max_result_3)
                # d_33_ = pd.json_normalize(top_trends[0]['trends'])
                # d_33_.to_csv(self.filname_33, index=False)
                # df_33 = pd.read_csv(filname_33)





                # with open(filname, 'w', encoding='UTF-8') as csvfile:
                #     print("**********file opened ************************************************")
                #     csvwriter = csv.writer(csvfile, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
                #     csvwriter.writerow(header)
                #
                # for tweet in api.search_tweets(q=sword, lang=langu, payload_type="json"): #,since_id=since,max_id=max_result
                #     print("bbbbbbbbbbbbb")
                #     # print(tweet.entities)
                #     print(f"{tweet.text}")
                #     #     # j=json.dump(tweet)
                #     #     # with open("bbbbb.json" ,"w") as f:
                #     #     #     # f.write(j)
                #     a = f"{tweet.user.name}"
                #     b = f"{tweet.user.id}"
                #     c = f"{tweet.text}"
                #     d = f"{tweet.id}"
                #     e = f"{tweet.created_at}"
                #     f = f"{tweet.lang}"
                #     print(a)
                #     print(b)
                #     print(c)
                #     print(d)
                #     print(e)
                #     print(f)
                #     print("--------------------------")
                #     data=[b,a,c,d,e,f]
                #     print(data)
                #     with open(filname, 'a',encoding='UTF-8') as csvfile:
                #         print("**********file written ************************************************")
                #         csvwriter = csv.writer(csvfile, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
                #         csvwriter.writerow(data)
                # print("******")
                # print(filname)
                # print(filname2)
                # print("******")
                # df = pd.read_csv(filname)
                # d = dtale.show(df)
                # d.open_browser()
                # print("ssssonnnnnnnnn")

            except:
                pass
        else:
            print("----------------------except blogğuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu-------")
            desktop2 = desktop.replace( "Masaüstü","Desktop")
            ff = str(filname2)
            filname2 = desktop2 + "\\" + ff
            auth = tw.OAuthHandler(key, secret)
            auth.set_access_token(atoken, asecret)
            api = tw.API(auth, wait_on_rate_limit=True)
            tweets = api.search_tweets(q=self.sword, lang=self.langu, count=self.max_result)
            d2 = pd.DataFrame(tweets['statuses'])
            y2 = pd.json_normalize(d2.user)
            y2.to_csv(filname2, index=False)
            df2 = pd.read_csv(filname2)
            ddf2 = dtale.show(df2)
            ddf2.open_browser()



            # with open(filname2, 'w',encoding='UTF-8') as csvfile:
            #     print("**********file opened ************************************************")
            #     csvwriter = csv.writer(csvfile, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
            #     csvwriter.writerow(header)
            #
            # for tweet in api.search_tweets(q=sword, lang=langu,since_id=since,max_id=max_result ,payload_type="json"):
            #     # print(tweet.entities)
            #     print(f"{tweet.text}")
            #     #     # j=json.dump(tweet)
            #     #     # with open("bbbbb.json" ,"w") as f:
            #     #     #     # f.write(j)
            #     a = f"{tweet.user.name}"
            #     b = f"{tweet.user.id}"
            #     c = f"{tweet.text}"
            #     d = f"{tweet.id}"
            #     e = f"{tweet.created_at}"
            #     f = f"{tweet.lang}"
            #     # print(a)
            #     # print(b)
            #     # print(c)
            #     # print(d)
            #     # print(e)
            #     # print(f)
            #     # print("--------------------------")
            #     data2 = [b, a, c, d, e, f]
            #     with open(filname2,'a',encoding='UTF-8') as csvfile:
            #         print("**********file written ************************************************")
            #         csvwriter = csv.writer(csvfile, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
            #         csvwriter.writerow(data2)
            # df = pd.read_csv(filname2)
            # d = dtale.show(df)
            # d.open_browser()

#************* tweepy search -------------------------------*****
    def fuction_one_button_work(self, key, secret, atoken, asecret, sword, langu, max_result,filname):  # eklenecek

        self.key = key
        self.secret = secret
        self.atoken = atoken
        self.asecret = asecret
        self.sword = sword
        self.langu = langu
        # self.since = since
        self.max_result = max_result
        self.filname = filname
        self.ids.deneme.text = "Loading search results..."
        self.function_interval = Clock.schedule_interval(self.update_label3, 0.05)


    def update_label4(self, txt,filname,*args):  # eklenecek
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            filname=desktop+"/"+filname+".csv"
            self.ids.deneme.text = txt
            print("-------")
            print(self.ids.deneme.text)
            print("*******")
            if (self.ids.deneme.text == "Succes."):
                print("start")
                self.ids.deneme.text = "finished successfully at PATH : {} ".format(filname)
                print(self.filname)
                self.function_interval.cancel()
            else:
                print("wrong pathway ")
                print(self.ids.deneme.text)
                self.ids.deneme.text = "finished . PATH: " + self.filname
                print(self.filname)
                self.function_interval.cancel()

    def update_label3(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading search results..."):
            print("started")
            self.function_interval.cancel()
            NewPage.autho(self,self.key,self.secret,self.atoken,self.asecret,self.sword,self.langu,self.max_result,self.filname)
            self.update_label4("Succes.",self.filname)
        else:
            pass

################     2   **************************

    def autho2(self,key,secret,atoken,asecret,max_result_2,filname_2):
        self.key=key
        self.secret=secret
        self.atoken=atoken
        self.asecret=asecret
        # self.sword_2=sword_2
        # self.langu=langu
        # self.since=since
        self.max_result_2=max_result_2
        self.filname_2 = filname_2
        filname_2 = filname_2 + ".csv"
        print("***************************")
        print(max_result_2,self.key)
        print("22222222222222222222222222222222222222222222222222222222222")
        print("***************************")


        auth = tw.OAuthHandler(self.key, self.secret)
        auth.set_access_token(self.atoken, self.asecret)
        # api = tw.API(auth, wait_on_rate_limit=True)
        api = tw.API(auth, wait_on_rate_limit=True, parser=tw.parsers.JSONParser())

        # auth = tw.OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_token, access_token_secret)

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h=os.getcwd()
        filname_22 = filname_2
        header = ["user_id", "user_name", "text", "tweet_id", "created_at", "language"]
        if(h.startswith("/home")):
            try:
                ff = str(filname_2)
                filname_2 = desktop + "/" + filname_2
                print("aaaaaaaaaaaa")

                print("????????????  222222222222222222222  ???????????????")
                print(filname_2)
                print(filname_22)
                print(self.asecret)
                print(self.max_result_2)
                print("????????????  222222222222222222222  ???????????????")
                print("22222222222222222222222222222222222222222222222222222222222")
                d2=list(tw.Cursor(api.home_timeline).items(self.max_result_2))
                d3=pd.DataFrame(d2)
                y2=pd.json_normalize(d3.user)
                print(y2)
                y2.to_csv(filname_2,index=False)
                df_2 = pd.read_csv(filname_2)
                d2_df = dtale.show(df_2)
                d2_df.open_browser()



            except:
                pass
        else:
            try:
                ff = str(filname_2)
                filname_22 = desktop + "//" + filname_22
                print("aaaaaaaaaaaa")

                print("???????????????????????????")
                print(filname_2)
                print(filname_22)
                d2 = list(tw.Cursor(api.home_timeline).items(self.max_result_2))
                d3 = pd.DataFrame(d2)
                y2 = pd.json_normalize(d3.user)
                y2.to_csv(filname_22, index=False)
                df_22 = pd.read_csv(filname_22)
                d22_df = dtale.show(df_22)
                d22_df.open_browser()


            except:
                pass

    ###############################
    def fuction_two_button_work(self, key, secret, atoken, asecret,max_result_2b, filname_2b):  # eklenecek

        self.key = key
        self.secret = secret
        self.atoken = atoken
        self.asecret = asecret

        self.max_result_2b = max_result_2b
        self.filname_2b = filname_2b
        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.update_label3b, 0.05)

    def update_label4b(self, txt, filname_2b, *args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname_2b = desktop + "/" + filname_2b + ".csv"
        self.ids.deneme.text = txt
        print("-------")
        print(self.ids.deneme.text)
        print("*******")
        if (self.ids.deneme.text == "Succes."):
            print("start")
            self.ids.deneme.text = "finished successfully at PATH : {} ".format(filname_2b)
            print(self.filname_2b)
            self.function_interval.cancel()
        else:
            print("wrong pathway ")
            print(self.ids.deneme.text)
            self.ids.deneme.text = "finished . PATH: " + self.filname_2b
            print(self.filname_2b)
            self.function_interval.cancel()

    def update_label3b(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("started")
            self.function_interval.cancel()
            NewPage.autho2(self, self.key, self.secret, self.atoken, self.asecret,
                          self.max_result_2b, self.filname_2b)
            self.update_label4b("Succes.", self.filname_2b)
        else:
            pass





####################              3       ******************

    def autho3(self, key, secret, atoken, asecret, max_result_3, filname_3):
        self.key = key
        self.secret = secret
        self.atoken = atoken
        self.asecret = asecret
        # self.sword=sword
        # self.langu=langu
        # self.since=since
        self.max_result_3 = max_result_3
        self.filname_3 = filname_3
        filname_3 = filname_3 + ".csv"
        print("***************************")
        print(max_result_3, self.key)
        print("***************************")

        auth = tw.OAuthHandler(self.key, self.secret)
        auth.set_access_token(self.atoken, self.asecret)
        # api = tw.API(auth, wait_on_rate_limit=True)
        api = tw.API(auth, wait_on_rate_limit=True, parser=tw.parsers.JSONParser())

        # auth = tw.OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_token, access_token_secret)

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        filname_33 = filname_3
        header = ["user_id", "user_name", "text", "tweet_id", "created_at", "language"]
        if (h.startswith("/home")):
            try:
                ff = str(filname_3)
                filname_3 = desktop + "/" + filname_3
                print("aaaaaaaaaaaa")

                print("3333333333333333333333333333333333333333333333333")
                print(filname_3)
                print(filname_33)
                print(self.max_result_3)
                print("befofffffffffffffer3333333333333333333333333333333333")

                top_trends = api.get_place_trends(self.max_result_3)
                d_3_ = pd.json_normalize(top_trends[0]['trends'])
                print("tooooooooooo csv 3333333")


                # d_3 = list(tw.Cursor(api.home_timeline).items(self.max_result_3))
                # d_3_ = pd.DataFrame(d_3)
                # y3 = pd.json_normalize(d_3_.user)
                d_3_.to_csv(filname_3, index=False)
                df_3 = pd.read_csv(filname_3)
                d3_df = dtale.show(df_3)
                d3_df.open_browser()



            except:
                pass
        else:
            try:
                ff = str(filname_3)
                filname_33 = desktop + "//" + filname_33
                print("aaaaaaaaaaaa")

                print("???????????????????????????")

                print(filname_33)

                top_trends = api.get_place_trends(self.max_result_3)
                d_33_ = pd.json_normalize(top_trends[0]['trends'])

                # d_33 = list(tw.Cursor(api.home_timeline).items(self.max_result_2))
                # d_33_ = pd.DataFrame(d_33)
                # y33 = pd.json_normalize(d_33_.user)
                d_33_.to_csv(filname_33, index=False)
                df_33 = pd.read_csv(filname_33)
                d33_df = dtale.show(df_33)
                d33_df.open_browser()


            except:
                pass
    #########################################33
    def fuction_three_button_work(self, key, secret, atoken, asecret, max_result_3b, filname_3b):  # eklenecek

        self.key = key
        self.secret = secret
        self.atoken = atoken
        self.asecret = asecret

        self.max_result_3b = max_result_3b
        self.filname_3b = filname_3b
        self.ids.deneme.text = "Loading place trends..."
        self.function_interval = Clock.schedule_interval(self.update_label3c, 0.05)

    def update_label4c(self, txt, filname_3b, *args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname_3b = desktop + "/" + filname_3b + ".csv"
        self.ids.deneme.text = txt
        print("-------")
        print(self.ids.deneme.text)
        print("*******")
        if (self.ids.deneme.text == "Succes."):
            print("start")
            self.ids.deneme.text = "finished successfully at PATH : {} ".format(filname_3b)
            print(self.filname_3b)
            self.function_interval.cancel()
        else:
            print("wrong pathway ")
            print(self.ids.deneme.text)
            self.ids.deneme.text = "finished . PATH: " + self.filname_3b
            print(self.filname_3b)
            self.function_interval.cancel()

    def update_label3c(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading place trends..."):
            print("started")
            self.function_interval.cancel()
            NewPage.autho3(self, self.key, self.secret, self.atoken, self.asecret,
                           self.max_result_3b, self.filname_3b)
            self.update_label4c("Succes.", self.filname_3b)
        else:
            pass


            # print("----------------------except blogğuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu-------")
            # desktop2 = desktop.replace("Desktop", "Masaüstü")
            # ff = str(filname_22)
            # filname_22 = desktop2 + "//" + filname_22
            # auth = tw.OAuthHandler(key, secret)
            # auth.set_access_token(atoken, asecret)
            # api = tw.API(auth, wait_on_rate_limit=True)
            # with open(filname_22, 'w',encoding='UTF-8') as csvfile:
            #     print("**********file opened ************************************************")
            #     csvwriter = csv.writer(csvfile, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
            #     csvwriter.writerow(header)

            # for tweet in api.search_tweets(q=sword, lang=langu,since_id=since,max_id=max_result ,payload_type="json"):
            #     # print(tweet.entities)
            #     print(f"{tweet.text}")
            #     #     # j=json.dump(tweet)
            #     #     # with open("bbbbb.json" ,"w") as f:
            #     #     #     # f.write(j)
            #     a = f"{tweet.user.name}"
            #     b = f"{tweet.user.id}"
            #     c = f"{tweet.text}"
            #     d = f"{tweet.id}"
            #     e = f"{tweet.created_at}"
            #     f = f"{tweet.lang}"
            #     # print(a)
            #     # print(b)
            #     # print(c)
            #     # print(d)
            #     # print(e)
            #     # print(f)
            #     # print("--------------------------")
            #     data2 = [b, a, c, d, e, f]
            #     with open(filname2,'a',encoding='UTF-8') as csvfile:
            #         print("**********file written ************************************************")
            #         csvwriter = csv.writer(csvfile, delimiter=';')  # , quotechar='|', quoting=csv.QUOTE_MINIMAL
            #         csvwriter.writerow(data2)
            # df = pd.read_csv(filname2)
            # d = dtale.show(df)
            # d.open_browser()






        
        # tweets = api.search_tweets(q=sword)
        # tt=[]
        # for t in tweets:
        #     txt=t.text
        #     txt=str(txt)
        #     if txt.count("LONGED")==1 or txt.count("SHORTED")==1:
        #         txt2=str(txt)
        #         h=txt2.split(' ')
        #         print(h[0:6])
        #     else:
        #         pass
        # result2="ok "

class P2(FloatLayout):
    pass
def show_popup():
    pass
    # webbrowser.open('howto.html')
    # show = P2()
    # popupWindow = Popup(title="Press on the screen to turn it off!",title_size=17,content=show,size_hint =(None, None),size=(400,400))
    # popupWindow.open()