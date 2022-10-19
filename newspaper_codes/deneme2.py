# import os
# import bs4
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
# import os
# import urllib.request
# import re
# import urllib3
# from pandas import DataFrame
# import csv
# import datetime
# from datetime import datetime, timedelta
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# url="https://www.cumhuriyet.com.tr/ekonomi"
# driver = webdriver.Chrome('/usr/bin/chromedriver')
# driver.get(url)
# time.sleep(1)
# # SCROLL_PAUSE_TIME = 10
# more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# more.click()
# # last_height = driver.execute_script("return document.body.scrollHeight")
# # print(len(more))
# browser = driver
# lastHeight = browser.execute_script("return document.body.scrollHeight")
# i = 0
# dizi = []
# while True:
#     try:
#         # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
#         more.click()
#         time.sleep(1)
#
#         # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         # time.sleep(2)
#         # browser.find_element_by_css_selector('.button .c_button .s_button').click()
#         newHeight = browser.execute_script("return document.body.scrollHeight")  # scroll ile aşağı inme işlemi
#         print(i)
#         print("nnnnnnnnnnnnnnnnnnnnn")
#         print(newHeight)
#         print(lastHeight)
#         print("llllllllllllllll")
#         if newHeight == lastHeight:
#             time.sleep(1)
#             print("finishedddddddddddddddd")
#             sayfa_kaynağı = browser.page_source
#             soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
#             list = soup.find_all('div', {"class": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
#             time.sleep(4)
#             for i in list:
#                 sayac = 0
#                 for j in i:
#                     for m in j:
#                         for n in m:
#                             if type(n) != "str":
#                                 # print(n)
#                                 z = str(n)
#                                 if (z.startswith("<a href")):
#                                     h = z.split('?')
#                                     hh = h[0]
#                                     hh = hh[9:]
#                                     # print(hh)
#                                     sayac += 1
#                                     if sayac % 2 == 1:
#                                         # print(sayac)
#                                         url = "https://www.cumhuriyet.com.tr"
#                                         new_url = '{}{}'.format(url, hh)
#                                         print(new_url)
#                                         dizi.append(new_url)
#                                         # with open(self.link_filname, 'a') as file:
#                                         #     file.write(new_url + '\n')
#                                     else:
#                                         pass
#                                 else:
#                                     pass
#                             else:
#                                 pass
#             break
#         else:
#             lastHeight = newHeight
#         more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
#         more.click()
#         i = i + 1
#
#
#     except:
#         break
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # j='https://www.cumhuriyet.com.tr/ekonomi'
# # sayfa = 10
# # # driver_path = 'usr/bin/chromedriver'
# # driver ='/usr/bin/chromedriver'
# # browser = webdriver.Chrome(driver)
# # browser.get(j)
# # a = 0
# # dizi = []
# # dizi2 = []
# # result = True
# # while a < sayfa:
# #
# #     lastHeight = browser.execute_script("return document.body.scrollHeight")
# #     i = 0
# #     while i < 1:
# #         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(2)
# #         browser.find_element_by_css_selector('.button .c_button .s_button').click()
# #         newHeight = browser.execute_script("return document.body.scrollHeight")  # scroll ile aşağı inme işlemi
# #
# #         if newHeight == lastHeight:
# #             break
# #         else:
# #             lastHeight = newHeight
# #         i = i + 1
# #         a += 1
# # # Prim günü eksik olan kadınlar Bağ-Kur’dan 3600 gün ile yaştan emekli olur mu?
# #
# #
# #
# # url='https://www.cumhuriyet.com.tr/ekonomi'
# # driver = webdriver.Chrome('/usr/bin/chromedriver')
# # driver.get(url)
# # sayfa_kaynağı = browser.page_source
# # soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
# # test = soup.find_all('a', attrs={"target": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# #
# # for i in test:
# #     h=soup.find('a').get("href")
# #     print(h)
# #     # result = i['href'].startswith(('/arama', 'https:', '//', '/spor'), 0, 7)  # standartlara uygun linkleri çekiyor
# #     # link = i['href']
# #     # if result == False:
# #     #     if len(link) > 35:
# #     #         date = "{}{}".format('https://www.haberturk.com', link)
# #     #         dizi.append(date)
# #
# #
# #
# #
# # # j='https://www.cumhuriyet.com.tr/ekonomi'
# # # # sayfa_kaynağı = browser.page_source
# # # html = requests.get(j).content
# # # soup = BeautifulSoup(html, "html.parser")
# # # test = soup.find_all('a', attrs={"target": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# # #
# # # for i in test:
# # #     h=soup.find('a').get("href")
# # #     print(h)
# #
# # url='https://www.cumhuriyet.com.tr/ekonomi'
# # driver = webdriver.Chrome('/usr/bin/chromedriver')
# # driver.get(url)
# # sayfa_kaynağı = browser.page_source
# # soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
# # list2 = soup.find('div', {"class": "dahaFazlaGoster"})
# # print(type(list2))
# # print(list2)
# # print(len(list2))
# # count=0
# # while len(list2>2):
# #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #     time.sleep(2)
# #     # browser.find_element_by_css_selector('.button .c_button .s_button').click()
# #     browser.find_element_by_xpath('/html/body/main/div[1]/div[3]/div[3]/div[1]/div[4]/span').click()
# #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #     try:
# #         list2 = soup.find('div', {"class": "dahaFazlaGoster"})
# #         print(len(list2))
# #         if len(list2<3):
# #             break
# #         else:
# #             count+=1
# #             print(count)
# #     except:
# #         break
# # dizi=[]
# # u=soup.find_all('div',{"class":"col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# # for i in u:
# #     h=soup.find('a').get("href")
# #     print(h)
# #     dizi.append(h)
# #
# #
# #
# #
# #
# #
# #
# # i='https://www.cumhuriyet.com.tr/ekonomi'
# # driver = webdriver.Chrome('/usr/bin/chromedriver')
# # driver.get(i)
# # time.sleep(1)
# # # SCROLL_PAUSE_TIME = 10
# # more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# # more.click()
# # # last_height = driver.execute_script("return document.body.scrollHeight")
# # # print(len(more))
# # browser=driver
# # lastHeight = browser.execute_script("return document.body.scrollHeight")
# # i = 0
# # dizi = []
# # while True:
# #     try:
# #         # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         more=driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# #         more.click()
# #         time.sleep(1)
# #
# #         # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         # time.sleep(2)
# #         # browser.find_element_by_css_selector('.button .c_button .s_button').click()
# #         newHeight = browser.execute_script("return document.body.scrollHeight")  # scroll ile aşağı inme işlemi
# #         print(i)
# #         print("nnnnnnnnnnnnnnnnnnnnn")
# #         print(newHeight)
# #         print(lastHeight)
# #         print("llllllllllllllll")
# #         if newHeight == lastHeight:
# #             time.sleep(1)
# #             print("finishedddddddddddddddd")
# #
# #             u = soup.find_all('div', {"class": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# #             time.sleep(4)
# #             for i in u:
# #                 print("insideeeeeeeeeeeeee")
# #                 h = soup.find('a').get("href")
# #                 print(h)
# #                 dizi.append(h)
# #             break
# #         else:
# #             lastHeight = newHeight
# #         more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# #         more.click()
# #         i = i + 1
# #
# #
# #     except:
# #         break
# # print("out of while")
# # for i in dizi:
# #     print(i)
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
# # uur='https://www.cumhuriyet.com.tr/ekonomi'
# # html = requests.get(uur).content
# # # # date=url[37:]
# # soup = BeautifulSoup(html, "html.parser")
# #
# #
# #
# # list = soup.find_all("div", {"class": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# #
# #
# #
# #
# #
# #
# # for i in list:
# #     sayac = 0
# #     for j in i:
# #             for m in j:
# #                 for n in m:
# #                     if type(n)!="str":
# #                         # print(n)
# #                         z=str(n)
# #                         if(z.startswith("<a href")):
# #                             h=z.split('?')
# #                             hh=h[0]
# #                             hh=hh[9:]
# #                             # print(hh)
# #                             sayac+=1
# #                             if sayac%2==1:
# #                                 # print(sayac)
# #                                 url="https://www.cumhuriyet.com.tr"
# #                                 new_url='{}{}'.format(url,hh)
# #                                 print(new_url)
# #                             else:
# #                                 pass
# #                         else:
# #                             pass
# #                     else:
# #                         pass
# #                     # print("=_=_=_=_=_=_=__=")
# #
# #             # print(j.get("href"))
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
# # uur='https://www.cumhuriyet.com.tr/ekonomi'
# # driver = webdriver.Chrome('/usr/bin/chromedriver')
# # driver.get(url)
# # time.sleep(1)
# # # SCROLL_PAUSE_TIME = 10
# # more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# # more.click()
# # # last_height = driver.execute_script("return document.body.scrollHeight")
# # # print(len(more))
# # browser = driver
# # lastHeight = browser.execute_script("return document.body.scrollHeight")
# # i = 0
# # dizi = []
# # while True:
# #     try:
# #         # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# #         more.click()
# #         time.sleep(1)
# #
# #         # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         # time.sleep(2)
# #         # browser.find_element_by_css_selector('.button .c_button .s_button').click()
# #         newHeight = browser.execute_script("return document.body.scrollHeight")  # scroll ile aşağı inme işlemi
# #         print(i)
# #         print("nnnnnnnnnnnnnnnnnnnnn")
# #         print(newHeight)
# #         print(lastHeight)
# #         print("llllllllllllllll")
# #         if newHeight == lastHeight:
# #             time.sleep(1)
# #             print("finishedddddddddddddddd")
# #             sayfa_kaynağı = browser.page_source
# #             soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
# #             u = soup.find_all('div', {"class": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# #             time.sleep(4)
# #             for i in u:
# #                 print("insideeeeeeeeeeeeee")
# #                 h = soup.find('a').get("href")
# #                 print(h)
# #                 dizi.append(h)
# #             break
# #         else:
# #             lastHeight = newHeight
# #         more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
# #         more.click()
# #         i = i + 1
# #
# #
# #     except:
# #         break
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
# # dizi = []
# # u = soup.find_all('div', {"class": "col-xs-6 col-sm-6 col-md-6 col-lg-6 pl5 pr5"})
# # for i in u:
# #     h = soup.find('a').get("href")
# #     print(h)
# #     dizi.append(h)
#
#     # # Scroll down to bottom
#     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     #
#     # # Wait to load page
#     # time.sleep(SCROLL_PAUSE_TIME)
#     #
#     # # Calculate new scroll height and compare with last scroll height
#     # new_height = driver.execute_script("return document.body.scrollHeight")
#     #
#     # more = driver.find_element_by_css_selector('.dahaFazlaGoster > span:nth-child(1)')
#     # more.click()
#     # print(more)
#
#     # if new_height != last_height:
#
#     # last_height = new_height
#
#
#
# # element=driver.find_element_by_tag_name('body')
# # while True:
# #     element.send_keys(Keys.PAGE_DOWN)
# #     time.sleep(2)
#
# print("selam")
# sayac=0
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# #
# # url='https://www.cumhuriyet.com.tr/bilim-teknoloji/9-gunluk-bayram-tatilinde-siber-saldirilara-dikkat-1955132?utm_medium=Kategori%20Sayfasi&utm_source=Cumhuriyet&utm_campaign=Kategori%20Sayfasi'
# # # url='https://www.odatv4.com/guncel/amerikadan-turkiye-icin-yeni-saldiri-uyarisi-0101171200-106799'
# # # url='https://www.odatv4.com/arsiv?ara=&tarih=2017-01-01'
# # html = requests.get(url).content
# # soup = BeautifulSoup(html, "html.parser")
# # title=soup.find("h1",{"class":"baslik"}).text.strip()
# # print(title)
# #
# # date=soup.find("div",{"class":"yayin-tarihi"}).text.strip()
# # date=date[:-7]
# # date=date.strip()
# # print(date)
# # list = soup.find("div", {"class": "haberMetni"}).find_all('p')
# # txt=""
# # for i in list:
# #     txt+=i.text.strip()
# # #         txt+=i.text
# # cdata='{} ; {} ; {} ; {}'.format(url,date,title,txt)
# #
# #
#
#
#
#
#
#
#
# #
# #
# # categ="aaaaaaaaaaa"
# # d1="2017-10-10"
# # d2="2017-10-11"
# # u1 = "https://www.gazeteduvar.com.tr/arsiv?"
# # u2 = "&tarih_baslangic="
# # u3 = "&tarih_bitis="
# # u4 = "&siralama=0&sayfa="
# # t1 = datetime.strptime(d1, '%Y-%m-%d').date()
# # t2 = datetime.strptime(d2, '%Y-%m-%d').date()
# # dizi = []
# # t = timedelta(days=1)
# # dates = np.arange(t1, t2, t).astype(datetime)
# # counter = 1
# # for i in dates:
# #     print("------------------------")
# #     print(i)
# #     print("------------------------")
# #     i = i.strftime('%d.%m.%Y')
# #     print("------------------------")
# #     print(i)
# #     print("------------------------")
# #     switch = 0
# #     while switch == False:
# #         # uur='{}{}{}{}'.format(u1,u2,u3,u4)
# #         if len(categ) > 107:
# #             url = categ
# #             try:
# #                 print("I am here ")
# #                 html = requests.get(url).content
# #                 # # date=url[37:]
# #                 soup = BeautifulSoup(html, "html.parser")
# #                 list = soup.find_all("div", {"class": "alert alert-danger"})
# #                 for i in list:
# #                     if len(i.text) == 52:
# #                         break
# #                     else:
# #                         counter += 1
# #                         dizi.append(url)
# #             except:
# #                 pass
# #         else:
# #             try:
# #                 u2 = '&tarih_baslangic={}'.format(t1)
# #                 u3 = '&tarih_bitis={}'.format(t2)
# #                 new_url = '{}{}{}{}{}'.format(u1, u2, u3, u4, counter)
# #                 print(new_url)
# #
# #                 html = requests.get(new_url).content
# #                 # # date=url[37:]
# #                 soup = BeautifulSoup(html, "html.parser")
# #                 list = soup.find_all("div", {"class": "alert alert-danger"})
# #                 print(len(list))
# #                 dizi.append(new_url)
# #                 if len(list>0):
# #                     switch=True
# #                     break
# #
# #                 # for i in list:
# #                 #     print("//////////////////////////////////")
# #                 #     print(i)
# #                 #     h = soup.find('p', {"class": "mb-0"}).text
# #                 #     print("******************************")
# #                 #     print(h)
# #                 #     print(len(h))
# #                 #     print(type(len(h)))
# #                 #     print("******************************")
# #                 #     if len(h) != 50:
# #                 #         counter += 1
# #                 #         dizi.append(new_url)
# #                 #         print(new_url)
# #                 #         print("xxxxxxxxxxxxxxxxxxxxxxxllllllllxlxlxlx")
# #                 #
# #                 #
# #                 #
# #                 #     else:
# #                 #         switch = True
# #                 #         break
# #                 #
# #                 #         # counter+=1
# #                 #         # dizi.append(new_url)
# #                 #         # print(new_url)
# #                 counter += 1
# #             except:
# #                 pass
# # for i in dizi:
# #     print(i)
# #
# # url='https://www.gazeteduvar.com.tr/diyarbakirda-bin-800-yillik-kalorifer-sistemi-bulundu-galeri-1501367'
# # # url='https://www.gazeteduvar.com.tr/aksoy-arastirma-erdogan-yavas-ve-imamoglu-karsisinda-kaybediyor-galeri-1515387?p=5'
# # # url='https://www.gazeteduvar.com.tr/arsiv?&tarih_baslangic=22.07.2015&tarih_bitis=22.07.2021&siralama=0&sayfa=1'
# # html = requests.get(url).content
# # # # date=url[37:]
# # soup = BeautifulSoup(html, "html.parser")
# # list = soup.find_all("div", {"class": "content-text max-width"})
# # date= soup.find("div", {"class": "info"}).text
# # date=date.strip()
# # date=date[:-6]
# #
# # title= soup.find("h1", ).text
# # # print(title)
# # # print(date[:-6])
# # counter=0
# # txt=''
# # for i in list:
# #     if counter>0:
# #         break
# #     else:
# #         h=soup.find_all('p')
# #         for j in h:
# #             txt+=j.text
# #             # print(h.text.strip())
# #             # print(j.text)
# #     counter+=1
# #
# # cdata='{} ; {} ; {} ; {}'.format(url,date,title,txt)
# # print(cdata)
# #
#
#
#
# #
# #
# # url='https://www.dailymail.co.uk/home/sitemaparchive/day_20161001.html'
# # html = requests.get(url).content
# # # # date=url[37:]
# # soup = BeautifulSoup(html, "html.parser")
# # # list = soup.find_all("div", {"class": "col-12 col-lg mw0"})
# # list2=soup.find_all('ul',{"class":"archive-articles debate link-box"})
# # z=[]
# # for i in list2:
# #     h=soup.find_all('li')
# #     for j in h:
# #         if (j.a.get("href"))==None:
# #             break
# #         else:
# #             uur='https://www.dailymail.co.uk'
# #             new_url=uur+j.a.get("href")
# #             z.append(new_url)
# # for i in z:
# #     print(i)
#
#
# # #
# # urls=['https://www.dailymail.co.uk/wires/ap/article-8827387/Right-Labanc-Sharks-sign-Labanc-18-9M-4-year-deal.html','https://www.dailymail.co.uk/wires/ap/article-8827387/Right-Labanc-Sharks-sign-Labanc-18-9M-4-year-deal.html','https://www.dailymail.co.uk/sport/rugbyunion/article-8827373/Exeter-boss-Rob-Baxter-hopeful-Jack-Nowell-fit-European-Cup-final-against-Racing-92.html']
# # # uvr=
# # zz=[]
# # for irs in urls:
# #     html = requests.get(irs).content
# #     # # date=url[37:]
# #     soup = BeautifulSoup(html, "html.parser")
# #     list = soup.find_all("div", {"itemprop": "articleBody"})
# #     list2=soup.find('h2').text
# #     print(list2)
# #     print("*****************************")
# #     z=""
# #
# #
# #     for i in list:
# #         h=soup.find_all("p")
# #         for j in h:
# #             print(j.text)
# #             z+=j.text.strip()
# #     zz.append(z)
# # print("==========================================")
# # for i in zz:
# #     print(i)
# # print("=============================================")
# #
# # # articleBody
#
# # url='https://www.gazeteduvar.com.tr/arsiv?tarih_baslangic=22.07.2016&tarih_bitis=24.07.2016&kategoriler[0]=5f6f684508038f7697471493&siralama=0&sayfa=1'
# # html = requests.get(url).content
# # # # date=url[37:]
# # soup = BeautifulSoup(html, "html.parser")
# # # list = soup.find_all("div", {"class": "col-12 col-lg mw0"})
# # list2=soup.find_all('a',{"class":"box archive-box image-left_text-right"})
# # z=[]
# # for i in list2:
# #     print(i.a.get("href"))
#     # z.append(i.find('a',{"class":"box archive-box image-left_text-right"}))
#     # z.append(i.a.get("href"))
# #     z.append(i)
# # for s in z:
# #     print(s)
#
#
# #
# #
# # def fibo(sayi):
# #     a=1
# #     b=1
# #     c=2
# #     for i in range(sayi):
# #         a=b+c
# #         b=a+c
# #         c=a+b
# #         print(a, b, c)
# #
# # fibo(5)
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # txt="asdfadfadfadf ;date ;cat"
# # j=txt.split(';')
# # date=j[1].strip()
# # url=j[0].strip()
# # cat=j[2].strip()
# # print(url)
# # print(date)
# # print(cat)
# #
# # url='https://www.milligazete.com.tr/arsiv/2019-04-02'
# #
# # uur='https://www.milligazete.com.tr/haber/1936227/sandik-basinda-katledilen-saadet-partililer-hakka-ugurlandi'
# # #milli gazete get creator*************************
# # # r = requests.get(uur)
# # # soup = BeautifulSoup(r.content, 'lxml')
# # # title=soup.find('h1').getText()
# # # print(title)
# # # print("------------------")
# # # art=soup.find("div",{"class":"post-text"})
# # # z=art.find_all('p')
# # # txt=""
# # # for i in z:
# # #     txt+=i.text
# # # print(txt)
# # # #-----------------------------------------------------
# # #
# # #
# #
# # #   -----------------milli gazete get links----------
# # # html = requests.get(url).content
# # # date=url[37:]
# # # soup = BeautifulSoup(html, "html.parser")
# # # # list = soup.find_all("div", {"class": "category-news"})
# # # list = soup.find_all("div", {"class": "f-cat f-item"})
# # # # for i in list:
# # # for j in list:
# # #
# # #     print("---------------------------")
# # #     cat=j.find('h3',{"class":"f-brandon-black"}).text
# # #     print(j.find('h3',{"class":"f-brandon-black"}).text)
# # #     print("---------------------------")
# # #     z=j.find_all('a', {"class": "lb"})
# # #     # print(z)
# # #     for i in z:
# # #         wdata = "{}{} ;{} ;{}".format("https://www.milligazete.com.tr", i.get("href"), date,cat)
# # #         print(wdata)
# # #         # print(i.get("href"))
# # #     #     print(i.find(('a', {"class": "lb"})))
# #
# #
# #
# #
# # # url='https://www.haberler.com/arsiv/2018-10-10/haberler/s9/'
# # # def page_get_link_selenium(url):
# # #     dizi=[]
# # #     driver = webdriver.Chrome('/usr/bin/chromedriver')
# # #     driver.get(url)
# # #     time.sleep(1)
# # #
# # #
# # #     return dizi
#
#
#
#
# #***************************************************************************
# # sayac=1
# # dizi=[]
# # while True:
# #
# #     url = 'https://www.haberler.com/arsiv/2011-10-10/haberler/s{}/'.format(sayac)
# #     # print(url)
# #     # print(sayac)
# #     dizi.append(url)
# #     r = requests.get(url).content
# #     soup = BeautifulSoup(r, "html.parser")
# #     # p_count = soup.find("div",{"class":"hbPagination"}).find_all("span")
# #     array = []
# #     span = ""
# #     pages_links=[]
# #
# #     if not soup.find("div", {"class": "hbPagination"}):  # Linklerin sayfaları ile birlite ayarlıyor
# #         pages_links.append(url)
# #     else:
# #
# #         p_count = soup.find("div", {"class": "hbPagination"}).find_all("span")
# #         a=p_count
# #         # print(a[3].text)
# #         try:
# #             print(a[4].text)
# #             if a[4].text==(""):
# #
# #                 print("bura boş ")
# #             else:
# #
# #                 print("devam et")
# #
# #         except:
# #             h=a[3].text
# #             print("son sayfa {} dur".format(h))
# #             break
# #         sayac += 1
# # for i in dizi:
# #     print(i)
# #*******************************************************************
#
#
#
#
#
# #         # # while True:
# #         # for i in p_count:
# #         #     span = i.getText()
# #         #     array.append(span)
# #         #     # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
# #         #     # print(span)
# #         #     # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
# #
# #         # page_num = len(array) - 1
# #         # new_url = url
# #         # new_url = new_url.replace("s1", "s{}")
# #         #
# #         # for i in range(page_num):
# #         #     i = str(i + 1)
# #         #     lnk = new_url.format(i)
# #         #     pages_links.append(lnk)
# #
# # #
# # d1='2018-10-10'
# # d2='2018-10-11'
# # dizi = []
# # pages=[]
# # pgl=[]
# # # ser_date = pd.Series(pd.date_range('19920101', periods=12000))
# # t1 = datetime.strptime(d1, '%Y-%m-%d').date()
# # t2 = datetime.strptime(d2, '%Y-%m-%d').date()
# # t = timedelta(days=1)
# # dates = np.arange(t1, t2, t).astype(datetime)
# # # url = "https://www.haberler.com/arsiv/{}/haberler/s1/"
# # # num = 1
# # # # t1 = datetime(2006, 6, 1)
# # # # t2 = datetime(2021, 8, 5)  # Genel liinkleri oluşturyor
# # # # t = timedelta(days=1)
# # # # dates = np.arange(t1, t2, t).astype(datetime)
# # # for j in dates:
# # #     new_url = (url.format(j.strftime('%d-%m-%Y'), num))
# # #     pages.append(new_url)
# # # for i in pages:
# # #     print("+++++++++++++++      +++++++++++++")
# # #     print(i)
# # #     uur=str(i.strip())
# # #
# # #     pgs=self.page_get_link(uur)
# # #     print("--------------pgl------------------")
# # #     for p in pgs:
# # #         print("****************** p **************************")
# # #         dizi.append(p)