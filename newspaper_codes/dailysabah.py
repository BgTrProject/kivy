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


#https://www.dailysabah.com/search?qlimit=by_fifty&pgno=4903&qsort=oldest
class dailysabah:
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


        # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/dailysabah_searchs/dailysabah_searchs_dailysabah"

        # self.content_filname = self.filname + "_content.txt"
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)

    def page_number(self,url):
        numb=""
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            dizinumb = soup.find_all("a",{"class": "page_number"})
            numb=int(dizinumb[-1].text)
            # print(type(numb))
            print(numb)
        except:
            pass
        return numb

    def dateCreator(self,d1,d2):
        dizi=[]
        if self.categ.startswith("all") or self.categ.startswith(" "):
            url = 'https://www.dailysabah.com/search?qlimit=by_fifty&pgno=1&qsort=oldest'
            p_numb = self.page_number(url)
            for i in range(p_numb):
                new_url='https://www.dailysabah.com/search?qlimit=by_fifty&pgno={}&qsort=oldest'.format(i)
                dizi.append(new_url)
        # elif self.categ.startswith("politics") or  self.categ.startswith("environment") or self.categ.startswith("turkey") or self.categ.startswith("world") or self.categ.startswith("businees") or self.categ.startswith("lifestyle") or self.categ.startswith("arts") or self.categ.startswith("sports") or self.categ.startswith("gallery") or self.categ.startswith("opinion") :
        #     url='https://www.dailysabah.com/search?qsubsection={}'.format(self.categ)

        else:
            cat=self.categ.split(',')

            try:
                for c in cat:
                    url='https://www.dailysabah.com/search?qsubsection={}&pgno=1'.format(c)
                    p_numb = self.page_number(url)
                    for i in range(p_numb):
                        new_url='https://www.dailysabah.com/search?qsubsection={}&pgno={}'.format(c,i)
                        dizi.append(new_url)
            except:
                url='https://www.dailysabah.com/search?qsubsection=science&pgno=1'
                p_numb=self.page_number(url)
                for i in range(p_numb):
                    new_url='https://www.dailysabah.com/search?qsubsection=science&pgno={}'.format(self.categ,i)
                    dizi.append(new_url)
        # url='https://www.dailysabah.com/search?qlimit=by_fifty&pgno=4903&qsort=oldest'
        # for i in range(1,4094):
        #     url='https://www.dailysabah.com/search?qlimit=by_fifty&pgno={}&qsort=oldest'.format(i)
        #     dizi.append(url)
        return dizi
    def get_link(self,url):
        # url="https://www.dailysabah.com/search?qlimit=by_fifty&pgno=4903&qsort=oldest"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        links = soup.find("ul", attrs={"class": "items_list"}).find_all('a')
        counter = 0
        for i in links:
            counter += 1
            if counter % 2 == 1:
                link=i.get("href")
                print(link)
                with open(self.link_filname, 'a') as file:
                    # print(link)
                    file.write(link + '\n')
            else:
                pass
    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        h= url.split('/')
        categ=h[3]
        try:

            title = soup.find("h1", {"class", "main_page_title"}).getText().strip()
        except:
            title="None"
        # print(title)
        try:
            date = soup.find("div", attrs={"class": "left_mobile_details"}).getText()  # "sc-DlApP"}).getText()
            date = date.split()
            date = date[4] + "-" + date[5][:-1] + "-" + date[6]
            date = date
        except:
            date="None"
        try:
            text = soup.find("div", attrs={"class": "article_body"})
            txt = ''
            for i in text.stripped_strings:
                txt += i.strip()
        except:
            txt="None"

        cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt) #categ çıkarıldı
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # print(cdata)
        # with open(self.content_filname, 'a') as file:
        #     file.write(cdata + '\n')

    def main(self):
        print("************ started to collect page links")

        self.page_links=self.dateCreator(self.date1,self.date2)
        print("-------- all links---")


        for i in self.page_links[:]:
            print(i)
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
