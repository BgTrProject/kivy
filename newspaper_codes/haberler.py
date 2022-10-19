import os
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import urllib.request
import re
import urllib3
from pandas import DataFrame
import csv
import datetime
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class haberler:
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
    # def page_get_link_selenium(self,url):
    #     dizi=[]
    #
    # 
    #
    #
    #     return dizi

    def page_get_link(self,urr):
        sayac = 1
        dizi = []
        new_url = urr
        new_url = new_url.replace("s1", "s{}")
        while True:

            url =new_url.format(sayac)
            # print(url)
            # print(sayac)
            dizi.append(url)
            r = requests.get(url).content
            soup = BeautifulSoup(r, "html.parser")
            # p_count = soup.find("div",{"class":"hbPagination"}).find_all("span")
            array = []
            span = ""
            pages_links = []

            if not soup.find("div", {"class": "hbPagination"}):  # Linklerin sayfaları ile birlite ayarlıyor
                pages_links.append(url)
            else:

                p_count = soup.find("div", {"class": "hbPagination"}).find_all("span")
                a = p_count
                # print(a[3].text)
                try:
                    print(a[4].text)
                    if a[4].text == (""):
                        pass
                        # print("bura boş ")
                    else:
                        pass
                        # print("devam et")

                except:
                    h = a[3].text
                    # print("son sayfa {} dur".format(h))
                    break
                sayac += 1
        # r = requests.get(url).content
        # soup = BeautifulSoup(r, "html.parser")
        # # p_count = soup.find("div",{"class":"hbPagination"}).find_all("span")
        # array = []
        # span = ""
        # pages_links=[]
        # if not soup.find("div", {"class": "hbPagination"}):  # Linklerin sayfaları ile birlite ayarlıyor
        #     pages_links.append(url)
        # else:
        #     p_count = soup.find("div", {"class": "hbPagination"}).find_all("span")
        #     for i in p_count:
        #         span = i.getText()
        #         array.append(span)
        #         print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        #         print(span)
        #         print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        #
        #     page_num = len(array) - 1
        #     new_url = url
        #     new_url = new_url.replace("s1", "s{}")
        #
        #     for i in range(page_num):
        #         i = str(i + 1)
        #         lnk = new_url.format(i)
        #         pages_links.append(lnk)
        return dizi
 # https://www.haberler.com/arsiv/02-01-2017/haberler/s1/
    def dateCreator(self,d1,d2):

        dizi = []
        pages=[]
        pgl=[]
        # ser_date = pd.Series(pd.date_range('19920101', periods=12000))
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        url = "https://www.haberler.com/arsiv/{}/haberler/s1/"
        num = 1
        # t1 = datetime(2006, 6, 1)
        # t2 = datetime(2021, 8, 5)  # Genel liinkleri oluşturyor
        # t = timedelta(days=1)
        # dates = np.arange(t1, t2, t).astype(datetime)
        for j in dates:
            new_url = (url.format(j.strftime('%d-%m-%Y'), num))
            pages.append(new_url)
        for i in pages:
            print("+++++++++++++++      +++++++++++++")
            print(i)
            uur=str(i.strip())

            pgs=self.page_get_link(uur)
            # pgs=self.page_get_link_selenium(uur)
            print("--------------pgl------------------")
            for p in pgs:
                print("****************** p **************************")
                dizi.append(p)

        return dizi



    def get_link(self,url):
        page_news_links=[]
        # url="https://www.haberler.com/arsiv/02-01-2017/haberler/s1/"
        r = requests.get(url).content
        soup = BeautifulSoup(r, "html.parser")
        # list = soup.find_all("div", {"class": "box boxStyle color-general"})
        list = soup.find_all("div", {"class": "p12-col"})
        # tüm sayfalardaki haberlerin linklerini alıyor
        for i in list:
            href = i.find("a").get("href")
            nhref="{}{}".format("https://www.haberler.com",href)
            print(nhref)
            page_news_links.append(nhref)

        with open(self.link_filname, "a", encoding="utf-8") as file:
            for i in page_news_links:
                file.write(i + "\n")

    def creator(self,url):
        r = requests.get(url).content
        soup = BeautifulSoup(r, "html.parser")
        # title = soup.find("div", {"class": "hbptHead"}).find("h1", {"class": "haber_baslik"}).getText()
        title = soup.find("header", {"class": "hbptHead"}).find("h1").getText()
        # print(title)
        date = soup.find("div", {"class": "hbptTagDate"}).find("time").getText()
        date = date[:10]
        # print(date)
        # categori_array = []
        # categori = soup.find("div", {"class": "hbptTagDate"}).find_all("a")
        #
        # for i in categori:
        #     # print(i)
        #     categori_array.append(i.getText())  # Her Link içeriğini alır ve yazdırır
        # cat = categori_array[len(categori_array) - 1]
        # print(cat)

        content_string = ""
        content = soup.find("main", {"class": "hbptContent haber_metni"}).find_all("p")

        for i in content:
            content_string += i.getText().strip("Kaynak: ")
        cdata = "{} ; {} ; {} ; {}".format(url, date, title, content_string)
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # print(sentence)
        #
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(sentence + "\n")

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




    # def creator(url):
    #     r = requests.get(url).content
    #     soup = BeautifulSoup(r, "html.parser")
    #     # title = soup.find("div", {"class": "hbptHead"}).find("h1", {"class": "haber_baslik"}).getText()
    #     title = soup.find("header", {"class": "hbptHead"}).find("h1").getText()
    #     print(title)
    #     date = soup.find("div", {"class": "hbptTagDate"}).find("time").getText()
    #     date = date[:10]
    #     print(date)
    #     categori_array = []
    #     categori = soup.find("div", {"class": "hbptTagDate"}).find_all("a")
    #
    #
    #     for i in categori:
    #         # print(i)
    #         categori_array.append(i.getText())  # Her Link içeriğini alır ve yazdırır
    #     cat = categori_array[len(categori_array) - 1]
    #     print(cat)
    #
    #     content_string = ""
    #     content = soup.find("main", {"class": "hbptContent haber_metni"}).find_all("p")
    #
    #     for i in content:
    #         content_string += i.getText().strip("Kaynak: ")
    #     sentence = "{} ; {} ; {} ; {} ; {}".format(url, cat, date, title, content_string)
    #     print(sentence)
