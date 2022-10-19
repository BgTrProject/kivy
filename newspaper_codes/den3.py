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
#
# import urllib.request
# import re
# import urllib3
# from pandas import DataFrame
# import csv
# import datetime
# from datetime import datetime, timedelta, date
# import os
# import csv
# import concurrent
# import multiprocessing
# from multiprocessing import pool
# import io
# from pprint import pprint
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
# import urllib.request
# import re
# import concurrent
# import multiprocessing
# from multiprocessing import pool
# import io
# from pprint import pprint
# # #
# # # # i='https://www.theguardian.com/world/2020/oct/17/all'
# # # # page_one = 0
# # # # r = requests.get(i)
# # # # soup = BeautifulSoup(r.content, 'html5lib')
# # # # uzunluk = len("https://www.theguardian.com/{}/".format(categ))
# # # # url = i[uzunluk + 3:uzunluk + 7]
# # # # print(url)
# # # # url2 = "https://www.theguardian.com/{}/blog/".format(categ) + url
# # # # url3 = "https://www.theguardian.com/{}/".format(categ) + url
# # # # count = 0
# # # # # print(self.link_filname)
# # # # print("dosya açççççççççççççççççççç")
# # # # for a in soup.find_all('a', href=True):
# # # #     link = a['href']
# # # #     count += 1
# # # #     result = len(link) > 50
# # # #     if result == True:
# # # #         result2 = link.startswith(url2) or link.startswith(url3)
# # # #         if result2 == True:
# # # #             if (count % 2 == 0):
# # # #                 print(link)
# # #
# # #
# # # # ---------------------guardian get link---------------------------
# # # # i='https://www.theguardian.com/world/2020/oct/18/all'
# # # # page_one = 0
# # # # r = requests.get(i)
# # # # soup = BeautifulSoup(r.content, 'html5lib')
# # # # # lnk=soup.find_all("div",{"class":"fc-item__content "})
# # # # links=soup.find("div",{"class":"fc-container__body fc-container--rolled-up-hide"}).find_all('a')
# # # # counter=1
# # # # say=1
# # # # for i in links[:-2]:
# # # #
# # # #     # print(len(i.text))
# # # #     counter+=1
# # # #     if( counter%2==0):
# # # #         print(say)
# # # #         # say+=1
# # # #         print(i.get("href"))
# # # #         say += 1
# # # #     else:
# # # #         pass
# # #
# # #
# # #
# # # #==================guardian creator===============================
# # # # url="https://www.theguardian.com/world/2020/oct/18/thai-protest-leaders-play-cat-and-mouse-with-police-as-thousands-rally"
# # # # url="https://www.theguardian.com/world/2020/oct/11/poisoning-the-pacific-new-book-details-us-military-contamination-of-islands-and-ocean"
# # # # r = requests.get(url)
# # # # soup = BeautifulSoup(r.content, 'html5lib')
# # # # title = soup.find("h1").getText()
# # # # print(title)
# # # # content_array = soup.find("div", attrs={"class": "article-body-commercial-selector"}).getText()
# # # # category = soup.find("a", attrs={"class": "dcr-yx39j8"}).getText()
# # # # print(category)
# # # # date = soup.find("summary", attrs={"class": "dcr-h56grb"}).getText()
# # # # date = date.split()
# # # # date = date[0] + '-' + date[1] + '-' + date[2]
# # # # print(date)
# # # # content_array = content_array.split()
# # # # content_string = ""
# # # # for w in content_array:
# # # #     content_string = content_string + " " + w
# # # # w_data = "{};{};{};{};{}".format(url, date, category, title, content_string)
# # # # print(w_data)
# # # # # with open(self.content_filname, 'a') as file:
# # # #     file.write(w_data + '\n')
# # #
# # #
# # # dizi=[]
# # # #-------------------------independent get link -----------------------
# # # i='https://www.independent.co.uk/archive/2020-10-10'
# # # r = requests.get(i)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # # try:
# # #     for a in soup.find_all('a', href=True):
# # #         link = a['href']
# # #         result = link.endswith(".html")
# # #         if (result == True):
# # #             result2 = link.startswith("/service") or link.startswith(
# # #                 "/news/world/journalism-license-srmg-middle-east-news-world-global-a9579111.html")
# # #             if (result2 == False):
# # #                 ekle = "https://www.independent.co.uk"
# # #                 link = "{}{}".format(ekle, link)
# # #                 # print(link)
# # #                 dizi.append(link)
# # # except:
# # #     pass
# # #
# # #
# # # #========================= independent creator =============================
# # # # url='https://www.independent.co.uk/news/world/europe/germany-holocaust-survivors-funding-coronavirus-covid-pandemic-b1034371.html'
# # # for url in dizi[:5]:
# # #     r = requests.get(url)
# # #     soup = BeautifulSoup(r.content, 'html5lib')
# # #     try:
# # #
# # #         title = soup.find("h1").getText()
# # #
# # #         # content_array = soup.find("div", attrs={"class": "sc-bxBxkN"}).getText()  #hatalıdır düzelt
# # #         content_array = soup.find("div", attrs={"class": "ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE"}).find_all('p')
# # #         # print (title)ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE
# # #         date = soup.find("div", attrs={"class":"FormattedDate__Wrapper-sc-tneaun-0 YtdZt"}).getText()# "sc-DlApP"}).getText()
# # #         date = date.split()
# # #         date = date[3] + "-" + date[2] + "-" + date[1]
# # #         # print (date)
# # #         date = datetime.strptime(date, "%Y-%B-%d").strftime("%Y-%m-%d")
# # #         # print (date)
# # #         # content_array = content_array.split()
# # #         content_string = ""
# # #         for w in content_array:
# # #             # stop = "(function({"
# # #             # if (w == stop):
# # #             #     break
# # #             # else:
# # #             # content_string = content_string + " " + w
# # #             content_string+=w.text
# # #                 # w_data = url+";"+date+";"+title+";"+content_string
# # #
# # #         w_data = "{} ; {} ; {} ; {}".format(url, date, title, content_string)
# # #         # write_to_txt(w_data)
# # #         print(w_data)
# # #     except:
# # #         pass
# # #
# # #
# # #
# # #
# # #
# # #
# # # url='https://www.independent.co.uk/news/world/americas/wisconsin-coronavirus-record-cases-deaths-masks-b1021654.html'
# # # r = requests.get(url)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # #
# # # title = soup.find("h1").getText()
# # #
# # # # content_array = soup.find("div", attrs={"class": "sc-bxBxkN"}).getText()  #hatalıdır düzelt
# # # content_array = soup.find("div", attrs={"class": "ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE"}).find_all('p')
# # # # print (title)ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE
# # # date = soup.find("div", attrs={"class":"FormattedDate__Wrapper-sc-tneaun-0 YtdZt"}).getText()# "sc-DlApP"}).getText()
# # # date = date.split()
# # # date = date[3] + "-" + date[2] + "-" + date[1]
# # # # print (date)
# # # date = datetime.strptime(date, "%Y-%B-%d").strftime("%Y-%m-%d")
# # # # print (date)
# # # # content_array = content_array.split()
# # # content_string = ""
# # # for w in content_array:
# # #     # stop = "(function({"
# # #     # if (w == stop):
# # #     #     break
# # #     # else:
# # #     # content_string = content_string + " " + w
# # #     content_string+=w.text
# # #         # w_data = url+";"+date+";"+title+";"+content_string
# # #
# # # w_data = "{} ; {} ; {} ; {}".format(url, date, title, content_string)
# # # # write_to_txt(w_data)
# # # print(w_data)
# # #
# # #
# # #
# # #
# # #
# # # #-----------------------------dailysabah get link-----------------------------------
# # # # items_list
# # # url='https://www.dailysabah.com/search?qlimit=by_fifty&pgno=4902&qsort=oldest'
# # # r = requests.get(url)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # # links = soup.find("ul", attrs={"class":"items_list"}).find_all('a')
# # # counter=0
# # # for i in links:
# # #     counter+=1
# # #     if counter%2==1:
# # #         print(i.get("href"))
# # #     else:
# # #         pass
# # #
# # #
# # # #=========================== dailysabah container
# # #
# # # url='https://www.dailysabah.com/business/2015/11/26/russia-threatens-trade-ties-but-cautious-on-cutting-gas-delivery'
# # # h=url.split('/')
# # # print(h[3])
# # # r = requests.get(url)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # #
# # # title = soup.find("h1",{"class","main_page_title"}).getText().strip()
# # # print(title)
# # # date = soup.find("div", attrs={"class":"left_mobile_details"}).getText()# "sc-DlApP"}).getText()
# # # date = date.split()
# # # date = date[4] + "-" + date[5][:-1] + "-" + date[6]
# # # date=date.strip()
# # # text=soup.find("div", attrs={"class": "article_body"})
# # # txt=''
# # # for i in text.stripped_strings:
# # #     txt+=i.strip()
# # #
# # # cdata='{} ; {} ; {} ; {}'.format(url,date,title,txt)
# # # print(cdata)
# # #
# # # cont= soup.find("div", attrs={"class": "article_body"}).getText()
# # #
# # #
# # #
# # # z=soup.find("div", attrs={"class": "article_body"})
# # # txt=''
# # # for i in z.stripped_strings:
# # #     txt+=i.strip()
# # # #hatalıdır düzelt
# # # # content_array = soup.find("div", attrs={"class": "ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE"}).find_all('p')
# # # # print (title)ContentWrapper__MainContent-sc-cvxyxr-6 hXAvOH ContentWrapper__StyledColumnContent-sc-cvxyxr-8 cHvvJE
# # #
# # # # date = datetime.strptime(date,"%B-%d-%Y").strftime("%Y-%m-%d")
# # # # print (date)
# # # # content_array = content_array.split()
# # # content_string = ""
# # # for w in content_array:
# # #     # stop = "(function({"
# # #     # if (w == stop):
# # #     #     break
# # #     # else:
# # #     # content_string = content_string + " " + w
# # #     content_string+=w.text
# # #         # w_data = url+";"+date+";"+title+";"+content_string
# # #
# # # w_data = "{} ; {} ; {} ; {}".format(url, date, title, content_string)
# # # # write_to_txt(w_data)
# # # print(w_data)
# # #
# # #
# # #
# # #
# # #
# # #
# # # #------------------------------segabg get link
# # # switch=0
# # # dizi=[]
# # # cats = ['category-observer', 'category-bulgaria']
# # #
# # # while switch==0:
# # #     for m in cats:
# # #         for i in range(188,2000):
# # #             url='https://www.segabg.com/{}?page={}'.format(m,i)
# # #             dizi.append(url)
# # #             r = requests.get(url)
# # #             soup = BeautifulSoup(r.content, 'html5lib')
# # #             title = soup.find("li",{"class","pager-show-more-next first last"}).text.strip()
# # #             if title.startswith('Няма повече стати'):
# # #                 print(" break thats enough")
# # #                 break
# # #             else:
# # #
# # #                 print(url)
# # #         # print(url)
# # #         switch=1
# # #
# # #
# # # for i in dizi:
# # #     print(i)
# # #
# # #
# # #
# # #
# # # #-------------------segabg get link-----------------------------------------
# # #
# # #
# # # # url='https://www.segabg.com/{}?page={}'.format(m,i)
# # #
# # #
# # # url='https://www.segabg.com/category-the-war?page=3'
# # # dizi.append(url)
# # # r = requests.get(url)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # # title = soup.find_all("div",{"class","title"})
# # # for i in title:
# # #     for j in i:
# # #         links=j.get("href")
# # #         print(links)
# # #     # h=soup.find('a').get("href")
# # #     # print(h)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # #======================= segabg creator ==============================
# # #
# # # link='https://www.segabg.com/article/dvoen-standart-ima-ne-samo-pri-hranite-no-i-vv-vsichki-sferi-na-zhivota-ni'
# # # # link="https://www.segabg.com/hot/category-the-war/ruskiyat-poslanik-oon-napusna-yadosan-zasedanie"
# # # inner_array=[]
# # # r = requests.get(link)
# # # inner_array.append(link)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # # dat = soup.find("div", attrs={"class": "sega-article-date"})
# # # datem = (dat.getText())
# # # # print(datem)
# # # atxt=""
# # #
# # # inner_array.append(datem)
# # # title = soup.find("h1", attrs={"class": "sega-title"}).getText()
# # # # print(title)
# # # inner_array.append(title)
# # # table = soup.find("div", attrs={"class": "sega-body"}).findAll('p')
# # # cable = soup.findAll("p")
# # # for j in cable[:-6]:
# # #     if j != " ":
# # #         atxt += j.getText().strip()
# # #     else:
# # #         print("yyyyy")
# # # # for i in table.stripped_string:
# # # #     atxt+=i.getText().strip()
# # # # print("---",atxt)
# # #
# # # inner_array.append(atxt)
# # # ps = ""
# # # ps = "{}{}{}{}{}{}{}".format(inner_array[0], ";", inner_array[1], ";", inner_array[2], ";", inner_array[3])
# # # print(ps)
# # #
# # # print(cable)
# # # for k in table[:-6]:
# # #     m=soup.find_all('p')
# # #     for n in m:
# # #         print(n)
# #
# #
# #
# # #========================== banker contain ===================
# # # link='https://www.banker.bg/upravlenie-i-biznes/read/durjavnite-benzinostancii-na-finalnata-prava-no-s-neiasno-finansirane'
# # # inner_array = []
# # # atxt = ""
# # # # print(link)
# # # lnk=link.split(';')
# # # link=lnk[0]
# # # print("================")
# # # print(lnk[0])
# # # # print(lnk[1])
# # #
# # # inner_array.append(link)
# # # r = requests.get(link)
# # # soup = BeautifulSoup(r.content, 'html5lib')
# # # try:
# # #     dat=soup.find("span",attrs={"class":"time-published"}).time.get("datetime")
# # #     dat = dat[-10:]
# # #
# # #
# # # except:
# # #     dat="date None"
# # # print(dat)
# # # inner_array.append(dat)
# # # try:
# # #     title = soup.find("h1", attrs={"class": "blue"}).getText()
# # # except:
# # #     title=" title None"
# # # # print(title)
# # #
# # # inner_array.append(title.strip())
# # # try:
# # #     table = soup.find("div", attrs={"class": "body oembed"}).find_all("p")
# # #     print(table)
# # #     z=""
# # #     for k in table:
# # #         print("    kkkkkkkkkkk         kkk")
# # #         z+=k.text
# # # except:
# # #     z="None"
# # # print("          0-*-*-*- *-* - *- *- * -* -* -* - - *")
# # # print(z)
# # # print("          0-*-*-*- *-* - *- *- * -* -* -* - - *")
# # # # try:
# # # #
# # # #     for i in table:
# # # #         print("----i in table--")
# # # #         print(i.getText().strip())
# # # #         print(i)
# # # #
# # # #         # if (i.getText() == " " or i.getText() == ""):
# # # #         #     pass
# # # #         #     # print("***************")
# # # #         # else:
# # # #             # for j in i:
# # # #             # print(i)
# # # #         h = list(i.striped_string)
# # # #         print(h)
# # # #         print("ssssssssssssss        sssssssss")
# # # #         for i in h:
# # # #             print(i)
# # # #             print("sssssssssssssssssssssss")
# # # #             atxt +=i
# # # # except:
# # # #     atxt="content None"
# # # #         # print("----******---------")
# # # #         # for j in h:
# # # #         # atxt=h
# # # # print("+++++++++  content      ++++")
# # # # print(atxt.strip())
# # # inner_array.append(z.strip())
# #
# # # for i in inner_array:
# # #     print(i)
# #
# #
# #
# # #======================== aa haber
# # url='https://www.aa.com.tr/en/world'
# # driver = webdriver.Chrome('/usr/bin/chromedriver')
# # driver.get(url)
# # driver.maximize_window()
# # time.sleep(2)
# # p_h = driver.execute_script('return document.body.scrollHeight')
# # #
# # # driver=webdriver.Chrome('/usr/bin/chromedriver')
# # # # brows=driver.get('https://www.aa.com.tr/en/science-technology')
# # # driver=driver.get('https://www.aa.com.tr/en/world')
# # # time.sleep(1)
# # # driver.maximize_window()
# # # but=driver.find_element_by_xpath('/html/body/div/main/div[9]/div[3]/a')
# # # but.click()
# # p_h = driver.execute_script('return document.body.scrollHeight')
# # dizi=[]
# # while True:
# #     driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
# #     but = driver.find_element_by_xpath('/html/body/div/main/div[9]/div[3]/a')
# #     but.click()
# #     time.sleep(1)
# #     new_h = driver.execute_script('return document.body.scrollHeight')
# #     soup = BeautifulSoup(driver.page_source, 'html.parser')
# #     lnks = soup.find_all('a', {"class": "col-sm-12 col-md-6 col-lg-3 col-xl-3 p-sm-0 m-sm-0 p-0"})
# #     for i in lnks:
# #         if(i.get('href')!=None):
# #             dizi.append(i.get("href"))
# #         else:
# #             break
# #
# #     if new_h == p_h:
# #         break
# #     p_h = new_h
# # # 'col-sm-12 col-md-6 col-lg-3 col-xl-3 p-sm-0 m-sm-0 p-0'
# # # ids=driver.find_elements_by_xpath('//*[@href]')
# # # soup = BeautifulSoup(driver.page_source, 'html.parser')
# # # lnks=soup.find_all('a',{"class":"col-sm-12 col-md-6 col-lg-3 col-xl-3 p-sm-0 m-sm-0 p-0"})
# # # for i in lnks:
# # #     print(i.get("href"))
# # #
# # # for i in ids:
# # #     print(i)
# # count=1
# # for i in dizi:
# #     print(i)
# #     print(count)
# #     count+=1
#
# import os
# import json
# def tojson():
#     # the file to be converted
#     filename = 'webapp/g_upload/dailysabah_searchs_dailysabah_content_1.txt'
#     # resultant dictionary
#     dict1 = {}
#     # fields in the sample file
#     fields = ['link', 'date','category', 'title', 'content']
#
#     with open(filename) as fh:
#         # count variable for employee id creation
#         l = 1
#
#         for line in fh:
#             try:
#                 # reading line by line from the text file
#                 description = list(line.strip().split(';', 5))
#                 # for output see below
#                 print(description)
#                 # for automatic creation of id for each employee
#                 sno = 'news' + str(l)
#                 # loop variable
#                 i = 0
#                 # intermediate dictionary
#                 dict2 = {}
#                 while i < len(fields):
#                     # creating dictionary for each employee
#                     dict2[fields[i]] = description[i]
#                     i = i + 1
#                 # appending the record of each employee to
#                 # the main dictionary
#                 dict1[sno] = dict2
#                 l = l + 1
#             except:
#                 pass
#
#     # creating json file
#     out_file = open("webapp/g_upload/dailysabah_content.json", "w")
#     json.dump(dict1, out_file, indent=4)
#     out_file.close()
# tojson()




#
#
# import os
# import bs4
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
# import os
# import time
# import urllib.request
# import re
# import urllib3
# from pandas import DataFrame
# import csv
# import datetime
# from datetime import datetime, timedelta
#
# url='https://www.dailymail.co.uk/tvshowbiz/article-10366269/Clayton-Echard-doesnt-harbor-resentment-Nick-Viall.html'
# html = requests.get(url).content
# # # date=url[37:]
# soup = BeautifulSoup(html, "html.parser")
# list = soup.find_all("div", {"itemprop": "articleBody"})
# list2 = soup.find('h2').text
# # print(list2)
# sentence=""
# # date=""
# dat=""
# s=1
# for i in list:
#     h = soup.find_all("p")
#     for j in h:
#         if(s<6):
#             dat+=j.text.strip()+';'
#
#         elif(s>5):
#
#         # print(j.text)
#             sentence += j.text.strip()
#         else:
#             pass
#         s += 1
# new_date=dat.split(';')
#
# # for i in list:
#
# #     h = soup.find_all("p", {"class": "mol-para-with-font"})
# #     for j in h:
# #         sentence+=j.text.strip()
# cont='{} ; {} ; {} ; {}'.format(url,new_date[1][22:-40].strip(), list2,sentence)
