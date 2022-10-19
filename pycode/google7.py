from .helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)
from .utils import (BeautifulSoup, Options, UserAgent,webdriver_manager,
                              get, re, sys, time,
                             webdriver)
import csv

import random

from django.http import HttpResponse

from selenium import webdriver
import json
from fake_useragent import UserAgent


# class linkleri_al:
#     def dosya_olustur(self,isim, k):
#         for i in k:
#             with open(self.isim, 'a') as file:
#                 file.write(i + '\n')

class google_search7:

    def __init__(self, keyword, newspaper_url, filename, date1, date2):

        self.keyword = keyword
        self.newspaper_url = newspaper_url
        self.date1=date1
        self.date2=date2

        random_headers = {'User-Agent': UserAgent().random,
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
#&tbs=cdr:1,cd_min:01/01/2010,cd_max:02/01/2010
        self.search_term = '"{}" site:{}'.format(self.keyword, self.newspaper_url)
        # https: // www.google.com / search?q = {}{} site:{}{}&tbs=cdr:1,cd_min:{},cd_max:{}&
        urlk = "https://www.google.com/search?q={}".format('+'.join(self.search_term.split()))
        url = "{}&tbs=cdr:1,cd_min:{},cd_max:{}&".format(urlk, date1, date2)
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
                        # print(url)
                        # time.sleep(2)
                        # print(driver.get(url))
                        # h=driver.get(url)
                        # print(h)
                        # print(get_chrome_web_driver(url))
                        # if driver.get(url).startswith('https://www.google.com/sorry/'):
                        #     time.sleep(15)
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
                                links = driver.find_elements_by_xpath(
                                    '//div[@class="yuRUbf"]/a')
                                linky = [link.get_attribute('href') for link in links]
                                url_list.extend(linky)
                                print('bbbbb')
                                print(linky)
                                print('cccc')


                                # response = HttpResponse(content_type='text/csv')
                                # response['Content-Disposition'] = 'attachment; filename="venue.csv"'
                                # # create a csv writer
                                # writer = csv.writer(response)
                                # # venues = Venue.objects.all()
                                # # Add column headings to the csv file
                                # writer.writerow(['links'])

                                # lines=[]
                                with open(filename, 'a', encoding='UTF8', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile, delimiter=' ') #, quotechar='|', quoting=csv.QUOTE_MINIMAL
                                    # csvwriter.writerow(['links'])
                                    for lin in linky:
                                        csvwriter.writerow([lin])
                                        print("sssssssss")

                                # venue_csv(linky)
                                # for ii in linky:
                                #     venue_csv(ii)

                                    # csv.writer(ii)
                                    #
                                    # with open("abcde.txt", 'a') as file:
                                    #     file.write(ii + '\n')

                                try:
                                    driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
                                except:
                                    break

                                # time.sleep(15)


                                sys.stdout.write('\r No.of pages parsed : %s\r' % (str(index)))
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
                                linky = [link.get_attribute('href') for link in links]
                                url_list.extend(linky)

                                # response = HttpResponse(content_type='text/csv')
                                # response['Content-Disposition'] = 'attachment; filename="venue.csv"'
                                # # create a csv writer
                                # writer = csv.writer(response)
                                # venues = Venue.objects.all()
                                # Add column headings to the csv file
                                # writer.writerow(['links'])

                                # lines=[]

                                    # writer.writerow([lin])
                              # response = requests.get(
                            #     url="https://app.scrapingbee.com/api/v1/",
        #     params={
        #         "api_key": 'UCL6SGS4Q9Y8SERMTWWFDUQ98WLJH4Y5O4E4KEORTL99BSYJNRO4UUMW7DL8X6RWMXB4IL2OPHYTD25A',
        #         "url": url,
        #         "render_js": "false"
        #     }
        # )
        # if response.status_code == 200:
        #     return response
        # if response.status_code != 200:
        #     raise Exception("ScrapingBee status_code: "  + str(response.status_code) + " " + response.text)
                                with open(filename, 'a',encoding='UTF8', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile, delimiter=' ') #,quotechar='|', quoting=csv.QUOTE_MINIMAL


                                    for lin in linky:
                                        csvwriter.writerow([lin])
                                        print('ttttttt')



                                # venue_csv(linky)
                                # for jj in linky:
                                #
                                #     venue_csv(jj)
                                    # csv.writer(jj)
                                    # with open("abcde.txt", 'a') as file:
                                    #     file.write(jj + '\n')

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
                pass
                raise ValueError(
                    'Your search - %s - did not match any documents.' % str(self.search_term))
            #

            url_list = list(dict.fromkeys(url_list))
            url_list = [url for url in url_list if '.pdf' not in url]
            self.urls = [url for url in url_list if '.xml' not in url]

        except:
            pass
            # raise ValueError(
            #     'Your search - %s - did not match any documents.' % str(self.search_term))
    # def arat(self,a,b,c,d,e,f,g):
    #     h="https://www.google.com/search?q={}{} site:{}{}&tbs=cdr:1,cd_min:{},cd_max:{}&/headlines/section/topic/{}".format(a,b,c,d,e,f,g)
    #     print(h)
    #     https: // www.google.com / search?q = "virus"
    #     # site: https: // www.nytimes.com & tbs = cdr:1, cd_min: "2002-02-02", cd_max: "2009-10-10" & / headlines / section / topic / "BUSINESS"