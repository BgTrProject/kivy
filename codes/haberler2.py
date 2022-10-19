from unicodedata import category
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
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
newsLinksAll = []


class haberler2:
    
    def __init__(self,keyword,filname,start_date,end_date):
        self.start_date=start_date
        self.end_date=end_date
        self.links=[]
        self.linkNews=[]
        self.newsLinks=[]
        self.filname=filname


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
                self.filname = desktop + "/" + filname
                self.content_filname = self.filname + "_content.txt"
                self.link_filname = self.filname + "_link.txt"
                print(self.link_filname)
            except:
                pass
        else:
            ff = str(filname)
            self.filname = desktop + "//" + filname2
            self.content_filname = self.filname + "_content.txt"
            self.link_filname = self.filname + "_link.txt"
            print(self.link_filname)

    def date_creator(self,start_date, end_date):
        url = "https://www.haberler.com/arsiv/{}/haberler/s1/"
        num = 1
        if(end_date == ""):
            an = datetime.now()
            yearEnd = an.year
            monthEnd = an.month
            dayEnd = an.day
        else:
            end_date = end_date.split('-')
            yearEnd = end_date[0]
            monthEnd = end_date[1]
            dayEnd = end_date[2]
            an = datetime.now()
            if(int(yearEnd) > an.year):
                yearEnd = an.year
                monthEnd = an.month
                dayEnd = an.day
        if(start_date == ""):
            yearStart = "2006"
            monthStart = "6"
            dayStart = "1"
        else:
            start_date = start_date.split('-')
            yearStart = start_date[0]
            monthStart = start_date[1]
            dayStart = start_date[2]
            if(int(yearStart) < 2006):
                yearStart = "2006"
                if(int(monthStart) < 6):
                    monthStart = "6"
        if(monthStart[0] == "0"):
            monthStart = monthStart[1]
        if(dayStart[0] == "0"):
            dayStart = dayStart[1]
        monthEnd = str(monthEnd)
        if(monthEnd[0] == "0"):
            monthEnd = monthEnd[1]
        dayEnd = str(dayEnd)
        if(dayEnd[0] == "0"):
            dayEnd = dayEnd[1]
        t1 = datetime(int(yearStart), int(monthStart),
                      int(dayStart))  

        t2 = datetime(int(yearEnd), int(monthEnd), int(dayEnd))  

        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        for j in dates:
            new_url = (url.format(j.strftime('%d-%m-%Y'), num))
            links.append(new_url)
        return links

    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def getAllLinks(self,url):
        r = requests.get(url).content
        soup = BeautifulSoup(r, "html.parser")
        array = []
        span = ""
        if not soup.find("div", {"class": "hbPagination"}):
            linkNews.append(url)
        else:
            p_count = soup.find(
                "div", {"class": "hbPagination"}).find_all("span")
            for i in p_count:
                span = i.getText()
                array.append(span)

            page_num = len(array)-1
            new_url = url
            new_url = new_url.replace("s1", "s{}")

            for i in range(page_num):
                i = str(i+1)
                lnk = new_url.format(i)
                linkNews.append(lnk)
        return linkNews
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def news_getLink(url,keyword):
        r = requests.get(url)  
        soup = BeautifulSoup(r.content, 'html.parser')
        list = soup.find_all("a", {"class": "hbBoxMainText"})
        for i in list:
            link = i['href']
            url  =   "https://www.haberler.com"
            linkson = "{}{}".format(url,link)
            with open("url/haberlercomLinks_"+keyword+".txt", "a", encoding="utf-8") as file:
                file.write(linkson+"\n")

    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def creator(url, keyword):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        
        title = soup.find("h1").getText()
        date = soup.find("time", {"class": "hbptDate"}).getText()
        date = date.split(" ")
        date = date[0]
        date = date.replace(".","-")
        category = soup.find("div",attrs={"class":"hbptTagDate"})
        category = category.find("a")['title']
        content_string =""
        content = soup.find("main", {"class": "hbptContent"}).find_all('p')
        for i in content:
            content_string += i.getText()
        w_data = "{} ; {} ; {} ; {} ; {}".format(url, category, date, title, content_string)
        with open("content/haberlerContent_"+keyword+".txt", "a", encoding="utf-8") as file:
            file.write(w_data+"\n")

    # //////////////////////////////////////////////////////////////////////////////////////////////////
    
    def main(start_date,end_date,keyword):
        print("Start Date : " + start_date)
        print("End Date : " + end_date)
        print("Keyword : " + keyword)
        dateLinks = haberler2.date_creator(start_date, end_date)  # tarih
        for  i in dateLinks:
            newsLinks.append(haberler2.getAllLinks(i))
        print("Creating links")
        for j in range(0,len(newsLinks)):
            t1 = time.time()
            with concurrent.futures.ProcessPoolExecutor() as execut:
                b_res = [execut.submit(
                    haberler2.news_getLink, i.strip(), keyword) for i in newsLinks[j]]
            print("Links successfully pulled!!")
            print(time.time()-t1)
        
        with open("url/haberlercomLinks_"+keyword+".txt",'r',newline='') as f:
            for i in f.readlines():    
                newsLinksAll.append(i)
        print("Creating Content")
        t3 = time.time()
        with concurrent.futures.ProcessPoolExecutor() as execut:
            b_res = [execut.submit(
                haberler2.creator, i.strip(),keyword) for i in newsLinksAll]
        print(time.time()-t3)
        print("Content successfully pulled!!")
        
        

