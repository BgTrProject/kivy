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
from datetime import datetime, timedelta,date



class duvar:
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
        #
        # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
        #                                                                              self.dirname) + ff  # +"/"+ff
        # self.content_filname = self.filname + "_content.txt"
        self.content_filname = self.filname + "_content.csv"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)


# https://www.gazeteduvar.com.tr/arsiv?&tarih_baslangic=22.07.2015&tarih_bitis=22.07.2021&kategoriler[]=5f6f684508038f7697471493&siralama=1&sayfa=1
# https://www.gazeteduvar.com.tr/arsiv?&tarih_baslangic=22.07.2015&tarih_bitis=22.07.2021&siralama=0&sayfa=1


    def dateCreator(self,d1,d2):
        u1="https://www.gazeteduvar.com.tr/arsiv?"
        u2="&tarih_baslangic="
        u3="&tarih_bitis="
        u4="&siralama=0&sayfa="
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        dizi=[]
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        counter=1
        for i in dates:
            print("------------------------")
            print(i)
            print("------------------------")
            i = i.strftime('%d.%m.%Y')
            print("------------------------")
            print(i)
            print("------------------------")
            switch=0
            while switch==False:
                # uur='{}{}{}{}'.format(u1,u2,u3,u4)
                if len(self.categ)>107:
                    url=self.categ
                    try:
                        print("I am here ")
                        html = requests.get(url).content
                        # # date=url[37:]
                        soup = BeautifulSoup(html, "html.parser")
                        list2 = soup.find_all("div", {"class": "alert alert-danger"})
                        dizi.append(url)
                        counter += 1
                        if len(list2) > 0:
                            switch = True
                            break
                        else:
                            pass


                        # for i in list:
                        #     if len(i.text) == 52:
                        #         break
                        #     else:
                        #         counter += 1
                        #         dizi.append(url)
                    except:
                        pass
                else:
                    try:
                        u2 = '&tarih_baslangic={}'.format(t1)
                        u3 = '&tarih_bitis={}'.format(t2)
                        new_url = '{}{}{}{}{}'.format(u1, u2, u3, u4, counter)
                        print(new_url)

                        html = requests.get(new_url).content
                        # # date=url[37:]
                        soup = BeautifulSoup(html, "html.parser")
                        list = soup.find_all("div", {"class": "alert alert-danger"})
                        print(list)
                        dizi.append(new_url)
                        counter += 1
                        if len(list) > 0:
                            switch = True
                            break
                        else:
                            pass


                        # for i in list:
                        #     print("//////////////////////////////////")
                        #     print(i)
                        #     h=soup.find('p',{"class":"mb-0"}).text
                        #     print("******************************")
                        #     print(h)
                        #     print(len(h))
                        #     print(type(len(h)))
                        #     print("******************************")
                        #     if len(h) != 50:
                        #         counter += 1
                        #         dizi.append(new_url)
                        #         print(new_url)
                        #         print("xxxxxxxxxxxxxxxxxxxxxxxllllllllxlxlxlx")
                        #
                        #
                        #
                        #     else:
                        #         switch = True
                        #         break

                                # counter+=1
                                # dizi.append(new_url)
                                # print(new_url)

                    except:
                        pass

        return dizi #kanser_links, memekanseri_links, prostat_links, tamamı_links


    def get_link(self,url):
        html = requests.get(url).content
        # # date=url[37:]
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find_all("div", {"class": "col-12 col-lg mw0"})
        for i in list:
            h = soup.find_all('a', {"class": "box archive-box image-left_text-right"})
            for j in h:
                wdata=j.get("href")
         # print(wdata)
                with open(self.link_filname, "a", encoding="utf-8") as file:
                    file.write(wdata + "\n")
        # except:
            pass



    def creator(self,url):
        html = requests.get(url).content
        # # date=url[37:]
        soup = BeautifulSoup(html, "html.parser")
        try:
            list = soup.find_all("div", {"class": "content-text max-width"})
        except:
            pass
        try:

            date = soup.find("div", {"class": "info"}).text
            date = date.strip()
            date = date[:-6]
        except:
            date="0000"
        try:
            title = soup.find("h1", ).text
        except:
            title="None"
        # print(title)
        # print(date[:-6])
        counter = 0
        txt = ''
        try:
            for i in list:
                if counter > 0:
                    break
                else:
                    h = soup.find_all('p')
                    for j in h:
                        txt += j.text.strip()
                        # print(h.text.strip())
                        # print(j.text)
                counter += 1
        except:
            txt="None"

        cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(cdata + "\n")
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])

    def main(self):
        print("************ started to collect page links")

        self.page_links = self.dateCreator(self.date1, self.date2)
        print("-------- all links---")

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

        for i in self.newsLinks[:]:
            self.creator(i.strip())

        print("Successfully!")

        # def dateCreator(self, d1, d2):
        #     u1 = "https://www.gazeteduvar.com.tr/arsiv?"
        #     u2 = "&tarih_baslangic="
        #     u3 = "&tarih_bitis="
        #     u4 = "&siralama=0&sayfa="
        #     t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        #     t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        #     dizi = []
        #     t = timedelta(days=1)
        #     dates = np.arange(t1, t2, t).astype(datetime)
        #     counter = 1
        #     for i in dates:
        #         while True:
        #             i = i.strftime('%d.%m.%Y')
        #             if len(int(self.categ) > 107):
        #                 url = self.categ
        #                 try:
        #                     html = requests.get(url).content
        #                     # # date=url[37:]
        #                     soup = BeautifulSoup(html, "html.parser")
        #                     list = soup.find_all("div", {"class": "alert alert-danger"})
        #                     for i in list:
        #                         if len(i.text) == 52:
        #                             break
        #                         else:
        #                             counter += 1
        #                             dizi.append(url)
        #                 except:
        #                     pass
        #             else:
        #                 u2 = '{}{}'.format(u2, t1)
        #                 u3 = '{}{}'.format(u2, t2)
        #                 url = '{}{}{}{}{}'.format(u1, u2, u3, u4, counter)
        #
        #                 try:
        #                     html = requests.get(url).content
        #                     # # date=url[37:]
        #                     soup = BeautifulSoup(html, "html.parser")
        #                     list = soup.find_all("div", {"class": "alert alert-danger"})
        #                     for i in list:
        #                         if len(i.text) == 52:
        #                             break
        #                         else:
        #                             counter += 1
        #                             dizi.append(url)
        #                 except:
        #                     pass
        #     return dizi  # kanser_links, memekanseri_links, prostat_links, tamamı_links