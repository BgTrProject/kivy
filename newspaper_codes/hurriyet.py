from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
import datetime
from datetime import datetime, timedelta
import numpy as np
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint
from pycode.utils import (BeautifulSoup, Options, UserAgent,webdriver_manager,
                              get, re, sys, time,
                             webdriver)

from pycode.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)
# from kora.selenium import wd  # sorun yaratıyor çöz

class hurriyet:
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
    def is_available(self,url):
        pass

#   https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true
    def dateCreator(self,d1,d2):
        driver = webdriver.Chrome(self.os_find)
        # driver = webdriver.Chrome('/usr/bin/chromedriver')
        # browser=webdriver.Chrome('/usr/bin/chromedriver')
        links = []
        dizi=[]
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        # t1 = datetime(2019, 4, 9)  # en son 1999 05 01 e kadar çalışıyo
        # t2 = datetime(2019, 4, 10)
        # t = timedelta(days=1)
        # dates = np.arange(t1, t2, t).astype(datetime)
        link = "https://www.hurriyet.com.tr/arama/#/?page="  # 1000 e kadar sayfa var kanser

        #fonksiyon oluşturup sayfa sayısını çekmen lazım,
        switch=1
        # count = 0
        # count2 = 0
        # count3 = 0
        # test=[]
        while switch==1:
            for date in dates:
                    for page in range(1,1000):  # page 1 den başlıyo ortalama 70 80 sayfa var her bi günün  ama değişken olduğu için 100 verdim


                        if self.categ=='avrupa' or self.categ=='yerel-haberler' or self.categ=='dunya' or self.categ=='gundem' or self.categ=='ekonomi':
                            newdate = date.strftime('%Y/%m/%d')
                            enddate = pd.to_datetime(newdate) + pd.DateOffset(days=1)
                            enddate = enddate.strftime('%Y/%m/%d')
                            ll=("{}{}{}{}{}{}{}".format(link, page, '&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=', newdate,
                                                                 '&finishDate=', enddate, '&platform=hurriyet&mainCategory=/{}/&isDetail=true').format(self.categ))

                            # driver.get(ll)
                            # soup = BeautifulSoup(driver.page_source, 'html.parser')
                            # url = 'https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true'
                            # driver = webdriver.Chrome('/usr/bin/chromedriver')

                            driver = webdriver.Chrome('/usr/bin/chromedriver')

                            driver.get(ll)
                            time.sleep(1)
                            soup = BeautifulSoup(driver.page_source, 'html.parser')
                            try:
                                title = soup.find("p", {"class": "hs-nr-text"}).getText()
                                if title.startswith("Sonu"):

                                    switch=0
                                    driver.close()
                                    break
                                else:

                                    pass

                            except:
                                pass

                            print(ll)
                            links.append(ll)
                            print(" lllllllllllllllllllllllllllllin alındı   ")




                        else:


                            newdate = date.strftime('%Y/%m/%d')
                            enddate = pd.to_datetime(newdate) + pd.DateOffset(days=1)
                            enddate = enddate.strftime('%Y/%m/%d')
                            lls=("{}{}{}{}{}{}{}".format(link, page, '&where=hurriyet&how=Article&startDate=', newdate,
                                                                 '&finishDate=', enddate, '&platform=hurriyet&isDetail=true'))

                            driver = webdriver.Chrome('/usr/bin/chromedriver')

                            driver.get(lls)
                            time.sleep(1)
                            soup = BeautifulSoup(driver.page_source, 'html.parser')
                            title = soup.find("p", {"class": "hs-nr-text"}).getText()
                            try:
                                title = soup.find("p", {"class": "hs-nr-text"}).getText()
                                if title.startswith("Sonu"):

                                    print(title)
                                    switch=0
                                    driver.close()
                                    break
                                else:
                                    pass


                            except:
                                pass

                            print(lls)
                            links.append(lls)
                            print(" lllllllllllllllllllllllllllllin alındı   ")

                            driver.close()

        return links

   # "https://www.hurriyet.com.tr/arama/#/?page=5&where=hurriyet&how=Article&startDate=2018/10/10&finishDate=2018/10/11&platform=hurriyet&isDetail=true"

    # "https://www.hurriyet.com.tr/arama/#/?page=  5
    # &where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=
    # 01/01/2017
    # &finishDate=
    # 02/01/2017
    # &platform=hurriyet&mainCategory=/ekonomi/&isDetail=true"

    # "https://www.hurriyet.com.tr/arama/#/?page=5&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true"

    def get_link(self,i):
        # with open(self.link_filname, 'a') as file:
        #     file.write(i + '\n')
        sayfa = i
        # browser = wd

        options = get_web_driver_options()
        # options=webdriver.chrome('/usr/bin/chromedriver')
        set_automation_as_head_less(options)
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        # driver = get_chrome_web_driver(options)
        # from fake_useragent import UserAgent

        browser = webdriver.Chrome('/usr/bin/chromedriver')
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')


        # browser=webdriver.Chrome('/usr/bin/chromedriver')
        browser.get(sayfa)
        time.sleep(1)
        test = []
        count = 0
        count2 = 0
        count3 = 0
        dizi = []
        sayfa_kaynağı = browser.page_source
        soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
        for a in soup.find_all('a', href=True):
            count2 += 1
            link = a['href']
            test.append(link)
        for i in test:
            result = i.startswith("http://www.hurriyet.com.tr")
            if result == True:
                if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
                    with open(self.link_filname, 'a') as file:
                        file.write(i + '\n')
                        dizi.append(i)
                    count3 += 1
            count += 1
        browser.refresh()

    def creator(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        try:
            title = soup.find("div", {"class": "container"}).find("h1").getText()  # TİTLE Tamam
        except:
            title="None"# print(title)
        try:
            date = soup.find("span", {"class": "news-date"}).getText()
            date = date[:-6]
            date = date.strip()
        except:
            date="None"
            # print(date)
        try:
            content_array = soup.find("div", attrs={"class": "news-content readingTime"})
            # print(content_array)
            l_content = content_array.getText()
            l_content = l_content.strip()
        except:
            l_content="None"
            # print(l_content[14:])
        cdata = "{} ; {} ; {} ; {}".format(url, date, title, l_content)
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # print(w_data)
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



    #
    #
    # def creator(self,url):
    #     r = requests.get(url)
    #     soup = BeautifulSoup(r.content, 'html5lib')
    #     title = soup.find("h1", attrs={"class": "rhd-article-title"}).getText()
    #     category = soup.find("div", attrs={"class": "rhd-category-box"}).getText()
    #     content_array = soup.find("div", attrs={"class": "rhd-all-article-detail"}).getText()
    #     date = soup.find("span", attrs={"class": "rhd-time-box-text hidden-sm-down"}).getText()
    #     date = date.split()
    #     date = date[2]
    #     content_array = content_array.split()
    #     content_string = ""
    #     stop = "(function(url,"
    #     stop2 = "namespace)"
    #     for w in content_array:
    #         if w == stop or w == stop2:
    #             break
    #         else:
    #             content_string = content_string + " " + w
    #             # w_data = url+";"+date+";"+title+";"+content_string
    #     w_data = "{};{};{};{};{}".format(url, date, category, title, content_string)
    #     print(w_data)
    #     # write_to_txt(w_data)
    #     with open(self.content_filname, 'a') as file:
    #         file.write(w_data + '\n')
