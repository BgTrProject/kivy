#
# import requests
# from webapp.pycode.user_agent import random_header
# import bs4
# import urllib
# import webbrowser
# c=0
# from bs4 import BeautifulSoup
# url="https://www.google.com/search?q=%22virus%22:+/headlines/section/topic%22https://www.nytimes.com%22&tbs=cdr:1,cd_min:01/01/2020,cd_max:01/01/2022&source=lnms&tbm=nws"
# r=requests.Session()
# headers=random_header()
# r.headers=headers
# res=r.get(url,headers=headers)
# soup=BeautifulSoup(res.text, "html.parser")
# links=soup.select('.kCrYT a')
# # links=soup.select('.kCrYT a')#class_='WlydOe'):
# for g in links:
#     c+=1
#     print(c)
#     # print(g)
#     # print(g.text)
#     print("----------------------")
#     j=g.get("href")
#     # print(j)
#     m=str(j)
#     if m.startswith("<a"):
#         mm=m[55:]
#         nn=mm.split('"')
#         print(nn[0])
#     else:
#         # pass
#         print(m[30:])
#     print("--------------------ss--")
#

#
# from pycode.bing import Bing
# key="welding"
# site="www.nytimes.com"
# url="samet.txt"
# a=Bing(key,site,url)
# h=a.crawl_all()