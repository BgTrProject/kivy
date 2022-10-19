# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import csv
# import pandas as pd
# import datetime
# from datetime import datetime, timedelta
# import numpy as np
# import os
# import csv
# import concurrent
# import multiprocessing
# from multiprocessing import pool
# import io
# from pprint import pprint
# from webapp.pycode.utils import (BeautifulSoup, Options, UserAgent,webdriver_manager,
#                               get, re, sys, time,
#                              webdriver)
#
# from webapp.pycode.helpers import (get_chrome_web_driver, get_web_driver_options,
#                                set_automation_as_head_less,
#                                set_browser_as_incognito,
#                                set_ignore_certificate_error)
#
# from requests_html import HTMLSession
#
#
# def render_JS(URL):
#     session = HTMLSession()
#     r = session.get(URL)
#     r.html.render()
#     return r.html.text
#
# lns=['https://www.hurriyet.com.tr/arama/#/?page=2&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true','https://www.hurriyet.com.tr/arama/#/?page=3&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true','https://www.hurriyet.com.tr/arama/#/?page=4&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true','https://www.hurriyet.com.tr/arama/#/?page=5&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true','https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true']
#
# for url in lns:
#
#     count = 0
#     count2 = 0
#     count3 = 0
#     test = []
#     dizi = []
#     soup=render_JS(url)
#     # r = requests.get(url)
#     # soup = BeautifulSoup(soup, 'html.parser')
#     for a in soup.find_all('a', href=True):
#         count2 += 1
#         link = a['href']
#         test.append(link)
#     for i in test:
#         result = i.startswith("http://www.hurriyet.com.tr")
#         if result == True:
#             if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
#                 # with open(self.link_filname, 'a') as file:
#                 #     file.write(i + '\n')
#                 dizi.append(i)
#                 print("===================================")
#                 print(i)
#                 print("===================================")
#                 count3 += 1
#         count += 1
#
# # def func(url):
# #     count = 0
# #     count2 = 0
# #     count3 = 0
# #     test = []
# #     dizi = []
# #     #
# #     # print(url)
# #     # print("*-*-*-*-**--*-**-*-*--*--*-*-*-*-*-*--**-")
# #     #
# #     # # driver = webdriver.Chrome('/usr/bin/chromedriver')
# #     # driver = webdriver.Chrome('/usr/bin/chromedriver')
# #     # options = get_web_driver_options()
# #     # # options=webdriver.chrome('/usr/bin/chromedriver')
# #     # set_automation_as_head_less(options)
# #     # set_ignore_certificate_error(options)
# #     # set_browser_as_incognito(options)
# #     # # driver = get_chrome_web_driver(options)
# #     # # from fake_useragent import UserAgent
# #     #
# #     # # driver = webdriver.Chrome('/usr/bin/chromedriver')
# #     # ua = UserAgent()
# #     # user_agent = ua.random
# #     # print(user_agent)
# #     # options.add_argument(f'user-agent={user_agent}')
# #     # driver.delete_all_cookies()
# #     # driver.refresh()
# #     # driver.get(url)
# #     # time.sleep(1)
# #     # soup = BeautifulSoup(driver.page_source, 'html.parser')
# #     r = requests.get(url)
# #     soup = BeautifulSoup(r.content, 'html.parser')
# #     for a in soup.find_all('a', href=True):
# #         count2 += 1
# #         link = a['href']
# #         test.append(link)
# #     for i in test:
# #         result = i.startswith("http://www.hurriyet.com.tr")
# #         if result == True:
# #             if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
# #                 # with open(self.link_filname, 'a') as file:
# #                 #     file.write(i + '\n')
# #                 dizi.append(i)
# #                 print("===================================")
# #                 print(i)
# #                 print("===================================")
# #                 count3 += 1
# #         count += 1
# #     # driver.delete_all_cookies()
# #     # driver.refresh()
# #     # driver.close()
# #     return dizi
# # arra=[]
# # for i in lns:
# #     arra.append(func(i))
# #
#
#
#
#
#
#
#
#
# # from bs4 import BeautifulSoup
# # import requests
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # import time
# # import csv
# # import pandas as pd
# # import datetime
# # from datetime import datetime, timedelta
# # import numpy as np
# # import os
# #
# #
# # def dateCreator(self, d1, d2):
# #     driver = webdriver.Chrome('/usr/bin/chromedriver')
# #
# #     links = []
# #     dizi = []
# #     t1 = datetime.strptime(d1, '%Y-%m-%d').date()
# #     t2 = datetime.strptime(d2, '%Y-%m-%d').date()
# #     t = timedelta(days=1)
# #     dates = np.arange(t1, t2, t).astype(datetime)
# #     # t1 = datetime(2019, 4, 9)  # en son 1999 05 01 e kadar çalışıyo
# #     # t2 = datetime(2019, 4, 10)
# #     # t = timedelta(days=1)
# #     # dates = np.arange(t1, t2, t).astype(datetime)
# #     link = "https://www.hurriyet.com.tr/arama/#/?page="  # 1000 e kadar sayfa var kanser
# #
# #     # fonksiyon oluşturup sayfa sayısını çekmen lazım,
# #     switch = 1
# #     count = 0
# #     count2 = 0
# #     count3 = 0
# #     test = []
# #     while switch == 1:
# #         for date in dates:
# #             for page in range(1,
# #                               1000):  # page 1 den başlıyo ortalama 70 80 sayfa var her bi günün  ama değişken olduğu için 100 verdim
# #
# #                 if self.categ == 'avrupa' or self.categ == 'yerel-haberler' or self.categ == 'dunya' or self.categ == 'gundem' or self.categ == 'ekonomi':
# #                     newdate = date.strftime('%Y/%m/%d')
# #                     enddate = pd.to_datetime(newdate) + pd.DateOffset(days=1)
# #                     enddate = enddate.strftime('%Y/%m/%d')
# #                     ll = ("{}{}{}{}{}{}{}".format(link, page,
# #                                                   '&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=',
# #                                                   newdate,
# #                                                   '&finishDate=', enddate,
# #                                                   '&platform=hurriyet&mainCategory=/{}/&isDetail=true').format(
# #                         self.categ))
# #
# #                     # driver.get(ll)
# #                     # soup = BeautifulSoup(driver.page_source, 'html.parser')
# #                     # url = 'https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true'
# #                     driver = webdriver.Chrome('/usr/bin/chromedriver')
# #                     driver.get(ll)
# #                     time.sleep(1)
# #                     soup = BeautifulSoup(driver.page_source, 'html.parser')
# #
# #                     try:
# #                         title = soup.find("p", {"class": "hs-nr-text"}).getText()
# #                         if title.startswith("Sonu"):
# #
# #                             switch = 0
# #                             driver.close()
# #                             break
# #                         else:
# #
# #                         from bs4 import BeautifulSoup
# #                         import requests
# #                         from selenium import webdriver
# #                         from selenium.webdriver.common.keys import Keys
# #                         import time
# #                         import csv
# #                         import pandas as pd
# #                         import datetime
# #                         from datetime import datetime, timedelta
# #                         import numpy as np
# #                         import os
# #
# #                         count = 0
# #                         count2 = 0
# #                         count3 = 0
# #                         test = []
# #                         dizi=[]
# #                         lns=['https://www.hurriyet.com.tr/arama/#/?page=5&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true','https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true']
# #                         for i in lns:
# #
# #                             driver = webdriver.Chrome('/usr/bin/chromedriver')
# #                             driver.get(i)
# #                             soup = BeautifulSoup(driver.page_source, 'html.parser')
# #                             for a in soup.find_all('a', href=True):
# #                                 count2 += 1
# #                                 link = a['href']
# #                                 test.append(link)
# #                             for i in test:
# #                                 result = i.startswith("http://www.hurriyet.com.tr")
# #                                 if result == True:
# #                                     if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
# #                                         # with open(self.link_filname, 'a') as file:
# #                                         #     file.write(i + '\n')
# #                                         dizi.append(i)
# #                                         print("===================================")
# #                                         print(i)
# #                                         print("===================================")
# #                                         count3 += 1
# #                                 count += 1
# #
# #                     except:
# #                         pass
# #                     print(ll)
# #                     links.append(ll)
# #                     print(" lllllllllllllllllllllllllllllin alındı   ")
# #
# #
# #
# #
# #                 else:
# #
# #                     newdate = date.strftime('%Y/%m/%d')
# #                     enddate = pd.to_datetime(newdate) + pd.DateOffset(days=1)
# #                     enddate = enddate.strftime('%Y/%m/%d')
# #                     lls = ("{}{}{}{}{}{}{}".format(link, page, '&where=hurriyet&how=Article&startDate=', newdate,
# #                                                    '&finishDate=', enddate, '&platform=hurriyet&isDetail=true'))
# #                     driver = webdriver.Chrome('/usr/bin/chromedriver')
# #                     driver.get(lls)
# #                     soup = BeautifulSoup(driver.page_source, 'html.parser')
# #                     title = soup.find("p", {"class": "hs-nr-text"}).getText()
# #                     try:
# #                         title = soup.find("p", {"class": "hs-nr-text"}).getText()
# #                         if title.startswith("Sonu"):
# #
# #                             print(title)
# #                             switch = 0
# #                             driver.close()
# #                             break
# #                         else:
# #                             # links.append(lls)
# #                             # print(lls)
# #                             for a in soup.find_all('a', href=True):
# #                                 count2 += 1
# #                                 link = a['href']
# #                                 test.append(link)
# #                             for i in test:
# #                                 result = i.startswith("http://www.hurriyet.com.tr")
# #                                 if result == True:
# #                                     if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
# #                                         # with open(self.link_filname, 'a') as file:
# #                                         #     file.write(i + '\n')
# #                                         dizi.append(i)
# #                                         print("===================================")
# #                                         print(i)
# #                                         print("===================================")
# #                                         count3 += 1
# #                                 count += 1
# #                     except:
# #                         pass
# #                     print(lls)
# #                     links.append(lls)
# #                     print(" lllllllllllllllllllllllllllllin alındı   ")
# #                     driver.close()
# #
# #     return dizi
# #
# #
# #
# #
# #
# #
# # # def creator(url):
# # #     r = requests.get(url)
# # #     soup = BeautifulSoup(r.content, 'html.parser')
# # #     title = soup.find("h1", attrs={"class": "rhd-article-title"})
# # #     print(title)
# # #     category = soup.find("div", attrs={"class": "rhd-category-box"})
# # #     print(category)
# # #     content_array = soup.find("div", attrs={"class": "rhd-all-article-detail"})
# # #     print(content_array)
# # #     date = soup.find("span", attrs={"class": "rhd-time-box-text hidden-sm-down"})
# # #     print(date)
# # #     date = date.split()
# # #     date = date[2]
# # #     content_array = content_array.split()
# # #     content_string = ""
# # #     stop = "(function(url,"
# # #     stop2 = "namespace)"
# # #     for w in content_array:
# # #         if w == stop or w == stop2:
# # #             break
# # #         else:
# # #             content_string = content_string + " " + w
# # #             # w_data = url+";"+date+";"+title+";"+content_string
# # #     w_data = "{};{};{};{};{}".format(url, date, category, title, content_string)
# # #     print(w_data)
# # #     # write_to_txt(w_data)
# # #     # with open(self.content_filname, 'a') as file:
# # #     #     file.write(w_data + '\n')
# # #
# # # switch=1
# # # arr=['hali','veli','deli','yerli','tuz', 'ekmek']
# # # while switch==1:
# # #     for i in arr:
# # #         if i.startswith("yer"):
# # #             switch=0
# # #
# # #             break
# # #             print(i)
# # #         else:
# # #             print(i)
# # #
# # # url='https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true'
# # # driver = webdriver.Chrome('/usr/bin/chromedriver')
# # # driver.get(url)
# # # soup = BeautifulSoup(driver.page_source, 'html.parser')
# # # title = soup.find("p",{"class":"hs-nr-text"}).getText()
# # # if title.startswith("Sonu"):
# # #
# # #     print(title)
# # #     driver.close()
# # # else:
# # #     pass
# #
# # #
# # # url="http://www.hurriyet.com.tr/ekonomi/menfaatiniz-icin-kart-yerine-kredi-kullanin-40323999"
# # #
# # # html = requests.get(url).content
# # # soup = BeautifulSoup(html, "html.parser")
# # # title = soup.find("div", {"class": "container"}).find("h1").getText()  # TİTLE Tamam
# # # # print(title)
# # # date = soup.find("span", {"class": "news-date"}).getText()
# # # date = date[:-6]
# # # date = date.strip()
# # # # print(date)
# # # content_array = soup.find("div", attrs={"class": "news-content readingTime"})
# # # # print(content_array)
# # # l_content=content_array.getText()
# # # l_content=l_content.strip()
# # # # print(l_content[14:])
# # # w_data = "{};{};{};{}".format(url, date,  title, l_content)
# # # print(w_data)
# #
# # #
# # # r = requests.get(url)
# # # soup = BeautifulSoup(r.content, 'html.parser')
# # # title = soup.find("h1", attrs={"class": "news-detail-title title-actived"})
# # # print(title)
# # # print(title.getText())
# # # category = soup.find("div", attrs={"class": "rhd-category-box"})
# # # print(category)
# # # content_array = soup.find("div", attrs={"class": "rhd-all-article-detail"})
# # # print(content_array)
# # # date = soup.find("span", attrs={"class": "rhd-time-box-text hidden-sm-down"})
# # # print(date)
# # # date = date.split()
# # # date = date[2]
# # # content_array = content_array.split()
# # # content_string = ""
# # # stop = "(function(url,"
# # # stop2 = "namespace)"
# # # for w in content_array:
# # #     if w == stop or w == stop2:
# # #         break
# # #     else:
# # #         content_string = content_string + " " + w
# # #         # w_data = url+";"+date+";"+title+";"+content_string
# # # w_data = "{};{};{};{};{}".format(url, date, category, title, content_string)
# # # print(w_data)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # import os
# # # import bs4
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import pandas as pd
# # # import numpy as np
# # # import os
# # # import urllib.request
# # # import re
# # # import urllib3
# # # from pandas import DataFrame
# # # import csv
# # # import datetime
# # # from datetime import datetime, timedelta
# # # from selenium import webdriver
# # # from selenium.webdriver.common.keys import Keys
# # # import time
# # #
# # #
# # #
# # # class sabah:
# # #     def __init__(self, date1, date2, categ, filname, dirname, **kwargs):
# # #         self.date1 = date1
# # #         self.date2 = date2
# # #         self.categ = categ
# # #         self.filname = filname
# # #         self.dirname = dirname
# # #         self.page_links = []
# # #         self.content_filname = ""
# # #         self.link_filname = ""
# # #
# # #         self.newsLinks = []
# # #
# # #         desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# # #         print(desktop)
# # #
# # #         print(self.filname)
# # #         ff = str(filname)
# # #
# # #         self.filname = desktop[:-7] + "websites/rubic/webapp/g_upload/{}/{}_".format(self.dirname,
# # #                                                                                      self.dirname) + ff  # +"/"+ff
# # #         self.content_filname = self.filname + "_content.txt"
# # #         self.link_filname = self.filname + "_link.txt"
# # #         print(self.link_filname)
# # #
# # #     def dateCreator(self,d1,d2):
# # #
# # #
# # #         #https://www.sabah.com.tr/timeline/2020/10/10?c=yasam
# # #         url = 'https://www.sabah.com.tr/timeline'
# # #         keyword = ['gundem', 'ekonomi', 'yasam', 'saglik', 'dunya', 'seyahat', 'yazarlar']
# # #         all_links = []
# # #         txt = ""
# # #         t1 = datetime.strptime(d1, '%Y-%m-%d').date()
# # #         t2 = datetime.strptime(d2, '%Y-%m-%d').date()
# # #         t = timedelta(days=1)
# # #         dates = np.arange(t1, t2, t).astype(datetime)
# # #         for i in dates:
# # #             i = i.strftime('%Y/%m/%d')
# # #             if self.categ=='gundem' or self.categ=='ekonomi' or self.categ== 'yasam'or self.categ=='saglik' or self.categ=='dunya' or self.categ== 'seyahat' or self.categ== 'yazarlar':
# # #                 txt = "{}/{}?c={}".format(url, i, self.categ)
# # #                 all_links.append(txt)
# # #                 print(txt)
# # #             else:
# # #                 for j in keyword:
# # #                     txt="{}/{}?c={}".format(url, i, j)
# # #                     all_links.append(txt)
# # #                     print(txt)
# # #         return all_links
# # #
# # #
# # #
# # #
# # #     def get_link(self,i):
# # #         driver = webdriver.Chrome('/usr/bin/chromedriver')
# # #         driver.get(i)
# # #         time.sleep(2)
# # #         element=driver.find_element_by_tag_name('body')
# # #         while True:
# # #             element.send_keys(Keys.PAGE_DOWN)
# # #             time.sleep(2)
# # #         # req = requests.get(i)
# # #         try:
# # #             # soup = BeautifulSoup(req.content, "lxml")
# # #             print("selam")
# # #             soup= BeautifulSoup(driver.page_source, 'html.parser')
# # #             print(soup)
# # #             for a in soup.find_all('a', href=True):
# # #                 # print(a.get("href"))
# # #                 test = a.get("href")
# # #                 result = test.startswith(('/gunde', '/ekono', '/yasam', '/sagli', '/dunya', '/seyah', '/yazar'), 0,
# # #                                          6)
# # #                 if result == True:
# # #                     if len(test) > 20:
# # #                         txt = ""
# # #                         url = 'https://www.sabah.com.tr'
# # #                         wdata = "{}{}".format(url, test)
# # #                         with open(self.link_filname, "a", encoding="utf-8") as file:
# # #                             file.write(wdata + "\n")
# # #
# # #             # dblink+=[link.get('href') for link in soup.find_all('a')]
# # #         except:
# # #             print("------ website gives problem -----")
# # #
# # #
# # #
# # #
# # #     def creator(self,url):
# # #         count = 1
# # #         # for i in link:
# # #         r = requests.get(url)
# # #
# # #         soup = BeautifulSoup(r.content, 'lxml')
# # #         tt = ""
# # #         try:
# # #             dat = soup.find("div", attrs={"class": "newsBox"})
# # #             dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
# # #             dat2 = dat2[14:-5].strip()
# # #
# # #
# # #             for i in dat.stripped_strings:
# # #                 # print(i.strip())
# # #                 tt += i.strip()
# # #
# # #             cdata = '{};{};{}'.format(url, dat2.strip(), tt.strip())
# # #             with open(self.content_filname, "a", encoding="utf-8") as file:
# # #                 file.write(cdata + "\n")
# # #
# # #             tt = ''
# # #             print(count, ".Haber")
# # #             count += 1
# # #         except:
# # #             print("nanay    ----")
# # #         # count = 1
# # #         # # for i in link:
# # #         # r = requests.get(url)
# # #         # print(count, ".Haber")
# # #         # count += 1
# # #         # soup = BeautifulSoup(r.content, 'lxml')
# # #         # txt = ""
# # #         # try:
# # #         #
# # #         #     dat = soup.find("div", attrs={"class": "newsBox"}).text
# # #         #     dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
# # #         #     dat2 = dat2[14:-5].strip()
# # #         #     print("dddddddddddddddddddddddddddddddddddddd")
# # #         #     print(dat2)
# # #         #     print("dddddddddddddddddddddddddddddddddddddd")
# # #         #     print("*****************************************")
# # #         #     print(dat)
# # #         #     print("*****************************************")
# # #         #     for d in str(dat).split("\n"):
# # #         #
# # #         #         # d=d.strip()
# # #         #         if d.startswith('EN ÇOK OKUNANLAR') or d.startswith('SON DAKİKA'):
# # #         #             break
# # #         #         else:
# # #         #             txt += d
# # #         #             txt.strip()
# # #         #
# # #         #     # print("=========================================================")
# # #         #     cdata = '{};{};{}'.format(url, dat2.strip(), txt.strip())
# # #         #     print(cdata)
# # #         #
# # #         #     with open(self.content_filname, "a", encoding="utf-8") as file:
# # #         #         file.write(cdata + "\n")
# # #         #     txt = ''
# # #         #     # print("=========================================================")
# # #         # except:
# # #         #     print("nanay    ----")
# # #
# # #
# # #
# # #     def main(self):
# # #         print("************ started to collect page links")
# # #
# # #         self.page_links=self.dateCreator(self.date1,self.date2)
# # #         print("-------- all links---")
# # #
# # #
# # #         for i in self.page_links:
# # #             print(i)
# # #             self.get_link(i.strip())
# # #         print("reading links from {}.,.,.,.,.,.,.,.,.,.,. ".format(self.link_filname))
# # #         with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
# # #             for i in f.readlines():
# # #                 i = i.strip("\n")
# # #                 self.newsLinks.append(i)
# # #
# # #
# # #         print("-----------------------")
# # #         print(self.content_filname)
# # #         print(self.link_filname)
# # #         print("-------------------------")
# # #
# # #         for i in self.newsLinks[:]:
# # #             self.creator(i.strip())
# # #
# # #         print("Successfully!")
# # #
# # #
# # #
# # #
# # #
# # #
# # #     # def creator(url):
# # #     #     count = 1
# # #     #     # for i in link:
# # #     #     r = requests.get(url)
# # #     #     print(count, ".Haber")
# # #     #     count += 1
# # #     #     soup = BeautifulSoup(r.content, 'lxml')
# # #     #     txt = ""
# # #     #     try:
# # #     #
# # #     #         dat = soup.find("div", attrs={"class": "newsBox"})
# # #     #         dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
# # #     #         dat2=dat2[14:-5].strip()
# # #     #         cdat=dat.find_all('p')
# # #     #         print("dddddddddddddddddddddddddddddddddddddd")
# # #     #         print(dat2)
# # #     #         print("dddddddddddddddddddddddddddddddddddddd")
# # #     #         print("*****************************************")
# # #     #         print(cdat)
# # #     #         print("*****************************************")
# # #     #         for d in str(cdat).split("\n"):
# # #     #
# # #     #             # d=d.strip()
# # #     #             if d.startswith('EN ÇOK OKUNANLAR') or d.startswith('SON DAKİKA'):
# # #     #                 break
# # #     #             else:
# # #     #                 txt+=d
# # #     #                 txt.strip()
# # #     #
# # #     #
# # #     #         print("=========================================================")
# # #     #         cdata='{};{};{}'.format(url,dat2.strip(),txt.strip())
# # #     #         print(cdata)
# # #     #         txt=''
# # #     #         print("=========================================================")
# # #     #     except:
# # #     #         print("nanay    ----")
# # #     # uur='https://www.sabah.com.tr/gundem/2021/10/10/firat-kalkani-bolgesindeki-sehit-polis-sayisi-2ye-yukseldi'
# # #     # creator(uur)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # import os
# # # import bs4
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import pandas as pd
# # # import numpy as np
# # # import os
# # # import urllib.request
# # # import re
# # # import urllib3
# # # from pandas import DataFrame
# # # import csv
# # # import datetime
# # # from datetime import datetime, timedelta
# # #
# # #
# # #
# # # def creator(url):
# # #     count = 1
# # #     # for i in link:
# # #     r = requests.get(url)
# # #     print(count, ".Haber")
# # #     count += 1
# # #     soup = BeautifulSoup(r.content, 'lxml')
# # #     txt = ""
# # #     tt=""
# # #     try:
# # #
# # #         dat = soup.find("div", attrs={"class": "newsBox"})
# # #         dat2 = soup.find("span", attrs={"class": "textInfo"}).span.text
# # #         dat2 = dat2[14:-5].strip()
# # #         cdat = dat.find_all('p')
# # #         print(type(cdat))
# # #         print("dddddddddddddddddddddddddddddddddddddd")
# # #         for i in dat.stripped_strings:
# # #             # print(i.strip())
# # #             tt+=i.strip()
# # #         print("dddddddddddddddddddddddddddddddddddddd")
# # #         # print("*****************************************")
# # #         # print(cdat)
# # #         # for i in cdat:
# # #         #     # print(i.text)
# # #         #
# # #         #     tt+=i
# # #         # print("-------------------------------")
# # #         # # # print(tt)
# # #         # # tt=""
# # #         #
# # #         # # print(s)
# # #         # print("*****************************************")
# # #         # # for d in str(cdat).split("\n"):
# # #         #
# # #         #     # d=d.strip()
# # #         #     if d.startswith('EN ÇOK OKUNANLAR') or d.startswith('SON DAKİKA'):
# # #         #         break
# # #         #     else:
# # #         #         txt += d
# # #         #         txt.strip()
# # #
# # #         print("=========================================================")
# # #         cdata = '{};{};{}'.format(url, dat2.strip(), tt.strip())
# # #         print(cdata)
# # #         txt = ''
# # #         tt=''
# # #         print("=========================================================")
# # #     except:
# # #         print("nanay    ----")
# # #
# # #
# # # uur = 'https://www.sabah.com.tr/gundem/2021/10/10/firat-kalkani-bolgesindeki-sehit-polis-sayisi-2ye-yukseldi'
# # # creator(uur)
#
#
#
#     def dateCreator(self,d1,d2):
#         driver = webdriver.Chrome('/usr/bin/chromedriver')
#         options = get_web_driver_options()
#         # options=webdriver.chrome('/usr/bin/chromedriver')
#         set_automation_as_head_less(options)
#         set_ignore_certificate_error(options)
#         set_browser_as_incognito(options)
#         # driver = get_chrome_web_driver(options)
#         # from fake_useragent import UserAgent
#
#         # driver = webdriver.Chrome('/usr/bin/chromedriver')
#         ua = UserAgent()
#         user_agent = ua.random
#         print(user_agent)
#         options.add_argument(f'user-agent={user_agent}')
#
#         # browser=webdriver.Chrome('/usr/bin/chromedriver')
#
#
#         links = []
#         dizi=[]
#         t1 = datetime.strptime(d1, '%Y-%m-%d').date()
#         t2 = datetime.strptime(d2, '%Y-%m-%d').date()
#         t = timedelta(days=1)
#         dates = np.arange(t1, t2, t).astype(datetime)
#         # t1 = datetime(2019, 4, 9)  # en son 1999 05 01 e kadar çalışıyo
#         # t2 = datetime(2019, 4, 10)
#         # t = timedelta(days=1)
#         # dates = np.arange(t1, t2, t).astype(datetime)
#         link = "https://www.hurriyet.com.tr/arama/#/?page="  # 1000 e kadar sayfa var kanser
#
#         #fonksiyon oluşturup sayfa sayısını çekmen lazım,
#         switch=1
#         # count = 0
#         # count2 = 0
#         # count3 = 0
#         # test=[]
#
#         while switch==1:
#             for date in dates:
#                     for page in range(1,1000):  # page 1 den başlıyo ortalama 70 80 sayfa var her bi günün  ama değişken olduğu için 100 verdim
#
#
#                         if self.categ=='avrupa' or self.categ=='yerel-haberler' or self.categ=='dunya' or self.categ=='gundem' or self.categ=='ekonomi':
#                             newdate = date.strftime('%Y/%m/%d')
#                             enddate = pd.to_datetime(newdate) + pd.DateOffset(days=1)
#                             enddate = enddate.strftime('%Y/%m/%d')
#                             ll=("{}{}{}{}{}{}{}".format(link, page, '&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=', newdate,
#                                                                  '&finishDate=', enddate, '&platform=hurriyet&mainCategory=/{}/&isDetail=true').format(self.categ))
#
#                             # driver.get(ll)
#                             # soup = BeautifulSoup(driver.page_source, 'html.parser')
#                             # url = 'https://www.hurriyet.com.tr/arama/#/?page=6&where=hurriyet&how=Article,Column,NewsPhotoGallery,NewsVideo,Recipe&startDate=01/01/2017&finishDate=02/01/2017&platform=hurriyet&mainCategory=/ekonomi/&isDetail=true'
#                             # driver = webdriver.Chrome('/usr/bin/chromedriver')
#
#                             driver = webdriver.Chrome('/usr/bin/chromedriver')
#                             options = get_web_driver_options()
#                             # options=webdriver.chrome('/usr/bin/chromedriver')
#                             set_automation_as_head_less(options)
#                             set_ignore_certificate_error(options)
#                             set_browser_as_incognito(options)
#                             # driver = get_chrome_web_driver(options)
#                             # from fake_useragent import UserAgent
#
#                             # driver = webdriver.Chrome('/usr/bin/chromedriver')
#                             ua = UserAgent()
#                             user_agent = ua.random
#                             print(user_agent)
#                             options.add_argument(f'user-agent={user_agent}')
#                             if(ll.startswith("https://www.hurriyet.com.tr/cerez-politikasi")):
#                                 driver.refresh()
#                                 driver.delete_all_cookies()
#                                 time.sleep(1)
#                                 driver.close()
#                             else:
#                                 driver.get(ll)
#                                 time.sleep(1)
#                                 soup = BeautifulSoup(driver.page_source, 'html.parser')
#
#
#
#                                 try:
#                                     title = soup.find("p", {"class": "hs-nr-text"}).getText()
#                                     if title.startswith("Sonu"):
#
#                                         switch=0
#                                         driver.close()
#                                         break
#                                     else:
#
#                                         pass
#
#                                 except:
#                                     pass
#                                 count = 0
#                                 count2 = 0
#                                 count3 = 0
#                                 test = []
#
#                                 soup2 = BeautifulSoup(driver.page_source, 'html.parser')
#                                 for a in soup2.find_all('a', href=True):
#                                     count2 += 1
#                                     link = a['href']
#                                     test.append(link)
#                                     print("*******------0-0-0----bbbbbbbbbbbbbbbb------0")
#                                 for i in test:
#                                     result = i.startswith("http://www.hurriyet.com.tr")
#                                     print("*******------0-0-0------cccc-----0")
#                                     if result == True:
#                                         if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
#                                             # with open(self.link_filname, 'a') as file:
#                                             #     file.write(i + '\n')
#                                             dizi.append(i)
#                                             print("===================================")
#                                             print(i)
#                                             print("===================================")
#                                             count3 += 1
#                                     count += 1
#                                 driver.refresh()
#
#
#
#
#                                 print(ll)
#                                 links.append(ll)
#                                 print(" lllllllllllllllllllllllllllllin alındı   ")
#
#
#
#
#                         else:
#
#
#                             newdate = date.strftime('%Y/%m/%d')
#                             enddate = pd.to_datetime(newdate) + pd.DateOffset(days=1)
#                             enddate = enddate.strftime('%Y/%m/%d')
#                             lls=("{}{}{}{}{}{}{}".format(link, page, '&where=hurriyet&how=Article&startDate=', newdate,
#                                                                  '&finishDate=', enddate, '&platform=hurriyet&isDetail=true'))
#                             # driver = webdriver.Chrome('/usr/bin/chromedriver')
#
#                             driver = webdriver.Chrome('/usr/bin/chromedriver')
#                             options = get_web_driver_options()
#                             # options=webdriver.chrome('/usr/bin/chromedriver')
#                             set_automation_as_head_less(options)
#                             set_ignore_certificate_error(options)
#                             set_browser_as_incognito(options)
#                             # driver = get_chrome_web_driver(options)
#                             # from fake_useragent import UserAgent
#
#                             # driver = webdriver.Chrome('/usr/bin/chromedriver')
#                             ua = UserAgent()
#                             user_agent = ua.random
#                             print(user_agent)
#                             options.add_argument(f'user-agent={user_agent}')
#                             if lls.startswith("https://www.hurriyet.com.tr/cerez-politikasi"):
#                                 driver.refresh()
#                                 driver.delete_all_cookies()
#                                 time.sleep(1)
#                                 driver.close()
#                             else:
#                                 driver.get(lls)
#                                 time.sleep(1)
#                                 soup = BeautifulSoup(driver.page_source, 'html.parser')
#                                 title = soup.find("p", {"class": "hs-nr-text"}).getText()
#                                 try:
#                                     title = soup.find("p", {"class": "hs-nr-text"}).getText()
#                                     if title.startswith("Sonu"):
#
#                                         print(title)
#                                         switch=0
#                                         driver.close()
#                                         break
#                                     else:
#                                         pass
#
#
#                                 except:
#                                     pass
#
#                                 count = 0
#                                 count2 = 0
#                                 count3 = 0
#                                 test = []
#
#                                 # soup2 = BeautifulSoup(driver.page_source, 'html.parser')
#                                 for a in soup.find_all('a', href=True):
#                                     count2 += 1
#                                     link = a['href']
#                                     test.append(link)
#                                     print("*******------0-0-0----bbbbbbbbbbbbbbbb------0")
#                                 for i in test:
#                                     result = i.startswith("http://www.hurriyet.com.tr")
#                                     print("*******------0-0-0------cccc-----0")
#                                     if result == True:
#                                         if count > 15 and count % 5 == 2 and len(i) > 50 and count3 < 10:  #
#                                             # with open(self.link_filname, 'a') as file:
#                                             #     file.write(i + '\n')
#                                             dizi.append(i)
#                                             print("===================================")
#                                             print(i)
#                                             print("===================================")
#                                             count3 += 1
#                                     count += 1
#                                 driver.refresh()
#
#                                 print(lls)
#                                 links.append(lls)
#                                 print(" lllllllllllllllllllllllllllllin alındı   ")
#                                 driver.delete_all_cookies()
#                                 driver.close()
#
#         return dizi