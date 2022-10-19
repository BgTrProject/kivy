from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os


import csv
import dtale
import pandas as pd

import time
from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time
import numpy as np

import requests

from kivy.properties import StringProperty
import webbrowser
from kivy.clock import Clock
from codes.vatan import *
from codes.dailySabah import *
from codes.dailyHurriyet import *
from codes.haberler import *
from codes.turkiyeGazetesi import *
from codes.takvim import *
from codes.sabah import *


class News_Search(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'news'
        self.manager.get_screen('login').resetForm()

    def open_page(self):

        webbrowser.open('html_files\\news_date_search.html')

    def run(self, cat, n_name, fname):
        self.os_send=""
        self.function_interval = Clock.schedule_interval(self.n_update_label, 0.05)
        self.fname = fname
        self.filname4 = self.fname + ".txt"
        self.cat = cat
        self.n_name = n_name
        self.os_send=""

        fn = []
        link_list = []
        content_list = []
        file_list = []

        # cl = cl_names_all.split(",")
        cl = n_name.split(",")

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        self.fnames = desktop + "/" + fname + '_content.csv'
        filname5 = self.filname4
        if (h.startswith("/home")):  ## linux için
            self.os_send = "/usr/bin/chromedriver"

            try:
                ff = str(self.filname4)
                filname44 = desktop + "/" + self.filname4
                way = filname44
                print("filname4 = {}".format(filname44))

                for i in cl:
                    h_link = "{}{}_{}_link.txt".format(fname, fname, i)  #way değiştirildi fname yapıldı 1.parametre
                    h_content = "{}{}_{}_content.txt".format(fname, fname, i)
                    link_list.append(h_link)
                    content_list.append(h_content)

                    file_list.append(h_link)
                    file_list.append(h_content)

                    h = "{}".format(i.strip())
                    print(h)
                    print("--------hhhhhhh ---------------")
                    fn.append(h)
                ss = []

                for i in range(len(cl)):
                    print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
                    print(i)

                    ii = '{}={}("{}","{}","{}","{}")'.format(cl[i], cl[i],  self.cat, fn[i],fname,self.os_send)
                    print(ii)
                    print("zzzzzzzzzzzzzzzzzzzzzzzz")
                    ss.append(ii)
                zeta = []
                sayac = 0
                for i in ss:
                    print(i)
                    print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
                    exec(i)
                    d_link = "{}".format(link_list[sayac])
                    print("---------------------------------- dlink---------")
                    print(d_link)
                    print("???????????????????????")

                    z = i.split("=")
                    print(z)
                    zet = "{}{}".format(z[0], ".main()")
                    zeta.append(zet)
                    print("zeeeeeeeeeeettttttttttt")
                    print(zet)
                    exec(zet)
                    d_content = ("{}".format(content_list[sayac]))
                    print(" ***************** d_content ****************")
                    print(d_content)
                    print(" ***************** d_content ****************")
                    # zipped_file = zipFiles(d_content)
                    # download_file_g(d_content)
                    sayac += 1

                newspaper_result = "succesfully completed try another search"
                print(newspaper_result)

                df = pd.read_csv(self.fnames)
                d = dtale.show(df)
                d.open_browser()

            except:
                pass
        else:  # windows için
            self.os_send = "C:\\"
            try:
                ff = str(self.filname4)
                filname44 = desktop + "/" + self.filname4
                way = filname44
                print("filname4 = {}".format(filname44))

                for i in cl:
                    h_link = "{}{}_{}_link.txt".format(way, fname, i)
                    h_content = "{}{}_{}_content.txt".format(way, fname, i)
                    link_list.append(h_link)
                    content_list.append(h_content)

                    file_list.append(h_link)
                    file_list.append(h_content)

                    h = "{}".format(i.strip())
                    print(h)
                    print("--------hhhhhhh ---------------")
                    fn.append(h)
                ss = []

                for i in range(len(cl)):
                    print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
                    print(i)

                    ii = '{}={}("{}","{}","{}")'.format(cl[i], cl[i], self.cat, fn[i], fname)
                    print(ii)
                    print("zzzzzzzzzzzzzzzzzzzzzzzz")
                    ss.append(ii)
                zeta = []
                sayac = 0
                for i in ss:
                    print(i)
                    print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
                    exec(i)
                    d_link = "{}".format(link_list[sayac])
                    print("---------------------------------- dlink---------")
                    print(d_link)
                    print("???????????????????????")

                    z = i.split("=")
                    print(z)
                    zet = "{}{}".format(z[0], ".main()")
                    zeta.append(zet)
                    print("zeeeeeeeeeeettttttttttt")
                    print(zet)
                    exec(zet)
                    d_content = ("{}".format(content_list[sayac]))
                    print(" ***************** d_content ****************")
                    print(d_content)
                    print(" ***************** d_content ****************")
                    # zipped_file = zipFiles(d_content)
                    # download_file_g(d_content)
                    sayac += 1

                newspaper_result = "succesfully completed try another search"
                print(newspaper_result)

            except:
                pass

    def n_update_label2(self, txt, filname4, *args):  # eklenecek
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

    def n_update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            News_Search.run(self, self.keyword, self.newspaper_name, self.fname)
            self.n_update_label2("Succes.", self.filname4)

    def n_router(self, keyword,  newspaper_name, fname):  # kv den gelen root.x()
        self.keyword = keyword

        self.fname = fname
        self.newspaper_name = newspaper_name

        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.n_update_label, 0.05)
