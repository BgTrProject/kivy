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



class sabah:
    def __init__(self, date1, date2, categ, filname, dirname,os_find, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.categ = categ
        self.os_find=os_find
        self.filname = filname
        self.dirname = dirname
        self.page_links = []
        self.content_filname = ""
        self.link_filname = ""

        self.newsLinks = []

        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)

        print(self.filname)
        ff = str(filname)

        # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
        #                                                                              self.dirname) + ff  # +"/"+ff
        # self.content_filname = self.filname + "_content.txt"
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)

    def dateCreator(self,d1,d2):
        #https://www.sabah.com.tr/timeline/2020/10/10?c=yasam
        url = 'https://www.sabah.com.tr/timeline'
        keyword = ['gundem', 'ekonomi', 'yasam', 'saglik', 'dunya', 'seyahat', 'yazarlar']
        all_links = []
        txt = ""
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        for i in dates:
            i = i.strftime('%Y/%m/%d')
            if self.categ=='gundem' or self.categ=='ekonomi' or self.categ== 'yasam'or self.categ=='saglik' or self.categ=='dunya' or self.categ== 'seyahat':
                txt = "{}/{}?c={}".format(url, i, self.categ)
                all_links.append(txt)
                print(txt)
            elif self.categ== 'yazarlar':
                txt="{}{}{}".format(url[:-8],'yazarlar/',i)
                all_links.append(txt)
                print(txt)
            else:
                for j in keyword:
                    txt="{}/{}?c={}".format(url, i, j)
                    all_links.append(txt)
                    print(txt)
        return all_links




    def get_link(self,i):
        driver = webdriver.Chrome('/usr/bin/chromedriver')
        driver.get(i)
        time.sleep(2)
        p_h=driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(2)
            new_h=driver.execute_script('return document.body.scrollHeight')
            if new_h==p_h:
                break
            p_h=new_h
        # element=driver.find_element_by_tag_name('body')
        # while True:
        #     element.send_keys(Keys.PAGE_DOWN)
        #     time.sleep(2)

        print("selam")
        sayac=0
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup)
        for a in soup.find_all('a', href=True):
            # print(a.get("href"))
            test = a.get("href")
            result = test.startswith(('/gunde', '/ekono', '/yasam', '/sagli', '/dunya', '/seyah', '/yazar'), 0,
                                     6)
            if result == True:
                if len(test) > 20:
                    txt = ""
                    url = 'https://www.sabah.com.tr'
                    wdata = "{}{}".format(url, test)
                    sayac+=1
                    print(sayac,".Haber")
                    with open(self.link_filname, "a", encoding="utf-8") as file:
                        file.write(wdata + "\n")



    def creator(self,url):

        # for i in link:
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'lxml')
        tt = ""
        try:
            dat = soup.find("div", attrs={"class": "newsBox"})
            dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
            dat2 = dat2[14:-5].strip()


            for i in dat.stripped_strings:
                # print(i.strip())
                tt += i.strip()

            cdata = '{};{};{}'.format(url, dat2.strip(), tt.strip())
            with open(self.content_filname, "a", encoding="utf-8") as file:
                file.write(cdata + "\n")


            tt = ''


        except:
            print("gazeteden kaynaklı sorunlu haber  ----")
        # count = 1
        # # for i in link:
        # r = requests.get(url)
        # print(count, ".Haber")
        # count += 1
        # soup = BeautifulSoup(r.content, 'lxml')
        # txt = ""
        # try:
        #
        #     dat = soup.find("div", attrs={"class": "newsBox"}).text
        #     dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
        #     dat2 = dat2[14:-5].strip()
        #     print("dddddddddddddddddddddddddddddddddddddd")
        #     print(dat2)
        #     print("dddddddddddddddddddddddddddddddddddddd")
        #     print("*****************************************")
        #     print(dat)
        #     print("*****************************************")
        #     for d in str(dat).split("\n"):
        #
        #         # d=d.strip()
        #         if d.startswith('EN ÇOK OKUNANLAR') or d.startswith('SON DAKİKA'):
        #             break
        #         else:
        #             txt += d
        #             txt.strip()
        #
        #     # print("=========================================================")
        #     cdata = '{};{};{}'.format(url, dat2.strip(), txt.strip())
        #     print(cdata)
        #
        #     with open(self.content_filname, "a", encoding="utf-8") as file:
        #         file.write(cdata + "\n")
        #     txt = ''
        #     # print("=========================================================")
        # except:
        #     print("nanay    ----")



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
    #     count = 1
    #     # for i in link:
    #     r = requests.get(url)
    #     print(count, ".Haber")
    #     count += 1
    #     soup = BeautifulSoup(r.content, 'lxml')
    #     txt = ""
    #     try:
    #
    #         dat = soup.find("div", attrs={"class": "newsBox"})
    #         dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
    #         dat2=dat2[14:-5].strip()
    #         cdat=dat.find_all('p')
    #         print("dddddddddddddddddddddddddddddddddddddd")
    #         print(dat2)
    #         print("dddddddddddddddddddddddddddddddddddddd")
    #         print("*****************************************")
    #         print(cdat)
    #         print("*****************************************")
    #         for d in str(cdat).split("\n"):
    #
    #             # d=d.strip()
    #             if d.startswith('EN ÇOK OKUNANLAR') or d.startswith('SON DAKİKA'):
    #                 break
    #             else:
    #                 txt+=d
    #                 txt.strip()
    #
    #
    #         print("=========================================================")
    #         cdata='{};{};{}'.format(url,dat2.strip(),txt.strip())
    #         print(cdata)
    #         txt=''
    #         print("=========================================================")
    #     except:
    #         print("nanay    ----")
    # uur='https://www.sabah.com.tr/gundem/2021/10/10/firat-kalkani-bolgesindeki-sehit-polis-sayisi-2ye-yukseldi'
    # creator(uur)