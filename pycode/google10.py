from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from newsfetch.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)
from newsfetch.utils import (BeautifulSoup, Options, UserAgent,
                             get, re, sys, time,
                             webdriver)#webdriver_manager,
import csv
import random
# from django.http import HttpResponse
from selenium import webdriver
import json
from fake_useragent import UserAgent


class Google_Search10(Screen):
    def __init__(self, search_keyword, site_url, file_name, start_date, end_date,os_find):
        self.os_find=os_find

        self.keyword = search_keyword
        self.newspaper_url = site_url
        self.date1 = start_date
        self.date2 = end_date

        random_headers = {'User-Agent': UserAgent().random,
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        self.search_term = '"{}" site:{}'.format(
            self.keyword, self.newspaper_url)
        urlk = "https://www.google.com/search?q={}".format(
            '+'.join(self.search_term.split()))
        url = "{}&tbs=cdr:1,cd_min:{},cd_max:{}&".format(
            urlk, start_date, end_date)
        options = get_web_driver_options()
        # options=webdriver.chrome('/usr/bin/chromedriver')
        set_automation_as_head_less(options)
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)

        # driver = webdriver.Chrome('/usr/bin/chromedriver') #kendi masaüstü yolunuzu verin
        driver = webdriver.Chrome(self.os_find)  # kendi masaüstü yolunuzu verin
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')
        driver.get(url)
        time.sleep(3)

        url_list = []

        try:
            if len(driver.find_elements_by_xpath('//div[@id="result-stats"]')) != 0:
                results = driver.find_elements_by_xpath(
                    '//div[@id="result-stats"]')[0].text
                results = results[:results.find('results')]
                max_pages = 1000

            if max_pages != 0:
                index = 0
                sayac = 0

                while True:
                    has = driver.current_url

                    has = str(has)
                    if has.startswith("https://www.google.com/sorry/"):
                        print("beklemeye alındı cccc kodu")
                        time.sleep(45)
                    try:
                        h = driver.current_url
                        print(h)

                        if index < 1:
                            ha = driver.current_url
                            print('aaaaa')

                            ha = str(ha)
                            if ha.startswith("https://www.google.com/sorry/"):
                                print("beklemeye alındı aaaa kodu")
                                time.sleep(45)
                            else:

                                sayac += 1
                                index += 1
                                links = driver.find_elements_by_xpath(
                                    '//div[@class="yuRUbf"]/a')
                                linky = [link.get_attribute(
                                    'href') for link in links]
                                url_list.extend(linky)
                                # print('bbbbb')
                                # print(linky)
                                # print('cccc')
                                print("********")
                                print(file_name)
                                print("********")
                                with open(file_name, 'w', encoding='UTF8', newline='') as csvfile:
                                    # , quotechar='|', quoting=csv.QUOTE_MINIMAL
                                    csvwriter = csv.writer(
                                        csvfile, delimiter=' ')
                                    csvwriter.writerow(['links'])
                                    for lin in linky:
                                        csvwriter.writerow([lin])
                                        print("sssssssss")
                                try:
                                    driver.find_element_by_xpath(
                                        '//*[@id="pnnext"]/span[2]').click()
                                except:
                                    break
                                sys.stdout.write(
                                    '\r No.of pages parsed : %s\r' % (str(index)))
                                sys.stdout.flush()
                        else:
                            if ha.startswith("https://www.google.com/sorry/"):
                                print("beklemeye alındı bbbb kodu")
                                time.sleep(45)
                            else:

                                sayac += 1
                                index += 1
                                links = driver.find_elements_by_xpath(
                                    '//div[@class="yuRUbf"]/a')
                                linky = [link.get_attribute(
                                    'href') for link in links]
                                url_list.extend(linky)
                                print("********")
                                print(file_name)
                                with open(file_name, 'a', encoding='UTF8', newline='') as csvfile:
                                    # ,quotechar='|', quoting=csv.QUOTE_MINIMAL
                                    csvwriter = csv.writer(
                                        csvfile, delimiter=' ')

                                    for lin in linky:
                                        csvwriter.writerow([lin])
                                        print('ttttttt')
                                try:

                                    driver.find_element_by_xpath(
                                        '//*[@id="pnnext"]/span[2]').click()
                                except:
                                    break

                                time.sleep(2)
                                sys.stdout.write(
                                    '\r No.of pages parsed : %s\r' % (str(index)))
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
