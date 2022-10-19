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


class bgnes:
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


        ###################################
    def headermenuitemfinder(self,link):
        category_array = []
        req = requests.get(link)
        soup = BeautifulSoup(req.content, "lxml")
        title = soup.findAll("a", attrs={"class": "main_nav__link"})
        title2 = soup.findAll("a", attrs={"class": "main_nav__dropdown_link"})
        for i in title:
            b = i.get("href")
            category_array.append("{}{}".format("https://bgnes.bg", b))
        for i in title2:
            c = i.get("href")
            category_array.append("{}{}".format("https://bgnes.bg", c))
        return category_array

    def pagecountfinder(self,link):
        p_c_array = []
        req = requests.get(link)
        soup = BeautifulSoup(req.content, "lxml")
        title = soup.find("li", attrs={"class": "MarkupPagerNavLastNum"})
        p_c_array.append(title.a.getText())
        return p_c_array

    def link_creator(self,c_array):
        all_link = []
        for i in range(len(c_array)):

            c = self.page_counts[i]
            h = int(c[0])
            print(h)
            print(type(h))
            for j in range(h):
                ll = "{}{}{}".format(self.categories_array[i], "page", j + 1)
                all_link.append(ll)
        return all_link
###########|-------------------------------------------
    def dateCreator(self, d1, d2):
        url = "https://bgnes.bg/"
        self.cat_array = self.headermenuitemfinder(url)
        for i in self.cat_array[1:]:
            self.categories_array.append(i)

        for i in self.categories_array:
            self.page_counts.append(self.pagecountfinder(i))
        dizi = self.link_creator(self.page_counts)

        #
        #
        # t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        # t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        # t = timedelta(days=1)
        # txt = ""
        # url = "https://trud.bg/%D0%B0%D1%80%D1%85%D0%B8%D0%B2/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/?date="
        # dates = np.arange(t1, t2, t).astype(datetime)
        # dizi = []
        # for i in dates:
        #     txt = "{}{}".format(url, i.date())
        #     dizi.append(txt)
        return dizi

    def get_link(self, link):
    # def pageslinkcreator(link):
        plink_array = []
        req = requests.get(link)
        soup = BeautifulSoup(req.content, "lxml")
        title = soup.findAll("h3", attrs={"class": "mb-3 posts__item_head"})
        # title2=soup.findAll("a",attrs={"class":"main_nav__dropdown_link"})
        for i in title:
            b = i.a.get("href")
            new_link = "{}{}".format("https://bgnes.bg", b)
            # plink_array.append(new_link)
            ps = new_link
            print(ps)
            with open(self.link_filname, 'a') as file:
                file.write(ps + '\n')
        # return plink_array

    def creator(self,link):
        inner_array = []
        atxt = ""
        inner_array.append(link)
        print(link)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        dat = soup.find("div", attrs={"class": "news_metadata mb-4"})
        datem = (dat.span.getText("span"))
        print(datem[-19:-9])

        inner_array.append(datem[-19:-9])
        title = soup.find("h1", attrs={"class": "headline"}).getText()
        print(title)
        inner_array.append(title)
        table = soup.findAll("div", attrs={"class": "body_matrix__body__inner"})
        for i in table:
            atxt += i.p.getText()
        print(atxt)
        inner_array.append(atxt)
        # ps = ""
        # with open(self.content_filname, 'a') as file:
        #     # ps="{}{}{}{}{}{}{}".format(pdd[0],";",pdd[1],";",pdd[2],";",pdd[3])
        #     ps = "{}{}{}{}{}{}{}".format(inner_array[0], ";", inner_array[1], ";", inner_array[2], ";", inner_array[3])
        #     file.write(ps + '\n')
        # # return inner_array
        cdata = ""
        cdata = "{}{}{}{}{}{}{}".format(inner_array[0].strip(), " ; ", inner_array[1].strip(), " ; ",
                                        inner_array[2].strip(), " ; ", inner_array[3].strip())
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])

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