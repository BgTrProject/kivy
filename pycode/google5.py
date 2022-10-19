# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# from newsfetch.helpers import (get_chrome_web_driver, get_web_driver_options,
#                                set_automation_as_head_less,
#                                set_browser_as_incognito,
#                                set_ignore_certificate_error)
# root = "https://www.google.com/"
# # link = "https://www.google.com/search?q=biden&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwjAvsKDyOXtAhXBhOAKHXWdDgcQpwUIKQ&biw=1604&bih=760&dpr=1.2"
# # link="https://www.google.com/search?q=%22pakistan%22:+/headlines/section/topic/%22WORLD%22&tbs=cdr:1,cd_min:02-02-2010,cd_max:05-05-2015&tbm=nws"
# linky="https://www.google.com/search?q=%22pakistan%22:+/headlines/section/topic/%22WORLD%22&tbs=cdr:1,cd_min:02-02-2010,cd_max:05-05-2015&tbm=nws"
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# #
# # options = get_web_driver_options()
# # # options=webdriver.chrome('/usr/bin/chromedriver')
# # set_automation_as_head_less(options)
# # set_ignore_certificate_error(options)
# # set_browser_as_incognito(options)
# # driver = get_chrome_web_driver(options)
# from fake_useragent import UserAgent
# # pat=Serv"/usr/bin/chromedriver"
# ser = Service("/usr/bin/chromedriver")
# op = webdriver.ChromeOptions()
# s = webdriver.Chrome(service=ser, options=op)
# # driver = webdriver.Chrome(pat)
# # ua = UserAgent()
# # user_agent = ua.random
# # print(user_agent)
# # options.add_argument(f'user-agent={user_agent}')
# s.get(linky)
#
#
# # driver = webdriver.Chrome()
# # driver.get(linky)
# f = open('gggg.csv', 'w')
# f.write('Title,Link,Detail')
# for element in s.find_elements_by_xpath('//a[@class="WlydOe"]'):
#     print(element)
# # for element in driver.find_elements('//a[@class="ZINbbc xpd O9g5cc uUPGi"]'):
# # //a[@class='WlydOe']
#
#     # title = element.find_element_by_xpath('.//h3').text
#     # link = element.find_element_by_xpath('//a[@class="kCrYT"]').get_attribute('href')
#     link = element.find_element('//a[@class="kCrYT"]').get('href')
#     print(link)
#     # detail = element.find_element_by_xpath('.//span[@class="aCOpRe"]').text
#     # f.write(title.replace(',','|')+','+link.replace(',','|')+','+detail.replace(',','|')+'\n')
#
#
