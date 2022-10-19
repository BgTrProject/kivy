
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

class sozcu:
    def __init__(self, date1, date2, categ, filname, dirname, os_find, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.categ = categ
        self.os_find = os_find

        if categ!='gundem' or categ!='dunya':
            self.categ='teknoloji'
        else:
            self.categ=categ
        # self.categ = categ

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
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        # gundem_links = []
        # dunya_links = []
        # ekonomi_links = []
        # otomotiv_links = []
        # saglik_links = []
        # egitim_links = []
        # teknoloji_links = []
        dizi=[]
        gundem = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPalk2SW1kMWJtUmxiU0k3Y3pvNU9pSndiM04wWDNSNWNHVWlPM002TkRvaWNHOXpkQ0k3ZlE9PQ==/"  # 8146 sayfa
        dunya = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPalU2SW1SMWJubGhJanR6T2prNkluQnZjM1JmZEhsd1pTSTdjem8wT2lKd2IzTjBJanQ5/"  # 1895
        ekonomi = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPamM2SW1WcmIyNXZiV2tpTzNNNk9Ub2ljRzl6ZEY5MGVYQmxJanR6T2pRNkluQnZjM1FpTzMwPQ==/"  # 1474
        otomotiv = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPamc2SW05MGIyMXZkR2wySWp0ek9qazZJbkJ2YzNSZmRIbHdaU0k3Y3pvME9pSndiM04wSWp0OQ==/"  # 175
        saglik = ""  # hatalı sayfa ama açık bıraktım aşağıdaki yorum satırında olan prosesleri açıp doğru bi link girilince çalışır
        egitim = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPalk2SW1WbmFYUnBiU0k3Y3pvNU9pSndiM04wWDNSNWNHVWlPM002TkRvaWNHOXpkQ0k3ZlE9PQ==/"  # 295
        teknoloji = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPams2SW5SbGEyNXZiRzlxYVNJN2N6bzVPaUp3YjNOMFgzUjVjR1VpTzNNNk5Eb2ljRzl6ZENJN2ZRPT0=/"  # 321
        if self.categ=="gundem":
            for i in range(1, 8000, 1):
                # gundem_links.append("{}{}".format(gundem, i))
                dizi.append("{}{}".format(gundem, i))
        elif self.categ=="dunya":
            for i in range(1, 2000, 1):
                # dunya_links.append("{}{}".format(dunya, i))
                dizi.append("{}{}".format(dunya, i))
        elif self.categ == "ekonomi":
            for i in range(1, 200, 1):
                dizi.append("{}{}".format(ekonomi, i))
        elif self.categ == "otomotiv":
            for i in range(1, 200, 1):
                dizi.append("{}{}".format(otomotiv, i))
        elif self.categ == "saglik":
            for i in range(1, 175, 1):
                dizi.append("{}{}".format(saglik, i))
        elif self.categ == "egitim":
            for i in range(1, 295, 1):
                dizi.append("{}{}".format(egitim, i))
        else:
            for i in range(1, 321, 1):
                dizi.append("{}{}".format(teknoloji, i))


        return dizi#gundem_links, dunya_links, ekonomi_links, otomotiv_links, saglik_links, egitim_links, teknoloji_links

    def get_link(self,i):
        count = 1
        count2 = 0
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        dizi = []
        for a in soup.find_all('a', href=True):
            link = a['href']
            if count % 2 == 1:
                with open(self.link_filname, 'a') as file:
                    file.write(link + '\n')
                    dizi.append(link)
            count += 1

    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find("h1").getText()
        content_array = soup.find("div", attrs={"class": "content"}).getText()
        category_array = soup.find("a", attrs={"class": "text-muted small"}).getText()
        category_array = category_array.split()
        date = soup.find("time").getText()
        date = date.split()
        date = date[2] + date[3] + date[4]
        content_array = content_array.split()
        content_string = ""
        stop = "aip2('pageStructure',"
        for w in content_array:
            if stop == w:
                break
            else:
                content_string = content_string + " " + w
                # w_data = url+";"+date+";"+title+";"+content_string
        cdata = "{} ; {} ; {} ; {}".format(url, date, title, content_string)  #category_array çıkarıldı
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