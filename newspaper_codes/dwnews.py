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


class dwnews:
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



    def dateCreator(self,d1,d2):
        links = []

        # ser_date = pd.Series(pd.date_range('20011001', periods=8400))  # 01.10.2001 bu
        ser_date = pd.Series(pd.date_range(d1, periods=8400))  # 01.10.2001 bu
        link1 = "https://www.dw.com/search/?languageCode=en&item="
        link2 = "&searchNavigationId=9097&from="
        link3 = "&to="
        link4 = "&sort=DATE&resultsCounter=50"
        # category = ['science', 'technology']
        category = self.categ
        a = 5000
        b = 5100  # 7407 son
        for i in category:
            for j in range(a, b):
                dateEnd = ser_date[j].strftime("%d.%m.%Y")
                links.append("{}{}{}{}{}{}{}".format(link1, i, link2, dateEnd, link3, d2, link4))
                # links.append("{}{}{}{}{}{}{}".format(link1, i, link2, dateEnd, link3, dateEnd, link4))
        return links

    def get_link(self,i):
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        for a in soup.find_all('a', href=True):
            link = a['href']
            result = link.startswith("/en")
            if (result == True):
                control = link[len(link) - 11:len(link) - 9]
                if (control == "av" or control == "/a"):
                    result2 = link.startswith("/en/travel/") or link.startswith(
                        "/en/european-union-general-data-protection-regulationgdpr-valid-may-25-2018/a-18265246") or link.startswith(
                        "/en/accessibility-statement/a-54925999")
                    if (result2 == False):
                        w_data = "{}{}".format("https://www.dw.com", link)
                        # with open("NewsLinks.txt", 'a') as file:

                        with open(self.link_filname, 'a') as file:
                            file.write(w_data + '\n')

    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find("h1").getText()
        content_array = soup.find("div", attrs={"class": "longText"})
        content_array2 = ""
        for a in content_array.find_all('p'):
            content_array2 = content_array2 + a.getText()
        category = soup.find("h4", attrs={"class": "artikel"}).getText()
        date = soup.find("div", attrs={"class": "dim"}).getText()
        date = re.sub("^\s+|\s+$", "", date, flags=re.UNICODE)
        date = date.split("\n")
        date = date[1]
        content_string = ""
        content_array2 = content_array2.split(" ")
        for m in content_array2:
            content_string = content_string + " " + m
        cdata = "{} ; {} ; {} ; {}".format(url, date, title, content_string) #categori çıkarıldı
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # with open(self.content_filname, 'a') as file:
        #     file.write(w_data + '\n')
    def main(self):
        print("*********************")
        print(self.categ)
        self.page_links=self.dateCreator(self.date1,self.date2)

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