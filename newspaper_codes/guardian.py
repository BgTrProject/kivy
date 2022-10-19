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
from datetime import datetime, timedelta, date
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint


class guardian:
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
        dizi = []
        # ser_date = pd.Series(pd.date_range('19920101', periods=12000))
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        print(dates)
        link = "https://www.theguardian.com/"
        for i in dates:  # 10958
            newdate = i.strftime("/%Y/%b/%d/all")
            print(newdate)
            ln="{}{}{}".format(link,self.categ, newdate)
            print(ln)
            dizi.append(ln)
        return dizi


    # def dateCreator(self,d1,d2):
    #     print(type(d1))
    #     # d1=date(d1)
    #     print(type(d1))
    #     # d2=date(d2)
    #     technology = []
    #     # uk-news  coronavirus-outbreak   environment/climate-crisis
    #     # uk/environment   science   global-development  uk/technology  uk/business
    #     # category = ['uk-news', 'science', 'coronavirus-outbreak', 'environment/climate-crisis', 'uk/environment',
    #     #             'global-development', 'uk/technology', 'uk/business']
    #     category=self.categ
    #     ser_date = pd.Series(pd.date_range('19990101', periods=8400))
    #     # dat2=d2.strftime("%Y/%b/%d")
    #     # dat1=d1.strftime("%Y/%b/%d")
    #     delta = d2 -d1
    #
    #     print(type(delta))
    #     print(delta)
    #     # h = delta.total_seconds()
    #     # z = (int(h) / (3600 * 24))
    #     z=delta
    #     link = "https://www.theguardian.com/"
    #
    #     for i in category:
    #         for j in range(0, z):
    #             dateEnd = ser_date[j].strftime("/%Y/%b/%d/all")
    #             technology.append("{}{}{}".format(link, i, dateEnd))
    #     return technology

    # def get_link_technology(i):
    def get_link(self,i):
        page_one = 0
        # r = requests.get(i)
        # soup = BeautifulSoup(r.content, 'html5lib')
        # uzunluk = len("https://www.theguardian.com/{}/".format(self.categ))
        # url = i[uzunluk + 3:uzunluk + 7]
        # print(url)
        # url2 = "https://www.theguardian.com/{}/blog/".format(self.categ) + url
        # url3 = "https://www.theguardian.com/{}/".format(self.categ) + url
        # count = 0
        # print(self.link_filname)
        # print("dosya açççççççççççççççççççç")
        # for a in soup.find_all('a', href=True):
        #     link = a['href']
        #     count += 1
        #     result = len(link) > 50
        #     if result == True:
        #         result2 = link.startswith(url2) or link.startswith(url3)
        #         if result2 == True:
        #             if (count % 2 == 0):
        #                 print(link)
        page_one = 0
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        # lnk=soup.find_all("div",{"class":"fc-item__content "}
        try:
            links = soup.find("div", {"class": "fc-container__body fc-container--rolled-up-hide"}).find_all('a')
            counter = 1
            say = 1
            for i in links[:-2]:

                # print(len(i.text))
                counter += 1
                if (counter % 2 == 0):
                    print(say)
                    # say+=1
                    link=i.get("href")
                    say += 1
                    with open(self.link_filname, 'a') as file:
                        print(link)
                        file.write(link + '\n')
                else:
                    pass
        except:
            pass


    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            title = soup.find("h1").getText()
            print(title)
            content_array = soup.find("div", attrs={"class": "article-body-commercial-selector"}).getText()
            # try:
            #     category = soup.find("a", attrs={"class": "dcr-yx39j8"}).getText()
            #     print(category)
            # except:
            #     pass

            date = soup.find("summary", attrs={"class": "dcr-h56grb"}).getText()
            # title = soup.find("h1").getText()
            # print(title)
            # content_array = soup.find("div", attrs={"class": "article-body-commercial-selector"}).getText()
            # category = soup.find("a", attrs={"class": "dcr-yx39j8"}).getText()
            # print(category)
            # date = soup.find("div", attrs={"class": "dcr-km9fgb"}).getText()
            date = date.split()
            date = date[0] + '-' + date[1] + '-' + date[2]
            print(date)
            content_array = content_array.split()
            content_string = ""
            for w in content_array:
                content_string = content_string + " " + w
            cdata = "{} ; {} ; {} ; {}".format(url, date, title, content_string)
            with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=' ')
                csvwriter.writerow([cdata])
            # print(w_data)
            # with open(self.content_filname, 'a') as file:
            #     file.write(w_data + '\n')
        except:
            pass

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