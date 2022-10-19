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
from datetime import datetime, timedelta,date

class milli:
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
        self.filname = desktop + '/' + ff #+ '/' + ff

        # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
        #                                                                              self.dirname) + ff  # +"/"+ff
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)
        print(self.content_filname)
        print(self.filname)



# https://www.milligazete.com.tr/arsiv/2019-10-10/
    def dateCreator(self,d1,d2):
        dizi=[]
        tamam_link = "https://www.milligazete.com.tr/arsiv/"
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)

        for i in dates:
            newdate = i.strftime('%Y-%m-%d')
            dizi.append("{}{}".format(tamam_link, newdate))

        return dizi #kanser_links, memekanseri_links, prostat_links, tamamı_links


    def get_link(self,url):
        html = requests.get(url).content
        date = url[37:]
        soup = BeautifulSoup(html, "html.parser")
        # list = soup.find_all("div", {"class": "category-news"})
        # try:
        list = soup.find_all("div", {"class": "f-cat f-item"})
        # for i in list:
        for j in list:
            print("---------------------------")
            cat = j.find('h3', {"class": "f-brandon-black"}).text
            print(j.find('h3', {"class": "f-brandon-black"}).text)
            print("---------------------------")
            z = j.find_all('a', {"class": "lb"})
            print(z)
            for i in z:
                wdata = "{}{} ;{} ;{}".format("https://www.milligazete.com.tr", i.get("href"), date, cat)
                print(wdata)
                with open(self.link_filname, "a", encoding="utf-8") as file:
                    file.write(wdata + "\n")
        # except:
        #     pass


#https://www.milligazete.com.tr/haber/1708597/abdden-arabistana-teklif-fbi-ekibi-yollayabiliriz
    def creator(self,i):
        j =i.split(';')
        date = j[1].strip()
        url = j[0].strip()
        cat = j[2].strip()
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        # try:
        title = soup.find('h1').getText()
        # print(title)
        # print("------------------")
        art = soup.find("div", {"class": "post-text"})
        z = art.find_all('p')
        txt = ""
        for i in z:
            txt += i.text

        cdata = '{} ;{} ;{} ;{} ;{}'.format(url, date,cat,title,txt)
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(cdata + "\n")
        # except:
        #     pass
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])

    def main(self):
        print("************ started to collect page links")

        self.page_links = self.dateCreator(self.date1, self.date2)
        print("-------- all links---")

        for i in self.page_links:
            print(i)
            self.get_link(i.strip())
        print("reading links from {}.,.,.,.,.,.,.,.,.,.,. ".format(self.link_filname))
        with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                i = i.strip("\n")
                self.newsLinks.append(i)

        # print("-----------------------")
        # print(self.content_filname)
        # print(self.link_filname)
        # print("-------------------------")

        for i in self.newsLinks[:]:
            self.creator(i.strip())

        print("Successfully!")

