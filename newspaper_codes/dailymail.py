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
# https://www.dailymail.co.uk/home/sitemaparchive/day_20201010.html
class dailymail:
    def __init__(self, date1, date2, categ, filname, dirname,os_find, **kwargs):
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
        # print(self.link_filname)
        # https://www.dailymail.co.uk/home/sitemaparchive/day_20161001.html
    def dateCreator(self, d1, d2):
          # u1 = "https://www.gazeteduvar.com.tr/arsiv?"
          # u2 = "&tarih_baslangic="
          # u3 = "&tarih_bitis="
          # u4 = "&siralama=0&sayfa="
          # url="https://www.dailymail.co.uk/home/sitemaparchive/day_.html"
          t1 = datetime.strptime(d1, '%Y-%m-%d').date()
          t2 = datetime.strptime(d2, '%Y-%m-%d').date()
          dizi = []
          t = timedelta(days=1)
          dates = np.arange(t1, t2, t).astype(datetime)
          counter = 1
          for i in dates:
              i = i.strftime('%Y%m%d')
              url='https://www.dailymail.co.uk/home/sitemaparchive/day_{}.html'.format(i)
              dizi.append(url)
          return dizi
    def get_link(self,url):
        html = requests.get(url).content
        # # date=url[37:]
        soup = BeautifulSoup(html, "html.parser")
        # list = soup.find_all("div", {"class": "col-12 col-lg mw0"})
        list2 = soup.find_all('ul', {"class": "archive-articles debate link-box"})
        z = []
        for i in list2:
            h = soup.find_all('li')
            for j in h:
                lnk=j.a.get("href")
                if lnk== None:
                    break
                elif lnk.endswith("index.html"):
                    pass

                elif lnk.startswith("/news") or lnk.startswith("/money") or lnk.startswith("/health") or lnk.startswith("/debate") or lnk.startswith("/tvshowbiz") or lnk.startswith("/wires") or lnk.startswith("/sport"):
                    uur = 'https://www.dailymail.co.uk'
                    new_url = uur + j.a.get("href")
                    with open(self.link_filname, "a", encoding="utf-8") as file:
                        file.write(new_url + "\n")

                else:

                    pass


    def creator(self,url):
        html = requests.get(url).content
        # # date=url[37:]
        soup = BeautifulSoup(html, "html.parser")
        try:
            list = soup.find_all("div", {"itemprop": "articleBody"})
        except:
            list="None"
        try:
            list2 = soup.find('h2').text
        except:
            list2="None"
        # print(list2)
        sentence = ""
        # date=""
        dat = ""
        s = 1
        try:
            for i in list:
                h = soup.find_all("p")
                for j in h:
                    if (s < 6):
                        dat += j.text.strip() + ';'

                    elif (s > 5):

                        # print(j.text)
                        sentence += j.text.strip()
                    else:
                        pass
                    s += 1

            new_date2 = dat.split(';')
            new_date=new_date2[1][22:-37].strip()
        except:
            new_date="None"
            sentence="None"

        # for i in list:

        #     h = soup.find_all("p", {"class": "mol-para-with-font"})
        #     for j in h:
        #         sentence+=j.text.strip()

        cdata = ""
        cdata = '{} ; {} ; {} ; {}'.format(url,new_date , list2, sentence)
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(cont + "\n")
        # html = requests.get(url).content
        # # # date=url[37:]
        # soup = BeautifulSoup(html, "html.parser")
        # list = soup.find_all("div", {"itemprop": "articleBody"})
        # list2 = soup.find('h2').text
        # # print(list2)
        # sentence=""
        # # date=""
        # for i in list:
        #     h = soup.find_all("p")
        #     for j in h:
        #         # print(j.text)
        #         sentence += j.text.strip()
        # # for i in list:
        # #     h = soup.find_all("p", {"class": "mol-para-with-font"})
        # #     for j in h:
        # #         sentence+=j.text.strip()
        # cont='{} ; {}'.format(url,sentence)


    def main(self):
        print("************ started to collect page links")

        self.page_links = self.dateCreator(self.date1, self.date2)
        # print("-------- all links---")

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

        for i in range(len(self.newsLinks[:])):
            # if i%10==0:
            #     print(i)
                self.creator(self.newsLinks[i].strip())
            # else:
            #     pass

        print("Successfully!")