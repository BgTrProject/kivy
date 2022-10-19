import bs4
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup,builder_registry,builder
import pandas as pd
import numpy as np
import os
import urllib.request
import re
from pandas import DataFrame
import csv
import lxml
import html5lib
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import time
import multiprocessing
import threading
from multiprocessing import pool
import concurrent
import datetime
from datetime import datetime, timedelta


class trud:
    def __init__(self, date1, date2, categ, filname, dirname, os_find, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.categ = categ
        self.os_find = os_find
        self.filname=filname
        self.dirname=dirname
        self.page_links=[]
        self.content_filname=""
        self.link_filname=""


        self.newsLinks = []

        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)


        print(self.filname)
        ff = str(self.dirname)
        self.filname = desktop + '/' + ff

        # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
        #                                                                              self.dirname) + ff  # +"/"+ff
        # self.content_filname = self.filname + "_content.txt"
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)

    def dateCreator(self, d1, d2):
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        txt = ""
        url = "https://trud.bg/%D0%B0%D1%80%D1%85%D0%B8%D0%B2/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/?date="
        dates = np.arange(t1, t2, t).astype(datetime)
        dizi = []
        for i in dates:
            txt = "{}{}".format(url, i.date())
            dizi.append(txt)
        return dizi

    def get_link(self,link):
        dblink = []
        req = requests.get(link)
        soup = BeautifulSoup(req.content, "lxml")
        titlem = soup.find_all("h3", attrs={"class": "article__title article__title--l font_size_arhiv"})
        # print(titlem)
        c = ""
        counter = 0
        s = 1
        for i in titlem:
            if s == 21:
                break
            if (i is not None):
                c = "{}{}".format("http://trud.bg", i.a.get('href'))
                if c is not None:
                    dblink.append(c)
                    ps = ""
                    ps = c
                    with open(self.link_filname, 'a') as file:
                        # ps="{}{}{}{}{}{}{}".format(pdd[0],";",pdd[1],";",pdd[2],";",pdd[3])
                        # ps="{}".format(ps)
                        file.write(ps + '\n')
                        file.truncate()
                    s += 1
                else:
                    pass

        return dblink

    def creator(self,link):
        array = []
        atxt = ""
        print(link)
        array.append(link)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        dat = soup.find("time", attrs={"class": "tag__text"}).get("datetime")
        array.append(dat)
        title = soup.find("div", attrs={"class": "text"}).h3.getText()
        array.append(title)
        table = soup.select('div[id=article_text_container]')
        tmp2 = ""
        for i in table:
            tmp = soup.findAll("p")
            for i in tmp[:-2]:
                print(i.getText().strip())
                tmp2 += i.getText().strip()
        array.append(tmp2.strip())

        cdata="{}{}{}{}{}{}{}".format(array[0], ";", array[1], ";", array[2], ";", array[3])
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])


        # ps = ""
        # # with open(self.content_filname, 'a') as file:
        #     # ps="{}{}{}{}{}{}{}".format(pdd[0],";",pdd[1],";",pdd[2],";",pdd[3])
        #     ps = "{}{}{}{}{}{}{}".format(array[0], ";", array[1], ";", array[2], ";", array[3])
        #     file.write(ps + '\n')
        #     file.truncate()



    def main(self):
        print("*********************")
        print(self.categ)
        print(self.date1)
        print(self.date2)
        self.page_links=self.dateCreator(self.date1,self.date2)
        for i in self.page_links[:]:
            print(i)
            print("*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-**--*-*-*-*-")

        for i in self.page_links:
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