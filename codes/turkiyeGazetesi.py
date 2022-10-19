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

class turkiye:

    def __init__(self, keyword, filname, dirname, os_find, **kwargs):
        # self.date1=date1
        # self.date2=date2
        self.os_find = os_find
        self.dirname = dirname
        self.links=[]
        self.linkNews=[]
        self.newsLinks=[]
        self.filname=filname


        self.keyword=keyword
        # self.url = url
        self.count="5"
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
            self.os_find="/usr/bin/chromedriver"
            try:
                # ff = str(filname)
                # self.filname = desktop + "/" + filname
                ff = str(filname)
                print("===========================================")
                print(ff)
                print("===========================================")
                self.filname = desktop + "/" + self.dirname
                # self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
                #                                                                              self.dirname) + ff  # +"/"+ff

                self.content_filname = self.filname + "_content.csv"
                self.link_filname = self.filname + "_link.txt"
                print(self.link_filname)
            except:
                pass
        else:
            try:
                ff = str(filname)
                self.filname = desktop + "//" + dirname#filname2
                self.content_filname = self.filname + "_content.csv"
                self.link_filname = self.filname + "_link.txt"
                print(self.link_filname)
                print("dsfkslfjsdfsdlfjsdl")
            except:
                pass
            
    
    def date_creator(self,count,keyword):
        count=int(count)
        #https://www.turkiyegazetesi.com.tr/arama?q=amerika&pg=1
        for i in range(1, int(count)+1):
            lnk = "https://www.turkiyegazetesi.com.tr/arama?q=+"+keyword+"&pg={}".format(str(i))
            self.links.append(lnk)

        return self.links
         #/////////////////////////////////////////////////////////////////////////////////////////////////////////
    def getAllLinks(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find("div",{"class":"category_other_list"}).find_all("div",{"class":"cat_item clearfix"})
        for i in  list:
            href = i.find("a").get("href")
            with open(self.link_filname, "a", encoding="utf-8") as file:
                file.write(href+"\n")
        return "Yazdırılıyor"
        #////////////////////////////////////////////////////////////////////////////////////////
    def creator(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1").getText()
        content_array = soup.find("div", attrs = {"class":"article-body"}).getText()
        date = soup.find("div", attrs = {"class":"story_date"}).getText()
        date = date.split()
        date = date[0]
        content_array = content_array.split()
        content_string = ""
        for w in content_array:
            content_string = content_string+" "+w
            #w_data = url+";"+date+";"+title+";"+content_string
        
        cdata="{} ; {} ; {} ; {}".format(url,date,title,content_string)
        with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            csvwriter.writerow([cdata])
        #print(w_data)
        # write_to_txt(w_data)
        # with open(self.content_filname, 'a') as file:
        #     file.write(w_data+'\n')
        #/////////////////////////////////////////////////////////////////////////////////
    def getpagecount(self,keyword):
        print("++++++++++++++++")
        print(keyword)
        
        url ="https://www.turkiyegazetesi.com.tr/arama?q=+"+str(keyword)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        pagecount =soup.find("div",{"class":"sayfalama"}).find_all("a")
        count = pagecount[-1].get("href")
        count = count.rpartition("pg=")
        count = count[2]
        return count
        #//////////////////////////////////////////////////////////////////////////////
    def main(self):
        print("*********************")
        print(self.keyword)
        
        count = turkiye.getpagecount(self,self.keyword)
        
        self.count = int(count)
        if self.count<=10:
            counter=1
        else:
            counter = round(int((self.count / 10) + 1))
        print(counter)

        allLinks = turkiye.date_creator(self,self.count,self.keyword)

        for i in range(counter):
            self.getAllLinks(allLinks[i].strip())
            print("get all links............türkiye gazetesi...........")

        print(self.link_filname)



        # t1 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         self.getAllLinks, i.strip(),self.keyword) for i in allLinks]
        # print(time.time()-t1)
        
        with open(self.link_filname,'r',newline='') as f:
            for i in f.readlines():    
                self.newsLinks.append(i)

        print("-----------------------")
        print(self.content_filname)
        print(self.link_filname)
        print("-------------------------")
        # # for i in self.newsLinks:
        # #     print(i.strip())
        #
        for i in self.newsLinks[:]:
            self.creator(i.strip())
        # t3 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         turkiyeGazetesi2.creator, i.strip(),self.keyword) for i in self.newsLinks]
        # print(time.time()-t3)
        
        print("Successfully!")
        


