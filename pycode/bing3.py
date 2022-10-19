# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 06:28:47 2019

@author: asuer
"""
import bs4
import requests
from bs4 import BeautifulSoup
from collections import deque
from fake_useragent import UserAgent
from webapp.pycode.user_agent import random_header
# from user_agent import random_header
import threading
import time


class Bing3:
    def __init__(self, searched_item, site,date1,date2, urls_file):
        # self.file = open(urls_file, 'w', encoding='UTF8', newline='')
        # self.contain_file = open(cont_file, 'w', encoding='UTF8', newline='')
        self.file=open(urls_file,"a")
        self.url="https://www.google.com/search?q=%22virus%22:+/headlines/section/topic%22https://www.nytimes.com%22&tbs=cdr:1,cd_min:01/01/2020,cd_max:01/01/2022&source=lnms&tbm=nws"


        self.date1 = date1
        self.date2 = date2
        print("veriler create_searc_linke gönderiliyor")
        url = self.create_search_link(searched_item, site,date1,date2)
        # a queue of urls to be crawled next
        self.new_urls = deque([url])
        # a set of urls that we have already processed
        self.processed_urls = set()
        # a set of broken urls
        self.broken_urls = set()



    def get_next(self):
        # code = requests.get(self.url, headers={'User-Agent': 'Opera/9.25'})
        # plain = code.text
        r = requests.Session()
        headers = random_header()
        r.headers = headers
        res = r.get(self.url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select(".VDXfz")
        for li in links:
            try:
                next=li.get("href")
                next="https://news.google.com{}".format(next[1:])
            except:
                break
            self.url=next
            return next
        # for link in s.findAll('a', {'class': 'sb_pagN'}):
        #     try:
        #         next = "https://www.bing.com" + link.get('href')
        #     except:
        #         next = "https://www.bing.com"
        #     self.url = next
        #     return next

    def get_ur(self):
        code = requests.get(self.url, headers={'User-Agent': 'Opera/9.25'})
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for article in s.findAll('ol', {'id': 'b_results'}):
            for a in article.findAll('li', {'class': 'b_algo'}):
                for b in a.findAll('h2'):
                    for link in b.findAll('a'):
                        my_link = link.get('href') + "\n"
                        print(my_link)
                        self.file.write(my_link)
    def get_urls(self,url):
        # code = requests.get(self.url, headers={'User-Agent': 'Opera/9.25'})
        # plain = code.text
        # s = BeautifulSoup(plain, "html.parser")
        r = requests.Session()
        headers = random_header()
        r.headers = headers
        res = r.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        # links = soup.select(".dbsr a")
        links = soup.select('.kCrYT a')  # class_='WlydOe'):

        for g in links:
            j = g.get("href")
            m = str(j)

            if m.startswith("<a"):
                mm = m[55:]
                nn = mm.split('"')
                print(nn[0])
                tmp=nn[0]
                with open("asab.txt", 'a') as fw:
                    fw.write(tmp + '\n')
                    fw.close()
            else:
                print(m[30:])
                tmp=m[30:]
                with open("asab.txt", 'a') as fw:
                    fw.write(tmp + '\n')
                    fw.close()


        # links=soup.select(".WlydOe")
        # # print(links)
        # c=0
        # article_text = ""
        # for l in links:
        #     c+=1
        #     try:
        #         url_w=l.get("href")
        #         url_w="https://news.google.com{}".format(url_w[1:])
        #         # print(url_w)
        #         print(c)
        #         with open("asab.txt",'a') as fw:
        #             fw.write(url_w + '\n')
        #         # res2=requests.get(url_w,headers=headers)
        #         # parsed_article=bs4.BeautifulSoup(res2.text,'lxml')
        #         # paragraphs=parsed_article.findAll('p')
        #         # for p in paragraphs:
        #         #     article_text += p.text.strip()
        #         # print(article_text)
        #         # with open("sabcon.txt", 'a') as cfw:
        #         #     cfw.write(article_text + '\n')
        #         # article_text = ""
        #     except Exception as e:
        #         print("nanay")
        #
        # return c



        # for article in s.findAll('ol', {'id': 'b_results'}):
        #     for a in article.findAll('li', {'class': 'b_algo'}):
        #         for b in a.findAll('h2'):
        #             for link in b.findAll('a'):
        #                 my_link = link.get('href') + "\n"
        #                 print(my_link)
        #                 self.file.write(my_link)

    def crawl_all(self):
        counter=0
        while len(self.new_urls):
            # move url from the queue to processed url set
            self.url = self.new_urls.popleft()
            if self.url in self.processed_urls:
                break
            try:
                response = requests.get(self.url)
                counter += 1
            except(
            requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,
            requests.exceptions.InvalidSchema):
                # add broken urls to it’s own set, then continue
                self.broken_urls.add(self.url)
                continue

            self.processed_urls.add(self.url)
            # print the current url
            print('Processing %s' % self.url)

            counter=self.get_urls()
            next_url = self.get_next()
            self.new_urls.append(next_url)

        return counter


    def crawl_page(self):
        pass



    def create_search_link(self, item, site,date1,date2):
        link = 'https://www.google.com/search?q="{}":+/headlines/section/topic"{}"&tbs=cdr:1,cd_min:{},cd_max:{}&source=lnms&tbm=nws'
        if " " in item:
            words = item.split(" ")
            i = 0
            new_word = ""
            for word in words:
                if i == 1:
                    new_word = new_word + '+' + word
                else:
                    new_word = new_word + word
                i = 1
        else:
            new_word = item
        link = link.format(new_word, site,date1,date2)
        print("arama linki oluşturuldu")
        print(link)
        return link