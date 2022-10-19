from encodings import utf_8
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


class vatan:

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
                print("===========================================")
                print(ff)
                print("===========================================")
                self.filname = desktop + "/" + self.dirname#filname
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
                self.filname = desktop + "//" +self.dirname #filname2
                self.content_filname = self.filname + "_content.csv"
                self.link_filname = self.filname + "_link.txt"
            except:
                pass
            
            
    def date_creator(self,count,keyword):
        count=int(count)
        
        print(type(count))
        # print(count) 33333333333333333333
        
        #https://www.gazetevatan.com/api/search/searchcontentloadmore?query=korona&page=2&isFromNewsSearchPage=true   
        
        for i in range(1, int(count)+1): 
            lnk = "https://www.gazetevatan.com/api/search/searchcontentloadmore?query="+keyword+"&page={}&isFromNewsSearchPage=true".format(str(i)) 
            self.links.append(lnk)
            # print(lnk)   
        return self.links
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def getAllLinks(self,url):
        # print(keyword) 
        # print("getalllinks") 44444444444444444
        html = requests.get(url)  
        soup = BeautifulSoup(html.content, "html.parser")
        count=0
        for a in soup.find_all('a', href=True):
            link = a['href']
            result = link.startswith("/")
            if result == True:
                count+=1
                if (count%2==0):
                    if len(link)>20:
                        link="https://www.gazetevatan.com"+link
                        print(link)
                        with open(self.link_filname, 'a', encoding='utf-8') as file:
                            file.write(link + '\n')


                        # print(link)
                        # link_array = link.split("\n")
                        # link_string = ""
                        # for w in link_array:
                        #     link_string = link_string + w
                        #
                        # result = link_string.startswith("https")
                        # if(result == True):
                        #     with open(self.link_filname, 'a' ,encoding='utf-8') as file:
                        #         file.write(link_string+'\n')
                        #         # print(link_string)
                        # else:
                        #     print("Hatalı Link")
        # return "Yazdırılıyor"
    
    # //////////////////////////////////////////////////////////////////////////////////////////////////

    def creator(self,url):
        try:
            # print(url)
            html = requests.get(url)   
            soup = BeautifulSoup(html.content, "html.parser")
            try:
                title = soup.find("h1").getText()
            except:
                title="None"

            try:
                content_array = soup.find("div", {"class": "nd-content-column"}).getText()


                content_array = content_array.split()
                content_string = ""
                for w in content_array:

                    content_string = content_string+" "+w
            except:
                content_string="None"
            try:
                date = soup.find("span", {"class": "hidden-md-up"}).getText()
                date = date.split()
                date = date[1]
                date = date.replace('.', '-')
            except:
                date="None"
            # w_data = url+";"+date+";"+title+";"+content_string
            cdata="{} ; {} ; {} ; {}".format(url,date,title,content_string)
            print(cdata)
            with open(self.content_filname, 'a', encoding='UTF8', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=' ')
                csvwriter.writerow([cdata])

            #write_to_txt(w_data)
            # with open(self.content_filname, 'a',encoding='utf-8') as file:
            #
            #     file.write(w_data+'\n')
        except:
            pass

                
    # //////////////////////////////////////////////////////////////////////////////////////////////////
    def getpagecount(self,keyword):
        print("++++++++++++++++")
        print(keyword)

        try:
            print("Getpagecount") 
            # https://www.gazetevatan.com/api/search/searchcontentloadmore?query=korona&page=2&isFromNewsSearchPage=true 
            url = "https://www.gazetevatan.com/haberleri/"+keyword
            html = requests.get(url).content
            soup = BeautifulSoup(html, "html.parser")
            list = soup.find_all("strong", {"class": "tags__desc-item"})
            list=list[3].getText()
            # print(list)
            count = list.split(" ")
            count = count[0]
            # print(count)
            count = count.replace('.', '')
            
            count=int(count)
            count=count/25
            count+=1
            print(count)
        except:
            return
        return count
    #//////////////////////////////////////////////////////////////////////////////////////////////////
    def main(self):
        print("vatanMain") 
        print("*********************")
        print(self.keyword)

        count = vatan.getpagecount(self,self.keyword)
        self.count = int(count)
        if self.count <= 10:
            counter = 1
        else:
            counter = round(int((self.count / 10) + 1))
        print(counter)

        allLinks = vatan.date_creator(self,self.count,self.keyword)

        for i in range(counter):
            self.getAllLinks(allLinks[i].strip())
            print("get all links............vatan...........")

        print(self.link_filname)


        #
        # t1 = time.time()
        # with concurrent.futures.ProcessPoolExecutor() as execut:
        #     b_res = [execut.submit(
        #         vatan.getAllLinks, i.strip(),self.keyword) for i in allLinks]
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
            #         self.creator, i.strip(),self.keyword) for i in self.newsLinks]
            # print(time.time()-t3)


        
        print("Successfully!")
        

