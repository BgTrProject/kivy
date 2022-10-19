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
# import json
from fake_useragent import UserAgent
from kivy.clock import Clock


import time
from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time
import numpy as np

from pycode.google import google_search
from pycode.google6 import google_search6
import pandas as pd
import dtale
import csv
import requests
from newsplease import *
from newsplease import NewsPlease
import webbrowser
from newspaper import Article

class GoogleTopik(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'search_engine'
        self.manager.get_screen('login').resetForm()
    def open_page(self):
        webbrowser.open('html_files\\google_topik.html')
    
    def run(self, keyword,topic, date1, date2, fname):
        self.function_interval = Clock.schedule_interval(self.topicgoogle_update_label, 0.05)
        self.fname = fname
        self.topic=topic
        self.filname4 = self.fname + ".csv"
        self.date1 = date1
        self.date2 = date2
        self.keyword = keyword
        self.url_links = []
        dat1 = self.date1.split(',')
        dat2 = self.date2.split(',')
        print(self.date1)
        print(self.date2)
        self.os_send=""
        # fn = []
        # link_list = []
        # content_list = []
        # file_list = []
        #
        # # cl = cl_names_all.split(",")
        # cl = n_name.split(",")
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
            fnames = desktop + "/" + fname + '.csv'
            fnames2 = desktop + "/" + fname + '_content.csv'
            fnamesw = desktop + "\\" + fname + '.csv'
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
            # self.os_send = "/usr/bin/google-chrome"
            for da1, da2 in zip(dat1, dat2):
                non = 0
                da1 = da1.strip()
                d1 = da1
                #
                # d1 = datetime.strptime(da1, '%Y/%m/%d').date()
                # d1 = d1.strftime('%m/%d/%Y')

                da2 = da2.strip()
                # d2 = datetime.strptime(da2, '%Y-%m-%d').date()
                # d2 = d2.strftime('%m/%d/%Y')
                d2 = da2

                # vord = "*.*"
                # print(vord)

                print(d1)
                print(d2)
                google = google_search6(self.keyword,self.topic,fnames, d1, d2,self.os_send)
                # google = google_bypass(vord, ngnum2, fnames, d1, d2)
                try:
                    for i in google.urls:
                        non += 1
                        self.url_links.append(i)
                except AttributeError:
                    pass

            # with open(fnames) as csv_file:
            #     csv_reader = csv.reader(csv_file, delimiter=',')
            #     line_count = 0
            #     for row in csv_reader:
            #         if row == "links":
            #             pass
            #         else:
            #             self.url_links.append(row)
            # with open(fnames, 'r', newline='', encoding="utf-8") as f:
            #     for i in f.readlines():
            #         i = i.strip("\n")
            #         print(i)
            #         self.url_links.append(i)

            # for i in self.url_links:
            #     i = str(i)
            #
            #
            #     # fieldnames = ['url', 'date', 'title', 'content']
            #     try:
            #         article = NewsPlease.from_url(i.strip())
            #         a = article.url
            #     except:
            #         a="None"
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
            #     if(a=='None'):
            #         pass
            #     else:
            #         sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
            #         with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
            #             csvwriter = csv.writer(csvfile, delimiter=' ')
            #             csvwriter.writerow([sent_line])
            #     #     for lin in linky:
            #     #         csvwriter.writerow([lin])
            #     #         print("sssssssss")
            #         print("close csv")
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
                print(dd)
                sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ')
                    csvwriter.writerow([sent_line])
                #     for lin in linky:
                #         csvwriter.writerow([lin])
                #         print("sssssssss")
                print("close csv")


                #########################################333333
                # counter=0

                # with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                #     print("open csv")
                #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #     # if counter==0:
                #     #     csvwriter.writerow(rows)
                #     # for lin in linky:
                #     csvwriter.writerow(fieldnames)
                #     csvwriter.writerow(rows)

                # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                #     writer = csv.DictWriter(f, fieldnames=fieldnames)
                #     writer.writeheader()
                #     writer.writerows(rows)

                # print(f'Processed {line_count} lines.')

            newspaper_result = "succesfully completed try another search"
            print(newspaper_result)
            df = pd.read_csv(fnames2)
            d = dtale.show(df)
            d.open_browser()
            #
            # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
            # # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # # file_path = BASE_DIR + '/g_upload/' + fname
            # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
            # print(file_path)
            # zf = "{}/{}".format(file_path, fname)
            # print(zf)
            # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
            # shutil.make_archive(zf, 'zip', file_path, '{}.csv'.format(fname))

            # shutil.make_archive(zf, 'zip', file_path, '{}_{}_content.txt'.format(fname, cl[0]))  # ,'{}'.format(fname))
            # zf_s = "{}{}".format(zf, '.zip')
            # print(zf_s)
            #
            # file = open(zf_s, 'rb')
            # response = FileResponse(file)
            # response['Content-Type'] = 'application/octet-stream'
            # response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)

            # return response

        else:
            self.os_send = "C:\\"
            for da1, da2 in zip(dat1, dat2):
                non = 0
                da1 = da1.strip()
                d1 = da1
                #
                # d1 = datetime.strptime(da1, '%Y/%m/%d').date()
                # d1 = d1.strftime('%m/%d/%Y')

                da2 = da2.strip()
                # d2 = datetime.strptime(da2, '%Y-%m-%d').date()
                # d2 = d2.strftime('%m/%d/%Y')
                d2 = da2

                # vord = "*.*"
                # print(vord)

                print(d1)
                print(d2)
                google = google_search6(self.keyword, self.topic, fnamesw, d1, d2, self.os_send)
                # google = google_bypass(vord, ngnum2, fnames, d1, d2)
                try:
                    for i in google.urls:
                        non += 1
                        self.url_links.append(i)
                except AttributeError:
                    pass

            # with open(fnames) as csv_file:
            #     csv_reader = csv.reader(csv_file, delimiter=',')
            #     line_count = 0
            #     for row in csv_reader:
            #         if row == "links":
            #             pass
            #         else:
            #             self.url_links.append(row)
            # with open(fnames, 'r', newline='', encoding="utf-8") as f:
            #     for i in f.readlines():
            #         i = i.strip("\n")
            #         print(i)
            #         self.url_links.append(i)

            # for i in self.url_links:
            #     i = str(i)
            #
            #
            #     # fieldnames = ['url', 'date', 'title', 'content']
            #     try:
            #         article = NewsPlease.from_url(i.strip())
            #         a = article.url
            #     except:
            #         a="None"
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
            #     if(a=='None'):
            #         pass
            #     else:
            #         sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
            #         with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
            #             csvwriter = csv.writer(csvfile, delimiter=' ')
            #             csvwriter.writerow([sent_line])
            #     #     for lin in linky:
            #     #         csvwriter.writerow([lin])
            #     #         print("sssssssss")
            #         print("close csv")
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
                print(dd)
                sent_line = '{} ; {} ; {} ; {}'.format(a, b, c, dd)
                with open(fnames2w, 'a', encoding='UTF8', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ')
                    csvwriter.writerow([sent_line])
                #     for lin in linky:
                #         csvwriter.writerow([lin])
                #         print("sssssssss")
                print("close csv")

                #########################################333333
                # counter=0

                # with open(fnames2, 'a', encoding='UTF8', newline='') as csvfile:
                #     print("open csv")
                #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #     # if counter==0:
                #     #     csvwriter.writerow(rows)
                #     # for lin in linky:
                #     csvwriter.writerow(fieldnames)
                #     csvwriter.writerow(rows)

                # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                #     writer = csv.DictWriter(f, fieldnames=fieldnames)
                #     writer.writeheader()
                #     writer.writerows(rows)

                # print(f'Processed {line_count} lines.')

            newspaper_result = "succesfully completed try another search"
            print(newspaper_result)
            df = pd.read_csv(fnames2w)
            d = dtale.show(df)
            d.open_browser()

    def topicgoogle_update_label2(self, txt, filname4, *args):  # eklenecek
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

    def topicgoogle_update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            GoogleTopik.run(self, self.keyword,self.topic,self.d1, self.d2, self.fname)
            self.topicgoogle_update_label2("Succes.", self.filname4)

    def topicgoogle_router(self, keyword,topic, d1, d2, fname):
        self.keyword = keyword
        self.topic=topic
        self.d1 = d1
        self.d2 = d2
        self.fname = fname

        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.topicgoogle_update_label, 0.05)