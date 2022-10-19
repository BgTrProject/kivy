# 832030  # 200 =227
import os
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import time
import urllib.request
import re
import urllib3
from pandas import DataFrame
import csv
import datetime
from datetime import datetime, timedelta
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint

class turkiye:
    def __init__(self, date1, date2, categ, filname, dirname, os_find, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.categ = categ
        self.os_find = os_find
        self.filname = filname
        self.dirname = dirname
        self.page_links = []
        self.content_filname = ""
        self.link_filname = ""

        self.newsLinks = []

        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)

        print(self.filname)
        ff = str(self.dirname)
        self.filname = desktop + '/' + ff

        # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
        #                                                                              self.dirname) + ff  # +"/"+ff
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)

    def dateCreator(self,d1,d2):
        links = []
        son=832030  # 200 =227
        ilk=200
        page_count=son-ilk

        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        z=t2-t1
        day_count=z.days
        count=int(page_count/day_count)
        # f1=t1-datetime(2011,11,29)
        til1='2011-11-29'
        til_=datetime.strptime(til1, '%Y-%m-%d').date()
        f1 = t1 - til_
        print(f1)

        if f1.days>0:
            f1_count=f1.days
        else:
            f1_count=1
        f2 = t2 - til_
        if f2.days > 0:
            f2_count = f2.days
        else:
            f2_count = 2

        day_range=count*(f2_count-f1_count)+205
        print(f1_count)
        print(f1_count*count)
        print(f2_count*count)
        print(f2_count)
        print(day_range)
        url = "https://www.turkiyegazetesi.com.tr/gundem/"
        for i in range(f1_count*213,f2_count*213):
            url_in = "{}{}{}".format(url, i, ".aspx")
            links.append(url_in)

        # t = timedelta(days=1)
        # dates = np.arange(t1, t2, t).astype(datetime)
        #
        # for j in dates:
        #     # link3 = (lnk3.format(j.strftime('%Y/%m/%d')))
        #     link3=
        #     links.append(link3)

        # url = "https://www.turkiyegazetesi.com.tr/gundem/"  # ortadaki kategori anlamsız isteğe göre değiştirebilirsiniz
        # for i in range(200, 300):  # sayfa adeti 200 den başlayıp 798330 e kadar gitmekte
        #     url_in = "{}{}{}".format(url, i, ".aspx")
        #     links.append(url_in)
        #     with open("türkiyegazetesi_link.txt", 'a') as file:
        #         file.write(url_in + '\n')
        return links

    def get_link(self,link):
        href=link
        with open(self.link_filname, "a", encoding="utf-8") as file:
            file.write(href + "\n")

    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find("h1").getText()
        content_array = soup.find("div", attrs={"id": "alan"}).getText()
        date = soup.find("div", attrs={"class": "story_date"}).getText()
        category = soup.find("a", attrs={"class": "current-page"}).getText()
        date = date.split()
        date = date[0]
        content_array = content_array.split()
        content_string = ""
        for w in content_array:
            content_string = content_string + " " + w
            # w_data = url+";"+date+";"+title+";"+content_string
        cdata = "{} ; {} ; {} ; {}".format(url, date, title, content_string) # category çıkarıldı
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])


        # print(w_data)
        # # write_to_txt(w_data)
        # with open(self.content_filname, 'a') as file:
        #     file.write(w_data + '\n')





    def main(self):
        print("************ started to collect page links")

        self.page_links=self.dateCreator(self.date1,self.date2)
        print("-------- all links---")


        for i in self.page_links:
            print(i)
            self.get_link(i.strip())
        print("reading links from {}.,.,.,.,.,.,.,.,.,.,. ".format(self.link_filname))
        with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                i = i.strip("\n")
                self.newsLinks.append(i)


        print("-----------------------")
        print(self.content_filname)
        print(self.link_filname)
        print("-------------------------")

        for i in self.newsLinks[:]:
            self.creator(i.strip())

        print("Successfully!")