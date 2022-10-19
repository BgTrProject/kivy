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


class ensonhaber:
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
        # self.content_filname = self.filname + "_content.txt"
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)

    def dateCreator(self,d1,d2):
        # t1 = datetime(2019, 4, 3)  # en son 1999 05 01 e kadar çalışıyo
        # t2 = datetime(2019, 4, 5)
        # t = timedelta(days=1)
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        links = []
        link = "https://www.ensonhaber.com/mansetler.htm?tarih="  # 146 e kadar sayfa var kanser
        for i in dates:
            newdate = i.strftime('%Y-%m-%d')
            links.append("{}{}".format(link, newdate))

        return links

    def get_link(self,i):
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        url = 'https://www.ensonhaber.com'
        for a in soup.find_all('a', href=True):
            link = a['href']
            result = link.startswith('/')
            if result == True:
                if len(link) > 28:
                    result2 = link.startswith('//')
                    if result2 == False:
                        data = "{}{}".format(url, link)
                        with open(self.link_filname, 'a') as file:
                            file.write(data + '\n')

    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find("h1").getText()
        content_array = soup.find("article", attrs={"class": "content"}).getText()
        category = soup.find("span", attrs={"itemprop": "name"}).getText()
        date = soup.find("div", attrs={"class": "c-date"}).getText()
        date = date.split()
        if date[0] == 'AA' or date[0] == 'İHA' or date[0] == 'DHA' or date[0] == 'REUTERS':
            date = date[1]
        else:
            date = date[2]
        title = title.split()
        content_array = content_array.split()
        content_string = ""
        title_string = ""
        for w in title:
            title_string = title_string + " " + w
        for w in content_array:
            content_string = content_string + " " + w
            # w_data = url+";"+date+";"+title+";"+content_string
        cdata = "{} ; {} ; {} ; {}".format(url, date, category, title_string, content_string) #category çıkarıldı
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])

        # write_to_txt(w_data)
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