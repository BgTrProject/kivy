import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import time
import sys
import urllib.request
import re
import urllib3
from pandas import DataFrame
import csv
import datetime
from datetime import datetime, timedelta, date
import concurrent
import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor
import mimetypes
# from django.http.response import HttpResponse
# from django.shortcuts import redirect
import dtale


links = []
linkNews = []
newsLinks = []


class dailysabah:

    def __init__(self, keyword, filname, dirname, os_find, **kwargs):
        # self.date1=date1
        # self.date2=date2
        self.os_find = os_find
        self.dirname=dirname
        self.links = []
        self.linkNews = []
        self.newsLinks = []
        self.filname = filname
        self.keyword = keyword
        # self.url = url
        self.count = "5"
        print(self.keyword)
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)

        print(self.filname)
        ff = str(self.dirname)
        self.filname = desktop + '/' + ff
        print("---*-*-*-*-*------------*-*-*-*-*")
        print(self.filname)

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        print("?????????????????")
        print(self.filname)
        filname2 = self.filname
        if (h.startswith("/home")):
            try:


                ff = str(filname)
                print("===========================================")
                print(ff)
                print("===========================================")
                self.filname = desktop + "/" + self.dirname
                # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,self.dirname) + ff#+"/"+ff
                self.content_filname = self.filname + "_content.csv"
                self.link_filname = self.filname + "_link.txt"
                print(self.link_filname)
            except:
                pass
        else:
            ff = str(filname)
            self.filname = desktop + "//" + self.dirname
            self.content_filname = self.filname + "_content.csv"
            self.link_filname = self.filname + "_link.txt"
            print(self.link_filname)

    def date_creator(self, count, keyword):
        count = int(count)

        print(type(count))
        # https://www.dailysabah.com/search?query=corona&pgno=2
        for i in range(1, int(count) + 1):
            lnk = "https://www.dailysabah.com/search?query=" + keyword + "&pgno={}".format(
                str(i))
            self.links.append(lnk)
            # print(lnk)
        return self.links

    def getAllLinks(self, url):
        # print(keyword)
        print("get all links***************************")
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find("div", {"class": "list_with_rectangle_image search_results"}).find_all(
            "div", {"class": "widget_content"})
        for i in list:
            href = i.find("h3").find("a").get("href")
            print(href)
            print("hrrrrrrrrrrrrrrrrrrrrrrrrrrrrrreeeeeeeeeeeeeeeefffffffffffff")
            with open(self.link_filname, "a", encoding="utf-8") as file:
                file.write(href + "\n")
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # # filepath = BASE_DIR + '/g_upload/' + self.link_filname
        # filepath=self.link_filname
        # print(filepath)
        # # Open the file for reading content
        # path = open(filepath, 'rb')
        # # Set the mime type
        # mime_type, _ = mimetypes.guess_type(filepath)
        # # Set the return value of the HttpResponse
        # response = HttpResponse(path, content_type=mime_type)
        # # Set the HTTP header for sending to browser
        # response['Content-Disposition'] = "attachment; filename=%s" % self.link_filname
        # h = dtale.show()
        # h.main_url()
        # return response

    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def creator(self, url):
        print("startttttttttttttttt")

        print(url)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("div", {"class": "top_title_widget"}).find("h1").getText().strip()
        # top_title_widget
        # h1--> main_page_title
        # title = soup.find("div", {"class": "nd-article__title"}).find("h1").getText().strip()  # title tamam
        content = soup.find("div", {"class": "article_body"})
        date = soup.find("div", {"class": "left_mobile_details"})
        categori = "Science"
        content_string = ""
        print(title)
        print(date)
        if date == None:
            date = ""
        else:
            date = soup.find("div", {"class": "left_mobile_details"}).find_all("span")
            if (len(date) == 2):
                date = date[1].getText().strip()
                date = date[:-15].replace(",", "")
                date = date.strip()
                print(date)
            else:
                date = date[2].getText().strip()
                date = date[:-16].replace(",", "")
                date = date.strip()
                print(date)

        if content == None:
            return
        else:
            content = soup.find("div", {"class": "article_body"}).find_all("p")
            for i in content:
                i = i.getText().replace(" ", " ")
                z = " ".join(i.split())
                content_string += z

        if content_string != "":
            content = soup.find("div", {"class": "article_body"}).getText()
            content = content.strip()
            content = " ".join(content.split())
            content_string = content

        print(title)
        print(content_string)
        print(categori)

        cdata = "{} ; {} ; {} ; {}".format(url, date,  title, content_string) # categori çıkarıldı
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])




        # print(sentence)
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(sentence + "\n")

        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # # filepath = BASE_DIR + '/g_upload/' + self.content_filname
        # filepath_c=self.content_filname
        # print(filepath_c)
        # # Open the file for reading content
        # path = open(filepath_c, 'rb')
        # # Set the mime type
        # mime_type, _ = mimetypes.guess_type(filepath_c)
        # # Set the return value of the HttpResponse
        # response = HttpResponse(path, content_type=mime_type)
        # # Set the HTTP header for sending to browser
        # response['Content-Disposition'] = "attachment; filename=%s" % self.content_filname
        # h = dtale.show()
        # h.main_url()
        # return response

    # //////////////////////////////////////////////////////////////////////////////////////////////////
    def getpagecount(self, keyword):
        print("++++++++++++++++")
        print(keyword)

        url = "https://www.dailysabah.com/search?query=" + str(keyword)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        count = soup.find("div", {"class": "search_count"}).getText()
        count = count.split(" ")
        count = count[1]
        # print(count)

        return count

    # //////////////////////////////////////////////////////////////////////////////////////////////////
    def main(self):  # keyword
        print("*********************")
        print(self.keyword)
        # keyword=self.keyword
        count = dailysabah.getpagecount(self, self.keyword)

        self.count = int(count)
        print(self.count)
        counter=round(int((self.count/10)+1))
        print(counter)

        allLinks = dailysabah.date_creator(self, self.count, self.keyword)
        t1 = time.time()
        for i in range(counter):
            self.getAllLinks(allLinks[i].strip())
            print("get all linksssssssssssssssssssssssssssssssss")

        print(self.link_filname)


        #
        # with concurrent.futures.ProcessPoolExecutor(max_workers=5) as execut:
        #     b_res = [execut.submit(
        #             self.getAllLinks, i.strip(),self.keyword) for i in allLinks]
        # print(time.time()-t1)
        #
        # print(self.link_filname)
        #
        with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                self.newsLinks.append(i)
        #
        # t3 = time.time()
        print("-----------------------")
        print(self.content_filname)
        print(self.link_filname)
        print("-------------------------")
        # # for i in self.newsLinks:
        # #     print(i.strip())
        #
        for i in self.newsLinks[:]:
            self.creator(i.strip())
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         self.creator, i.strip(), self.keyword) for i in self.newsLinks]
        # print(time.time() - t3)

        print("Successfully!")





    # def main(self):  # keyword
    #     print("*********************")
    #     print(self.keyword)
    #     # keyword=self.keyword
    #     count = dailySabah.getpagecount(self, self.keyword)
    #
    #     self.count = int(count)
    #
    #     allLinks = dailySabah.date_creator(self, count, self.keyword)
    #     t1 = time.time()
    #
    #     #
    #     # with concurrent.futures.ProcessPoolExecutor(max_workers=5) as execut:
    #     #     b_res = [execut.submit(
    #     #         self.getAllLinks, i.strip(),self.keyword) for i in allLinks]
    #     # print(time.time()-t1)
    #
    #     # print(self.link_filname)
    #
    #     with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
    #         for i in f.readlines():
    #             self.newsLinks.append(i)
    #
    #     t3 = time.time()
    #     print("-----------------------")
    #     print(self.content_filname)
    #     print(self.link_filname)
    #     print("-------------------------")
    #     # for i in self.newsLinks:
    #     #     print(i.strip())
    #
    #     with concurrent.futures.ProcessPoolExecutor() as execut:
    #         b_res = [execut.submit(
    #             self.creator, i.strip(), self.keyword) for i in self.newsLinks]
    #     print(time.time() - t3)
    #
    #     print("Successfully!")


