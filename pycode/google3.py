from newsfetch.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)
from newsfetch.utils import (BeautifulSoup, Options, UserAgent,webdriver_manager,
                              get, re, sys, time,
                             webdriver)
import csv
# from home.views import venue_csv
from home.home.views import *
import random
from fake_useragent import UserAgent
from newsfetch.user_agent import random_header

from django.http import HttpResponse

from selenium import webdriver
import json
from fake_useragent import UserAgent
import requests


# class linkleri_al:
#     def dosya_olustur(self,isim, k):
#         for i in k:
#             with open(self.isim, 'a') as file:
#                 file.write(i + '\n')

class google_search3:

    def __init__(self, keyword, newspaper_url, filename, date1, date2):

        self.keyword = keyword
        self.newspaper_url = newspaper_url
        self.date1=date1
        self.date2=date2
        self.newspaper_url=self.newspaper_url.upper()

        random_headers = {'User-Agent': UserAgent().random,
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
#&tbs=cdr:1,cd_min:01/01/2010,cd_max:02/01/2010
        self.search_term = '"{}":+/headlines/section/topic/"{}"'.format(self.keyword, self.newspaper_url)
        # https: // www.google.com / search?q = {}{} site:{}{}&tbs=cdr:1,cd_min:{},cd_max:{}&
        urlk = "https://www.google.com/search?q={}".format('+'.join(self.search_term.split()))
        # url = "{}&tbs=cdr:1,cd_min:{},cd_max:{}&".format(urlk, date1, date2)
        url = "{}&tbs=cdr:1,cd_min:{},cd_max:{}&source=lnms&tbm=nws".format(urlk, date1, date2)  # source=lnms&tbm=nws

        options = get_web_driver_options()
        # options=webdriver.chrome('/usr/bin/chromedriver')
        set_automation_as_head_less(options)
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        # driver = get_chrome_web_driver(options)
        # from fake_useragent import UserAgent

        driver=webdriver.Chrome('/usr/bin/chromedriver')
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')
        driver.get(url)
        time.sleep(3)

        # // *[ @ id = "xjs"] / table / tbody / tr / td[3] / a
        # // *[ @ id = "result-stats"] / text()
        # // *[ @ id = "result-stats"] / text()
        # // *[ @ id = "result-stats"] / text()
        # // *[ @ id = "result-stats"] / text()
        # print(driver.get(url))
        #https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3D%2522vir%25C3%25BCs%2522%2Bsite:https://www.hurriyet.com.tr/%26ei%3DzPriYZmBDdyHxc8P7MW-2AE%26start%3D10%26sa%3DN%26ved%3D2ahUKEwiZl_r6mrT1AhXcQ_EDHeyiDxsQ8NMDegQIARBU%26biw%3D745%26bih%3D832&q=EgRY7KjLGM31i48GIhD3ZX7NkNWoBdbX8Bynx_ndMgFy
        url_list = []

        try:
            if len(driver.find_elements_by_xpath('//div[@id="result-stats"]')) != 0:
                results = driver.find_elements_by_xpath(
                    '//div[@id="result-stats"]')[0].text
                results = results[:results.find('results')]


                max_pages=1000
                # max_pages = round(
                #     int(int(''.join(i for i in results if i.isdigit())) / 10))
                # print("max =", max_pages)
                # url = "{}&tbs=cdr:1,cd_min:{},cd_max:{}&".format(urlk, date1, date2)

            if max_pages != 0:
                index = 0
                sayac=0

                while True:
                    has=driver.current_url
                    # print(has)
                    has=str(has)
                    if has.startswith("https://www.google.com/sorry/"):
                        print("beklemeye alındı cccc kodu")
                        time.sleep(45)
                    try:
                        h=driver.current_url
                        print(h)

                        if index<1:
                            ha = driver.current_url
                            print('aaaaa')


                            ha = str(ha)
                            if ha.startswith("https://www.google.com/sorry/"):
                                print("beklemeye alındı aaaa kodu")
                                time.sleep(45)
                            else:
                                sayac +=1
                                index +=1
                                links = driver.find_elements_by_xpath('//div[@class="a.WlydOe"]')
                                linky = [link.get_attribute('href') for link in links]
                                url_list.extend(linky)
                                print('bbbbb')
                                print(linky[1])
                                print('cccc')
                                for i in linky:
                                    print("samet")
                                    print(i)
                                    print("??????")

                                r = requests.Session()
                                headers = random_header()
                                r.headers = headers
                                res = r.get(ha, headers=random_headers)
                                # res = requests.get(ha,headers=random_headers)
                                soup = BeautifulSoup(res.text, "html.parser")
                                # links = soup.select(".dbsr a")
                                linksm = soup.select("zAoYTe")
                                linkym = [link.get('href') for link in linksm]
                                url_list.extend(linkym)

                                with open(filename, 'w', encoding='UTF8', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile, delimiter=' ') #, quotechar='|', quoting=csv.QUOTE_MINIMAL
                                    csvwriter.writerow(['links'])
                                    for lin in linky:
                                        csvwriter.writerow([lin])
                                        print("sssssssss")
                                    for lin in linkym:
                                        csvwriter.writerow([lin])
                                        print("sssssssss")



                                try:
                                    driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
                                except:
                                    break

                                sys.stdout.write('\r No.of pages parsed : %s\r' % (str(index)))
                                sys.stdout.flush()
                        else:
                            if ha.startswith("https://www.google.com/sorry/"):
                                print("beklemeye alındı bbbb kodu")
                                time.sleep(45)
                            else:

                                sayac += 1
                                index += 1



                                links = driver.find_elements_by_xpath('//div[@class="WlydOe"]')
                                linky = [link.a.get('href') for link in links]
                                url_list.extend(linky)


                                for i in linky:
                                    print("sametttttttt")
                                    print(i)
                                    print("??????+++++++++")


                                r = requests.Session()
                                headers = random_header()
                                r.headers = headers
                                res = r.get(ha,headers=random_headers)
                                soup = BeautifulSoup(res.text, "html.parser")
                                # links = soup.select(".dbsr a")
                                linksm = soup.select(".zAoYTe a")
                                linkym2 = [l.get('href') for l in linksm]
                                url_list.extend(linkym2)
                                with open(filename, 'a',encoding='UTF8', newline='') as csvfile:
                                    csvwriter2 = csv.writer(csvfile, delimiter=' ') #,quotechar='|', quoting=csv.QUOTE_MINIMAL
                                    # csvwriter2.writerow(['links'])
                                    print("pppppp")
                                    print(len(linkym2))
                                    for lin in linky:
                                        csvwriter.writerow([lin])
                                        print("sssssssss")
                                    for lin in linkym2:
                                        csvwriter2.writerow([lin])
                                        print('ttttttt')


                                try:

                                    driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
                                except:
                                    break

                                time.sleep(2)
                                sys.stdout.write('\r No.of pages parsed : %s\r' % (str(index)))
                                sys.stdout.flush()

                    except:
                        continue

                driver.quit()
            else:
                raise ValueError(
                    'Your search - %s - did not match any documents.' % str(self.search_term))
            #

            url_list = list(dict.fromkeys(url_list))
            url_list = [url for url in url_list if '.pdf' not in url]
            self.urls = [url for url in url_list if '.xml' not in url]

        except:
            raise ValueError(
                'Your search - %s - did not match any documents.' % str(self.search_term))
