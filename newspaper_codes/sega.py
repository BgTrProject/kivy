
import bs4
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup,builder#,builder_registry
import pandas as pd
import numpy as np
import os
import urllib.request
import re
from pandas import DataFrame
import csv
import lxml
import html5lib
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import time
import multiprocessing
import threading
from multiprocessing import pool
import concurrent
import datetime
from datetime import datetime, timedelta


class sega:
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


        self.categories_array=[]
        self.cat_array=[]
        self.page_counts=[]

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


#############################################

    def headermenuitemfinder(link):
    # def dateCreator(self,link):
        category_array = []
        b = "/"
        lnk = ""
        req = requests.get(link)
        soup = BeautifulSoup(req.content, "lxml")
        # title=soup.find("ul",attrs={"class":"navbar-nav"}).findAll('li')
        title = soup.findAll("a")  # ,attrs={"class":"main_nav__link"})
        s = 0
        for i in title:

            j = i.get("href")
            if (s == 16):
                break
            if (j.startswith("/category")):
                b = (i.get("href"))
                s += 1
                lnk = ("{}{}{}".format("https://www.segabg.com", b, "?page=1"))
                category_array.append(lnk)
        return category_array

    def is_exist(self,link, c):
        # print(link)
        count = c
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        art = soup.findAll("div", attrs={"class": "article"})
        # print(count)
        if len(art) > 1:
            if count < 10:
                # print(count)
                count += 1
                new_link = "{}{}".format(link[:-1], count)
                return self.is_exist(new_link, count)
            elif count < 100:
                # print(count)
                count += 1
                new_link = "{}{}".format(link[:-2], count)
                return self.is_exist(new_link, count)
            elif count < 1000:
                # print(count)
                count += 1
                new_link = "{}{}".format(link[:-3], count)
                return self.is_exist(new_link, count)
            # return True
        else:
            return count - 1

    def dateCreator(self,d1,d2):
        switch = 0
        dizi = []
        cats = ['category-observer']
        # cats = ['category-observer', 'category-bulgaria', 'category-the-war', 'category-economy','category-foreign-country', 'category-culture', 'sport', 'category-education', 'category-then']
        while switch == 0:
            for m in cats:
                for i in range(188, 2000):
                    url = 'https://www.segabg.com/{}?page={}'.format(m, i)
                    dizi.append(url)
                    r = requests.get(url)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    title = soup.find("li", {"class", "pager-show-more-next first last"}).text.strip()
                    if title.startswith('Няма повече стати'):
                        print(" break thats enough")
                        break
                    else:

                        print(url)
                # print(url)
                switch = 1
        return dizi
        # # All_pages_link=[]
        # p_link = ""
        # for i in range(len(categories_links)):  # categories_links:
        #     category_pages_count = self.is_exist(categories_links[i], 1)
        #     h = categories_links[i]
        #     for j in range(1, category_pages_count + 1, 1):
        #         p_link = "{}{}".format(h[:-1], j)
        #         # All_pages_link.append(p_link)

    def get_link(self,url):
        # r = requests.get(url)
        # soup = BeautifulSoup(r.content, 'html5lib')
        # c_link = soup.findAll("div", attrs={"class": "title"})
        # for i in c_link:
        #     h = i.a.get("href")
        #     last_link = ("{}{}".format("https://www.segabg.com", h))
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find_all("div", {"class", "title"})
        for i in title:
            for j in i:
                lnk = j.get("href")
                # print(links)
                with open(self.link_filname, 'a') as file:
                    file.write(lnk + '\n')






#######################################################



    def creator(self,link):
        link="https://www.segabg.com/article/borisov-se-vrna-gurbet-i-shcho-da-vidi"
        inner_array = []
        atxt = ""
        inner_array.append(link)
        print(link)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            dat = soup.find("div", attrs={"class": "sega-article-date"})
            datem = (dat.getText())
            print(datem)
        except:
            datem="None"

        inner_array.append(datem)
        try:
            title = soup.find("h1", attrs={"class": "sega-title"}).getText()
            print(title)
        except:
            title="None"
        inner_array.append(title)
        try:
            table = soup.find("div", attrs={"class": "sega-body"}).findAll('P')
            cable = soup.findAll("p")
            for j in cable[:-6]:
                if j != " ":
                    # jj=' '.join(j.split())#.stripped_strings
                    atxt+= j.text

                else:
                    print("yyyyy")
        except:
            atxt="None"
        # for i in table:
        # atxt+=i
        # print("---",atxt)
        atxt=' '.join(atxt.split())
        inner_array.append(atxt)
        cdata=""
        cdata="{}{}{}{}{}{}{}".format(inner_array[0], ";", inner_array[1], ";", inner_array[2], ";", inner_array[3])
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])

        # ps = ""
        # with open(self.content_filname, 'a') as file:
        #     # ps="{}{}{}{}{}{}{}".format(pdd[0],";",pdd[1],";",pdd[2],";",pdd[3])
        #     ps = "{}{}{}{}{}{}{}".format(inner_array[0], ";", inner_array[1], ";", inner_array[2], ";", inner_array[3])
        #     print(ps)
        #     file.write(ps + '\n')
        # return inner_array


    def main(self):
        print("*********************")
        print(self.categ)
        print(self.date1)
        print(self.date2)
        self.page_links=self.dateCreator(self.date1,self.date2)
        for i in self.page_links[:]:
            print(i)
            print("*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-**--*-*-*-*-")

        for i in self.page_links[:]:
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