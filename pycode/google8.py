from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import os, sys
import time,requests
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
from bs4 import BeautifulSoup

class google_search8:



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

        ########################################

        def audioToText(mp3Path):
            print("1")
            driver.execute_script('''window.open("","_blank");''')
            driver.switch_to.window(driver.window_handles[1])
            print("2")
            driver.get(googleIBMLink)
            delayTime = 10
            # Upload file
            time.sleep(1)
            print("3")
            # Upload file
            time.sleep(1)
            root = driver.find_element_by_id('root').find_elements_by_class_name('dropzone _container _container_large')
            btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
            btn.send_keys('C:/Users/AbdulBasit/Documents/google-captcha-bypass/1.mp3')
            # Audio to text is processing
            time.sleep(delayTime)
            # btn.send_keys(path)
            print("4")
            # Audio to text is processing
            time.sleep(audioToTextDelay)
            print("5")
            text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements_by_tag_name(
                'span')
            print("5.1")
            result = " ".join([each.text for each in text])
            print("6")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print("7")
            return result

        ###############################################################3
        def saveFile(content, filename):
            with open(filename, "wb") as handle:
                for data in content.iter_content():
                    handle.write(data)
                    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

        def coz(coz_filename):
            href = driver.find_element_by_id('audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response, coz_filename)
            response = audioToText(os.getcwd() + '/' + coz_filename)
            print(response)
            driver.switch_to.default_content()
            iframe = driver.find_elements_by_tag_name('iframe')[self.audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputbtn = driver.find_element_by_id('audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)
            time.sleep(2)
            errorMsg = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                print("Success")

            else:
                print("nanay")
                pass

        #------------------------

        delayTime = 2
        self.coz_filename="/home/bilgi/Desktop"
        self.audioBtnIndex = -1
        coz_filename=self.coz_filename
        audioToTextDelay = 10
        filename = '1.mp3'
        byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
        googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
        driver = webdriver.ChromeOptions()
        option = get_web_driver_options()
        option.add_argument('--disable-notifications')
        option.add_argument("--mute-audio")
        # option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        option.add_argument(
            "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")



        #######**********************************
        # driver.get(byPassUrl)
        # time.sleep(1)
        # googleClass = driver.find_elements_by_class_name('g-recaptcha')[0]
        # time.sleep(2)
        # outeriframe = googleClass.find_element_by_tag_name('iframe')
        # time.sleep(1)
        # outeriframe.click()
        # time.sleep(2)
        # allIframesLen = driver.find_elements_by_tag_name('iframe')
        # time.sleep(1)
        # audioBtnFound = False
        # audioBtnIndex = -1
        # for index in range(len(allIframesLen)):
        #     driver.switch_to.default_content()
        #     iframe = driver.find_elements_by_tag_name('iframe')[index]
        #     driver.switch_to.frame(iframe)
        #     driver.implicitly_wait(delayTime)
        #     try:
        #         if audioBtnFound == False:
        #             audioBtn = driver.find_element_by_id('recaptcha-audio-button') or driver.find_element_by_id(
        #                 'recaptcha-anchor')
        #             audioBtn.click()
        #             audioBtnFound = True
        #             audioBtnIndex = index
        #             break
        #         else:
        #             ##########################      kod blog başı         ################################
        #             google_search8()
        #
        #         #### ***********          kod blog sonu **************************
        #
        #
        #     except Exception as e:
        #         pass
        # if audioBtnFound:
        #     try:
        #         while True:
        #             href = driver.find_element_by_id('audio-source').get_attribute('src')
        #             response = requests.get(href, stream=True)
        #             saveFile(response, filename)
        #             response = audioToText(os.getcwd() + '/' + filename)
        #             print(response)
        #             driver.switch_to.default_content()
        #             iframe = driver.find_elements_by_tag_name('iframe')[audioBtnIndex]
        #             driver.switch_to.frame(iframe)
        #             inputbtn = driver.find_element_by_id('audio-response')
        #             inputbtn.send_keys(response)
        #             inputbtn.send_keys(Keys.ENTER)
        #             time.sleep(2)
        #             errorMsg = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
        #             if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
        #                 print("Success")
        #                 break
        #     except Exception as e:
        #         print(e)
        #         print('Caught. Need to change proxy now')
        # else:
        #     print('Button not found. This should not happen.')

        #--------------------------------------------





        url_list = []

        try:
            if len(driver.find_elements_by_xpath('//div[@id="result-stats"]')) != 0:
                results = driver.find_elements_by_xpath(
                    '//div[@id="result-stats"]')[0].text
                results = results[:results.find('results')]
                max_pages=1000


            if max_pages != 0:
                index = 0
                sayac=0

                while True:
                    has=driver.current_url
                    # print(has)
                    has=str(has)
                    if has.startswith("https://www.google.com/sorry/"):
                        print("beklemeye alındı cccc kodu")
                        coz(coz_filename)
                        time.sleep(25)
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
                                links = driver.find_elements_by_xpath(
                                    '//div[@class="yuRUbf"]/a')
                                linky = [link.get_attribute('href') for link in links]
                                url_list.extend(linky)
                                print('bbbbb')
                                print(linky)
                                print('cccc')



                                with open(filename, 'a', encoding='UTF8', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile, delimiter=' ') #, quotechar='|', quoting=csv.QUOTE_MINIMAL
                                    # csvwriter.writerow(['links'])
                                    for lin in linky:
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
                                links = driver.find_elements_by_xpath(
                                    '//div[@class="yuRUbf"]/a')
                                linky = [link.get_attribute('href') for link in links]
                                url_list.extend(linky)


                                with open(filename, 'a',encoding='UTF8', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile, delimiter=' ') #,quotechar='|', quoting=csv.QUOTE_MINIMAL


                                    for lin in linky:
                                        csvwriter.writerow([lin])
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
                pass
                raise ValueError(
                    'Your search - %s - did not match any documents.' % str(self.search_term))
            #

            url_list = list(dict.fromkeys(url_list))
            url_list = [url for url in url_list if '.pdf' not in url]
            self.urls = [url for url in url_list if '.xml' not in url]

        except:
            pass


        ###################################






