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
from datetime import datetime, timedelta, time, date
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint


class independent:
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
# 'https://www.independent.co.uk/archive/2020-10-10'
    def dateCreator(self,d1,d2):
        dizi = []
        # ser_date = pd.Series(pd.date_range('19920101', periods=12000))
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        print(dates)
        link = "https://www.independent.co.uk/archive/"
        for i in dates:  # 10958
            newdate = i.strftime('%Y-%m-%d')
            print(newdate)
            ln="{}{}".format(link, newdate)
            print(ln)
            dizi.append(ln)
        return dizi

    # def datecreator(t1, t2, coday):
    #     t1 = datetime.strptime(t1, '%d/%m/%Y').date()
    #     t2 = datetime.strptime(t2, '%d/%m/%Y').date()
    #     k = int((t2 - t1).days)
    #     print(k)
    #     print(t1)
    #     print(type(t1))
    #     t = timedelta(days=int(coday))
    #     dates = np.arange(t1, t2, t).astype(datetime)
    #     for date in dates:
    #         newdate = date.strftime('%m/%d/%Y')
    #         mydates.append(newdate)
    #     return mydates

    # dates = np.arange(t1, t2, t).astype(datetime)

    #   categories=['dunya','yerel-haberler','ekonomi','egitim','gundem']
    #   for i in categories:
    #     link_categories="{}{}{}".format(url3,i,url4)
    #     for j in dates:
    #       newdate=j.strftime('%d-%m-%Y')
    #       generate_url="{}{}{}{}{}".format(url1,newdate,url2,newdate,link_categories)
    #       print(generate_url)

    def get_link(self,i):
        print(i)
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            for a in soup.find_all('a', href=True):
                link = a['href']
                result = link.endswith(".html")
                if (result == True):
                    result2 = link.startswith("/service") or link.startswith(
                        "/news/world/journalism-license-srmg-middle-east-news-world-global-a9579111.html")
                    if (result2 == False):
                        ekle = "https://www.independent.co.uk"
                        link = "{}{}".format(ekle, link)
                        with open(self.link_filname, 'a') as file:
                            file.write(link + '\n')
        except:
            pass

    def creator(self,url):
        # r = requests.get(url)
        # soup = BeautifulSoup(r.content, 'html5lib')
        # try:
        #     title = soup.find("h1").getText()
        #     content_array = soup.find("div", attrs={
        #         "class": "ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE"}).find_all(
        #         'p')
        #     # print (title)ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE
        #     date = soup.find("div", attrs={
        #         "class": "FormattedDate__Wrapper-sc-tneaun-0 YtdZt"}).getText()  # "sc-DlApP"}).getText()
        #
        #     # # content_array = soup.find("div", attrs={"class": "sc-bxBxkN"}).getText()  #hatalıdır düzelt
        #     # content_array = soup.find("div", attrs={"class": "sc-fTRTtq jUyLKW sc-kAeuys bhvlhs"}).getText()
        #     # # print (title)
        #     # date = soup.find("div", attrs={"class":"sc-fVmPpc ujYMm"}).getText()# "sc-DlApP"}).getText()
        #     date = date.split()
        #     date = date[3] + "-" + date[2] + "-" + date[1]
        #     # print (date)
        #     date = datetime.strptime(date, "%Y-%B-%d").strftime("%Y-%m-%d")
        #     # print (date)
        #     content_array = content_array.split()
        #     content_string = ""
        #     for w in content_array:
        #         content_string += w.text
        #         # stop = "(function({"
        #         # if (w == stop):
        #         #     break
        #         # else:
        #         #     content_string = content_string + " " + w
        #         #     # w_data = url+";"+date+";"+title+";"+content_string
        #
        #     w_data = "{};{};{};{}".format(url, date, title, content_string)
            # write_to_txt(w_data)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:

            title = soup.find("h1").getText()

            # content_array = soup.find("div", attrs={"class": "sc-bxBxkN"}).getText()  #hatalıdır düzelt
            content_array = soup.find("div", attrs={
                "class": "ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE"}).find_all(
                'p')
            # print (title)ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE
            date = soup.find("div", attrs={
                "class": "FormattedDate__Wrapper-sc-tneaun-0 YtdZt"}).getText()  # "sc-DlApP"}).getText()
            date = date.split()
            date = date[3] + "-" + date[2] + "-" + date[1]
            # print (date)
            date = datetime.strptime(date, "%Y-%B-%d").strftime("%Y-%m-%d")
            # print (date)
            # content_array = content_array.split()
            content_string = ""
            for w in content_array:
                # stop = "(function({"
                # if (w == stop):
                #     break
                # else:
                # content_string = content_string + " " + w
                content_string += w.text
                # w_data = url+";"+date+";"+title+";"+content_string

            cdata = "{} ; {} ; {} ; {}".format(url, date, title, content_string)
            with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=' ')
                csvwriter.writerow([cdata])
            # with open(self.content_filname, 'a') as file:
            #     file.write(w_data + '\n')
        except:
            pass
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