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



class odatv4:
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

    # https://www.odatv4.com/arsiv?ara=&tarih=2017-01-01
    def dateCreator(self,d1,d2):
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        dizi = []
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        url='https://www.odatv4.com/arsiv?ara=&tarih='
        for i in dates:
            i = i.strftime('%Y-%m.%d')
            new_url='{}{}'.format(url,i)
            dizi.append(new_url)
        return dizi

    def get_link(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find_all("a", {"class": "news-item-link br5"})
        for i in list:
            urr = i.get("href")
            wdata='{}{}'.format('https://www.odatv4.com',urr)
            with open(self.link_filname, "a", encoding="utf-8") as file:
                file.write(wdata + "\n")

    def creator(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1", {"class": "news-headline"}).text.strip()
        # print(title)
        date = soup.find("div", {"class": "news-date"}).find('span').text.strip()
        date = date[:-6]
        date = date.strip()
        # print(date)
        list = soup.find_all("div", {"class": "news-container-text"})
        txt = ""
        for i in list:
            h = soup.find_all('p')
            for j in h:
                txt += j.text
        cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(cdata + "\n")

    def main(self):
        print("************ started to collect page links")

        self.page_links = self.dateCreator(self.date1, self.date2)
        print("-------- all links---")

        for i in self.page_links:
            # print(i)
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




