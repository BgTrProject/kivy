
import bs4
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup,builder#,builder_registry
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

class banker:
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


        self.categories_array=[]
        self.cat_array=[]
        self.page_counts=[]
        self.date_link = []

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
#########################################################
    def is_full(self,link):
        # news_link_alive=[]
        pass_text = "Няма намерени материали съответстващи на избрания период"
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')

        dat = soup.find_all("div", attrs={"class": "col-xs-12 col-sm-6"})
        # print(len(dat))
        # print("1.fonk")
        # print(len(dat[1]))
        # print("-----------",dat.getText())
        h = len(dat)
        # print(len(h))
        # print("ssssss",h)
        # print(type(h))
        if h == 0:
            # pass
            # print("no news")
            return "None"
            # return None
        else:
            return link

    def pagecountfinder(self,link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            dat = soup.find("ul", attrs={"class": "pagination pagination-sm"}).findAll("li")
            txt = (dat[-1].a.get("href"))
            count = int(txt[-1])
        except:
            # print(link)
            # print(link[-10:])
            count = 2
            txt = "{}{}{}".format("/archive/", link[-10:], "/page//")
        return txt, count + 1



######################################################
    def dateCreator(self, d1, d2):
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        txt = ""
        newdate = ""
        url_in = ""
        available_links = []
        url = "https://www.banker.bg/archive/"
        dates = np.arange(t1, t2, t).astype(datetime)
        for i in dates:
            # print(i.strftime('%d-%m-%Y'))
            newdate = i.strftime('%d-%m-%Y')
            url_in = "{}{}".format(url, newdate)
            available_links.append(url_in)
        return available_links




    def get_link(self,link):
        array = []
        # dtime = []//self.date_link
        date = ""
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        dat = soup.findAll("div", attrs={"class": "col-xs-12 col-sm-6"})
        for i in dat:
            # for i in j.a.get("href"):
            in_link = "{}{}".format("https://www.banker.bg", i.a.get("href"))
            # print(i.a.get("href"))
            # print(in_link)
            array.append(in_link)
            date = link[-17:-7]
            # print(date)
            self.date_link.append(date)  # link[-17:-7]
            ps = ""
            with open(self.link_filname, 'a') as file:
                ps = "{}{}{}".format(in_link, ";", date)
                # ps="{}{}{}{}{}{}{}".format(inner_array[0],";",inner_array[1],";",inner_array[2],";",inner_array[3])
                file.write(ps + '\n')

    def creator(self,link, date):
        # link = 'https://www.banker.bg/upravlenie-i-biznes/read/durjavnite-benzinostancii-na-finalnata-prava-no-s-neiasno-finansirane'
        inner_array = []
        atxt = ""
        # print(link)
        lnk = link.split(';')
        link = lnk[0]
        print("================")
        print(lnk[0])
        # print(lnk[1])

        inner_array.append(link)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            dat = soup.find("span", attrs={"class": "time-published"}).time.get("datetime")
            dat = dat[-10:]


        except:
            dat = "date None"
        # print(dat)
        inner_array.append(dat)
        try:
            title = soup.find("h1", attrs={"class": "blue"}).getText()
        except:
            title = " title None"
        inner_array.append(title.strip())
        try:
            table = soup.find("div", attrs={"class": "body oembed"}).find_all("p")
            print(table)
            z = ""
            for k in table:
                print("    kkkkkkkkkkk         kkk")
                z += k.text
        except:
            z = "None"
        inner_array.append(z.strip())
        # ps = ""
        # with open(self.content_filname, 'a') as file:
        #       ps="{}{}{}{}{}{}{}".format(inner_array[0].strip()," ; ",inner_array[1].strip()," ; ",inner_array[2].strip()," ; ",inner_array[3].strip())
        #       file.write(ps+'\n')
        #       print(ps)
        cdata=""
        cdata="{}{}{}{}{}{}{}".format(inner_array[0].strip()," ; ",inner_array[1].strip()," ; ",inner_array[2].strip()," ; ",inner_array[3].strip())
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])





    def main(self):
        print("*********************")
        print(self.categ)
        print(self.date1)
        print(self.date2)
        self.page_links=self.dateCreator(self.date1,self.date2)
        for i in self.page_links[:]:
            print(i)
            print("*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-**--*-*-*-*-")

        for i in self.page_links[:]:
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
            sayac = 0
            self.creator(i[:-11].strip(),self.date_link[sayac])
            sayac += 1

        print("Successfully!")
