from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from newsfetch.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)
from newsfetch.utils import (BeautifulSoup, Options, UserAgent,
                             get, re, sys, time,
                             webdriver)#webdriver_manager,
import csv
import random
# from django.http import HttpResponse
from selenium import webdriver
import json
from fake_useragent import UserAgent

from kivy.clock import Clock


import time
from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time
import numpy as np

from pycode.google import google_search
from pycode.google10 import Google_Search10
import pandas as pd
import dtale
import csv
import requests
from newsplease import *
from newsplease import NewsPlease
import webbrowser
from newspaper import Article


class GoogleSearch(Screen):
        
    def open_page(self):
        webbrowser.open('html_files\\google_search.html')
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'search_engine'
        self.manager.get_screen('login').resetForm()
    
    def run(self,key,n_name,date1,date2,fname):
        self.function_interval = Clock.schedule_interval(self.searchgoogle_update_label, 0.05)
        self.fname = fname
        self.key=key
        self.filname4 = self.fname + ".csv"
        self.date1 = date1
        self.date2 = date2
        self.n_name = n_name
        self.url_links=[]
        self.os_send=""
        dat1 = self.date1.split(',')
        dat2 = self.date2.split(',')
        print(self.date1)
        print(self.date2)

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
            fnames = desktop + "/" + fname + '.csv'
            fnames2 = desktop + "/" + fname + '_content.csv'
            fnamesw=desktop + "\\" + fname + '.csv'
            fnames2w = desktop + "\\" + fname + '_content.csv'

            ff = str(self.filname4)
            filname44 = desktop + "/" + ff
            way = filname44
            print("filname4 = {}".format(filname44))
            print(fnames)

        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        filname5 = self.filname4
        if (h.startswith("/home")):
            self.os_send = "/usr/bin/chromedriver"



            for da1, da2 in zip(dat1,dat2):
                non = 0
                da1 = da1.strip()
                d1=da1
                da2 = da2.strip()
                d2=da2

                print(d1)
                print(d2)
                google = Google_Search10(self.key, n_name, fnames, d1, d2,self.os_send)

                try:
                    for i in google.urls:
                        non += 1
                        self.url_links.append(i)
                except AttributeError:
                    pass

            for i in self.url_links:
                i = str(i.strip())
                # article = NewsPlease.from_url(i)
                article = Article(i)
                article.download()
                try:
                    article.parse()
                except:
                    continue

                # fieldnames = ['url', 'date', 'title', 'content']
                a = article.url
                try:
                    b = article.publish_date
                except:
                    b = "None"
                try:
                    c = article.title
                    print(c)
                except:
                    c = "None"
                try:
                    d = article.text
                    dd = " ".join(d.split())
                except:
                    dd = "None"
                sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ')
                    csvwriter.writerow([sent_line])
                #     for lin in linky:
                #         csvwriter.writerow([lin])
                #         print("sssssssss")
                print("close csv")
            # for i in self.url_links:
            #     i = str(i)
            #
            #
            #     try:
            #         article = NewsPlease.from_url(i.strip())
            #         a = article.url
            #     except:
            #         a = "None"
            #     try:
            #         b = article.date_publish
            #     except:
            #         b = "None"
            #     try:
            #         c = article.title
            #         print(c)
            #     except:
            #         c = "None"
            #     try:
            #         d = article.maintext
            #         dd = " ".join(d.split())
            #     except:
            #         dd = "None"
            #     if (a == 'None'):
            #         pass
            #     else:
            #         sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
            #         with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
            #             csvwriter = csv.writer(csvfile, delimiter=' ')
            #             csvwriter.writerow([sent_line])
            #
            #         print("close csv")

            newspaper_result = "succesfully completed try another search"
            print(newspaper_result)
            df = pd.read_csv(fnames2)
            d = dtale.show(df)
            d.open_browser()


        else:
            self.os_send = "C:\\"
            for da1, da2 in zip(dat1, dat2):
                non = 0
                da1 = da1.strip()
                d1 = da1


                da2 = da2.strip()

                d2 = da2


                print(d1)
                print(d2)
                google = Google_Search10(self.key, n_name, fnamesw, d1, d2)
                # google = google_bypass(vord, ngnum2, fnames, d1, d2)
                try:
                    for i in google.urls:
                        non += 1
                        self.url_links.append(i)
                except AttributeError:
                    pass

            for i in self.url_links:
                i = str(i.strip())
                # article = NewsPlease.from_url(i)
                article = Article(i)
                article.download()
                try:
                    article.parse()
                except:
                    continue

                # fieldnames = ['url', 'date', 'title', 'content']
                a = article.url
                try:
                    b = article.publish_date
                except:
                    b = "None"
                try:
                    c = article.title
                    print(c)
                except:
                    c = "None"
                try:
                    d = article.text
                    dd = " ".join(d.split())
                except:
                    dd = "None"
                sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                with open(fnames2w, 'a', encoding='UTF8', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ')
                    csvwriter.writerow([sent_line])
                #     for lin in linky:
                #         csvwriter.writerow([lin])
                #         print("sssssssss")
                print("close csv")
            # for i in self.url_links:
            #     i = str(i)
            #
            #     # fieldnames = ['url', 'date', 'title', 'content']
            #     try:
            #         article = NewsPlease.from_url(i.strip())
            #         a = article.url
            #     except:
            #         a = "None"
            #     try:
            #         b = article.date_publish
            #     except:
            #         b = "None"
            #     try:
            #         c = article.title
            #         print(c)
            #     except:
            #         c = "None"
            #     try:
            #         d = article.maintext
            #         dd = " ".join(d.split())
            #     except:
            #         dd = "None"
            #     if (a == 'None'):
            #         pass
            #     else:
            #         sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
            #         with open(fnames2w, 'a', encoding='UTF8', newline='') as csvfile:
            #             csvwriter = csv.writer(csvfile, delimiter=' ')
            #             csvwriter.writerow([sent_line])
            #         #     for lin in linky:
            #         #         csvwriter.writerow([lin])
            #         #         print("sssssssss")
            #         print("close csv")


            newspaper_result = "succesfully completed try another search"
            print(newspaper_result)
            print(fnames2w)
            print("***********************")
            print(fnames2)
            df = pd.read_csv(fnames2w)
            d = dtale.show(df)
            d.open_browser()

    def searchgoogle_update_label2(self, txt, filname4, *args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname4 = desktop + "/" + filname4 + ".csv"
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

    def searchgoogle_update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            GoogleSearch.run(self, self.keyword,self.n_name, self.d1, self.d2, self.fname)
            self.searchgoogle_update_label2("Succes.", self.filname4)

    def searchgoogle_router(self, keyword,n_name, d1, d2, fname):
        self.keyword = keyword
        self.d1 = d1
        self.d2 = d2
        self.fname = fname
        self.n_name=n_name

        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.searchgoogle_update_label, 0.05)
