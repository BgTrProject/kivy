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
import concurrent
import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor

links = []
linkNews = []
newsLinks = []


class sabah:
    def __init__(self, keyword, filname, dirname, os_find, **kwargs):
        # self.date1=date1
        # self.date2=date2
        self.os_find = os_find
        self.dirname = dirname
        self.links = []
        self.linkNews = []
        self.newsLinks = []
        self.filname = filname
        self.keyword = keyword
        # self.url = url
        # self.count = "5"
        print(self.keyword)


        self.keyword=keyword
        # self.url = url
        self.count="2"
        print(self.keyword)
        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h=os.getcwd()
        print("?????????????????")
        print(self.filname)
        filname2 = self.filname
        if (h.startswith("/home")):
            try:
                ff = str(filname)
                self.filname = desktop + "/" + self.dirname
                self.content_filname = self.filname + "_content.csv"
                self.link_filname = self.filname + "_link.txt"
                print(self.link_filname)
            except:
                pass
        else:

            ff = str(filname)
            self.filname = desktop + "\\" + self.dirname
            self.content_filname = self.filname + "_content.csv"
            self.link_filname = self.filname + "_link.txt"
            print(self.link_filname)

    def date_creator(self,count,keyword):
        count=int(count)
        print(type(count))
        for i in range(1, int(count)+1):
            lnk = "https://www.sabah.com.tr/get/arama?query="+keyword+"&page={}".format(
                str(i))
            self.links.append(lnk)
            print(lnk)
        return self.links
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def getAllLinks(self,url):
        # print("Girdiiiiiii")
        # print(keyword)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find_all("figure", {"class": "multiple"})
        # print(list)
        for i in list:
            href = i.find("a").get("href")
            if str(href).startswith("http"):
                href=href
            else:
                # print(href)
                href = "https://www.sabah.com.tr"+href
                # print(href)
            with open(self.link_filname, "a", encoding="utf-8") as file:
                file.write(href+"\n")
                print(href)
        
        # return "Yazdırılıyor"
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def creator(self,url):
        # url="https://www.sabah.com.tr/galeri/spor/son-dakika-portekiz-turkiye-maci-oncesi-neler-yasandi-futbolculardan-biri-stefan-kuntza-gidip-sabah-spor-ozel"
        # print(url)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        try:
            title = soup.find("h1", {"class": "pageTitle"}).getText().strip()  # title tamam
        except:
            title="None"
        # print(title)
        try:
            content = soup.find("div", {"class": "imgList view20"}).get_text()
            # content = soup.find("div", {"class": "newsBox selectionShareable"})
            content_array = content.split()
            content_string = ""
            for w in content_array:
                content_string = content_string+" "+w
        except:
            content_string="None"
        print(content_string)
        try:
            date = soup.find("div", {"class": "view20"}).get_text().split()
            categori = "Galeri"
            date = date[2]
            date = date.replace('.', '-')
        except:
            date="None"
        print(date)

        cdata = "{} ; {} ; {} ; {}".format(url, date,  title, content_string) #categori çıkarıldı
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        # with open(self.content_filname, "a", encoding="utf-8") as file:
        #     file.write(sentence+"\n")
            
    # //////////////////////////////////////////////////////////////////////////////////////////////////
    def getpagecount(self,keyword):
        print("++++++++++++++++")
        print(keyword)
        
        url = "https://www.sabah.com.tr/arama?query="+str(keyword)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        count = soup.find("div", {"class": "searchPageCaption"}).find("span").getText()
        count=int(count)/6
        print(count)
        # count=1
        return count
    #//////////////////////////////////////////////////////////////////////////////////////////////////
    def main(self):
        
        count = sabah.getpagecount(self,self.keyword)
        
        self.count = int(count)
        counter = round(int((self.count / 10) + 1))
        print(counter)

        allLinks = sabah.date_creator(self,count,self.keyword)
        
        t1 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         self.getAllLinks, i.strip(),self.keyword) for i in allLinks]
        # print(time.time()-t1)

        for i in range(counter):
            self.getAllLinks(allLinks[i].strip())
            print("get all linksssssssssssssssssssssssssssssssss")

        print(self.link_filname)


        with open(self.link_filname,'r',newline='') as f:
            for i in f.readlines():    
                self.newsLinks.append(i)
        
        # t3 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         self.creator, i.strip(),self.keyword) for i in newsLinks]
        # print(time.time()-t3)
        print("-----------------------")
        print(self.content_filname)
        print(self.link_filname)
        print("-------------------------")
        # # for i in self.newsLinks:
        # #     print(i.strip())
        #
        for i in self.newsLinks[:]:
            self.creator(i.strip())
        print("Successfully!")
        

