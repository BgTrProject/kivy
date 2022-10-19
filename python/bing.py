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


from pycode.bing_s import *
# from pycode.bing_sm import *
# from pycode.bing import *
from pycode.bing_son import BingSon
import pandas as pd
import dtale
import csv
import requests
from newsplease import *
from newsplease import NewsPlease
import webbrowser



class Bing(Screen):
    def run(self,key,n_name,fnam):
        self.function_interval = Clock.schedule_interval(self.bing_update_label, 0.05)
        self.fnam = fnam
        self.key=key
        # self.filname4 = self.fnam + ".csv"
        # self.date1 = date1
        # self.date2 = date2
        self.n_name = n_name
        self.url_links=[]
        # print("=?=?=?=?=?=?=?=?=?=?=?=")
        # print(fnam)
        # print("=?=?=?=?=?=?=?=?=?=?=?=")
        # desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        # ff = str(self.fnam)
        # self.fname = desktop + '/' + ff
        # self.link_filname = self.filname + "_link_bing.txt"

        # desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        # print(desktop)
        # way = "{}{}{}/".format(desktop, "/", fnam)
        # print(way)

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
            self.fnames = desktop + "/" + fnam + '_bing.txt'
            self.fnames2 = desktop + "/" + fnam + '_content_bing.csv'
            self.fnamesw = desktop + "\\" + fnam + '_bing.txt'
            self.fnames2w = desktop + "\\" + fnam + '_content_bing.csv'

            # ff = str(self.filname4)
            # filname44 = desktop + "/" + ff
            # self.way = filname44
            # print("filname4 = {}".format(filname44))
            print("=?=?=?=?=?=?=?=?=?=?=?=_____________-")
            print(self.fnames)
            print(self.fnames2)
            print("=?=?=?=?=?=?=?=?=?=?=?=??????????????????")

        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        # filname5 = self.filname4
        if (h.startswith("/home")):
            bing_search = BingS(self.key, self.n_name, self.fnames)
            bing_search.crawl_all()
            # bing_search = BingSon("2019-02-01","2019-05-30",self.key, self.n_name, fnam,50)
            # bing_search.main()
            # self.url_links=bingsearch.crawl_all()
            bing_result = "Bing search completed successfully...wait for article content"
            print(bing_result)
            self.get_article_linux(self.fnames,self.fnames2)

            # fnames="/home/bilgi/Desktop/zzzzzzzzzz.txt"



        else:
            bingsearch = Bing(self.key, self.n_name, self.fnamesw)
            bingsearch.crawl_all()
            bing_result = "Bing search completed successfully...wait for article content"
            print(bing_result)
            self.get_article_windows(self.fnamesw,self.fnames2w)


    def get_article_linux(self,filname,filname2):

        with open(filname, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                i = i.strip("\n")
                # print(i)
                self.url_links.append(i)

        for i in self.url_links:
            i = str(i)
            print("llllllllllllllllllllllllllll")
            print(i)
            print("llllllllllllllllllllllllllll")

            # fieldnames = ['url', 'date', 'title', 'content']
            try:
                article = NewsPlease.from_url(i.strip())
                a = article.url
            except:
                a = "None"
            try:
                b = article.date_publish
            except:
                b = "None"
            try:
                c = article.title
                print(c)
            except:
                c = "None"
            try:
                d = article.maintext
                dd = " ".join(d.split())
            except:
                dd = "None"
            if (a == 'None'):
                pass
            else:
                sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                with open(filname2, 'a', encoding='UTF8', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ')
                    csvwriter.writerow([sent_line])
                #     for lin in linky:
                #         csvwriter.writerow([lin])
                #         print("sssssssss")
                print("close csv")

        newspaper_result = "succesfully completed try another search"
        print(newspaper_result)
        df = pd.read_csv(filname2)
        d = dtale.show(df)
        d.open_browser()


    def get_article_windows(self,filnamew,filname2w):
        with open(filnamew, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                i = i.strip("\n")
                # print(i)
                self.url_links.append(i)

        for i in self.url_links:
            i = str(i)
            print("llllllllllllllllllllllllllll")
            print(i)
            print("llllllllllllllllllllllllllll")

            # fieldnames = ['url', 'date', 'title', 'content']
            try:
                article = NewsPlease.from_url(i.strip())
                a = article.url
            except:
                a = "None"
            try:
                b = article.date_publish
            except:
                b = "None"
            try:
                c = article.title
                print(c)
            except:
                c = "None"
            try:
                d = article.maintext
                dd = " ".join(d.split())
            except:
                dd = "None"
            if (a == 'None'):
                pass
            else:
                sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                with open(filname2w, 'a', encoding='UTF8', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ')
                    csvwriter.writerow([sent_line])
                #     for lin in linky:
                #         csvwriter.writerow([lin])
                #         print("sssssssss")
                print("close csv")

        newspaper_result = "succesfully completed try another search"
        print(newspaper_result)
        df = pd.read_csv(filname2w)
        d = dtale.show(df)
        d.open_browser()

    def bing_update_label2(self, txt, filname4, *args):  # eklenecek
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

    def bing_update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            Bing.run(self,self.keyword,self.n_name, self.fname)
            self.bing_update_label2("Succes.", self.filname4)

    def bing_router(self, keyword,n_name,fname):
        self.keyword = keyword
        self.fname = fname
        self.n_name=n_name

        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.bing_update_label, 0.05)

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'search_engine'
        self.manager.get_screen('login').resetForm()
    def open_page(self):
        webbrowser.open('html_files\\bing.html')