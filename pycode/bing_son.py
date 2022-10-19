# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 06:28:47 2019

@author: asuer
"""

import requests
from bs4 import BeautifulSoup
from collections import deque
import threading
import time
import os
import sys


class BingSon:
    def __init__(self, date1, date2, keyword, n_name, dirname,until, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.keyword = keyword
        self.n_name = n_name
        self.dirname = dirname
        self.until = until
        self.page_links = []
        self.sayfa=int(int(self.until)/10)
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        ff = str(self.dirname)
        self.filname = desktop + '/' + ff
        self.link_filname = self.filname + "_bing_link.txt"

    def page_link_creator(self):
        # pg=int(self.until)/10
        for i in range(self.sayfa):
            uur= "https://www.bing.com/search?q={}+site%3{}+freshness%3a{}..{}&first={}1&FORM=PERE".format(self.keyword,self.n_name,self.date1,self.date2,i)
            self.page_links.append(uur)
        return self.page_links

    def get_link(self,url):
        count = 0
        i = 1
        while (count <= self.until):
            code = requests.get(url, headers={'User-Agent': 'Opera/9.25'})
            plain = code.text
            s = BeautifulSoup(plain, "html.parser")
            # print(soup)
            for article in s.findAll('ol', {'id': 'b_results'}):
                for a in article.findAll('li', {'class': 'b_algo'}):
                    for b in a.findAll('h2'):
                        for link in b.findAll('a'):
                            my_link = link.get('href') + "\n"
                            print(my_link.strip())
                            count += 1
                            print(count)
                            with open(self.link_filname, "a", encoding="utf-8") as file:
                                file.write(my_link.strip() + "\n")

            print("page {} ".format(i))
            i += 1
    def main(self):
        urls=self.page_link_creator()
        for i in urls:
            self.get_link(i.strip())


    #     self.url="https://www.bing.com/search?q={}+site%3{}+freshness%3a{}..{}&first={}1&FORM=PERE"
    #     self.link_filname = self.filname + "_link.txt"
    #     self.file = open(urls_file, "a")    #w değiştirildi
    #     url = self.create_search_link(searched_item, site)
    #     # a queue of urls to be crawled next
    #     self.new_urls = deque([url])
    #     # a set of urls that we have already processed
    #     self.processed_urls = set()
    #     # a set of broken urls
    #     self.broken_urls = set()
    #     self.fname=urls_file
    #     # try:
    #     #     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    #     #     print(desktop)
    #     # except:
    #     #     print("Linux Veya Unix Yolu Bulunamadı")
    #     # hos = os.getcwd()
    #     # # fname = urls_file
    #     # self.way = "{}{}{}/".format(desktop, "/", self.fname)
    #     # try:
    #     #     os.makedirs(self.way, exist_ok=True)
    #     #     print("Directory '%s' created successfully" % self.fname)
    #     # except OSError as error:
    #     #     newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
    #
    # def get_next(self):
    #     code = requests.get(self.url, headers={'User-Agent': 'Opera/9.25'})
    #     plain = code.text
    #     s = BeautifulSoup(plain, "html.parser")
    #     for link in s.findAll('a', {'class': 'sb_pagN'}):
    #         try:
    #             next = "https://www.bing.com" + link.get('href')
    #         except:
    #             next = "https://www.bing.com"
    #         self.url = next
    #         return next
    #
    # def get_urls(self):
    #     code = requests.get(self.url, headers={'User-Agent': 'Opera/9.25'})
    #     plain = code.text
    #     s = BeautifulSoup(plain, "html.parser")
    #     for article in s.findAll('ol', {'id': 'b_results'}):
    #         for a in article.findAll('li', {'class': 'b_algo'}):
    #             for b in a.findAll('h2'):
    #                 for link in b.findAll('a'):
    #                     my_link = link.get('href') + "\n"
    #                     # print(my_link)
    #                     # self.file.write(my_link)
    #                     # print("======================")
    #                     # print(self.way)
    #                     # new_file = "{}/{}.txt".format(self.way, self.fname)  #.txt eklendi
    #                     # print("======================")
    #                     with open(self.urls_file, "a", encoding="utf-8") as file:
    #                         file.write(my_link.strip() + "\n")
    #
    # def crawl_all(self):
    #     while len(self.new_urls):
    #         # move url from the queue to processed url set
    #         self.url = self.new_urls.popleft()
    #         if self.url in self.processed_urls:
    #             break
    #         try:
    #             response = requests.get(self.url)
    #         except(
    #         requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,
    #         requests.exceptions.InvalidSchema):
    #             # add broken urls to it’s own set, then continue
    #             self.broken_urls.add(self.url)
    #             continue
    #
    #         self.processed_urls.add(self.url)
    #         # print the current url
    #         print('Processing %s' % self.url)
    #
    #         self.get_urls()
    #         next_url = self.get_next()
    #         self.new_urls.append(next_url)
    #
    #
    #
    # def create_search_link(self, item, site):
    #     link = 'https://www.bing.com/search?q={}+site%3A{}&qs=n&form=QBLH&sp=-1'
    #     if " " in item:
    #         words = item.split(" ")
    #         i = 0
    #         new_word = ""
    #         for word in words:
    #             if i == 1:
    #                 new_word = new_word + '+' + word
    #             else:
    #                 new_word = new_word + word
    #             i = 1
    #     else:
    #         new_word = item
    #     link = link.format(new_word, site)
    #     return link
    #
