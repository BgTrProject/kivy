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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pycode.utils import (BeautifulSoup, Options, UserAgent,webdriver_manager,
                              get, re, sys, time,
                             webdriver)

from pycode.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)


class cumhuriyet:
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

    #https://www.cumhuriyet.com.tr/dunya
    def dateCreator(self, d1, d2):
        dizi=[]
        #  cat=['gundem','dunya','ekonomi','yasam','spor','siyaset','bilim-teknoloji']
        cat=['dunya']
        # for i in cat:
        #     if self.categ==i:
        #
        #         url = 'https://www.cumhuriyet.com.tr/'
        #         new_url = '{}{}'.format(url, self.categ)
        #         dizi.append(new_url)
        #     else:
        #         pass


        for i in cat:
            url='https://www.cumhuriyet.com.tr/'
            new_url='{}{}'.format(url,i)
            dizi.append(new_url)
            print(new_url)
        return dizi
    def get_link(self,url):

        # driver = webdriver.Chrome('/usr/bin/chromedriver')
        driver = webdriver.Chrome(self.os_find)
        driver.get(url)
        time.sleep(1)
        # SCROLL_PAUSE_TIME = 10
        more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
        more.click()
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # print(len(more))
        browser = driver
        lastHeight = browser.execute_script("return document.body.scrollHeight")
        i = 0
        dizi = []
        while True:
            try:
                # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
                more.click()
                time.sleep(1)

                # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # time.sleep(2)
                # browser.find_element_by_css_selector('.button .c_button .s_button').click()
                newHeight = browser.execute_script("return document.body.scrollHeight")  # scroll ile aşağı inme işlemi
                print(i)
                print("nnnnnnnnnnnnnnnnnnnnn")
                print(newHeight)
                print(lastHeight)
                print("llllllllllllllll")
                if newHeight == lastHeight:
                    time.sleep(1)
                    print("finishedddddddddddddddd")
                    sayfa_kaynağı = browser.page_source
                    soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
                    list = soup.find_all('div', {"class": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
                    time.sleep(4)
                    for i in list:
                        sayac = 0
                        for j in i:
                            for m in j:
                                for n in m:
                                    if type(n) != "str":
                                        # print(n)
                                        z = str(n)
                                        if (z.startswith("<a href")):
                                            h = z.split('?')
                                            hh = h[0]
                                            hh = hh[9:]
                                            # print(hh)
                                            sayac += 1
                                            if sayac % 2 == 1:
                                                # print(sayac)
                                                url = "https://www.cumhuriyet.com.tr"
                                                new_url = '{}{}'.format(url, hh)
                                                print(new_url)
                                                with open(self.link_filname, 'a') as file:
                                                    file.write(new_url + '\n')
                                            else:
                                                pass
                                        else:
                                            pass
                                    else:
                                        pass
                    break
                else:
                    lastHeight = newHeight
                more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
                more.click()
                i = i + 1


            except:
                break

    def creator(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        try:
            title = soup.find("h1", {"class": "baslik"}).text.strip()
            print(title)

            date = soup.find("div", {"class": "yayin-tarihi"}).text.strip()
            date = date[:-7]
            date = date.strip()
            print(date)
            list = soup.find("div", {"class": "haberMetni"}).find_all('p')
            txt = ""
            for i in list:
                txt += i.text.strip()
            #         txt+=i.text
            cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)
            with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=' ')
                csvwriter.writerow([cdata])
            # with open(self.content_filname, 'a') as file:
            #     file.write(cdata + '\n')
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
