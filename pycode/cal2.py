

from webapp.pycode.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error)
from webapp.pycode.utils import (BeautifulSoup, Options, UserAgent,webdriver_manager,
                              get, re, sys, time,
                             webdriver)
import csv

import random

from django.http import HttpResponse

from selenium import webdriver
import json
from fake_useragent import UserAgent
from webapp.pycode.user_agent import random_header
from webapp.pycode.bing3 import Bing3



from webapp.pycode.ddgoog import google_searchs

# keyword="virus"
# newspaper_url="https://www.nytimes.com"
# filename="asab"
# date1="01/01/2020"
# date2="01/01/2022"
#
# h=Bing3(searched_item=keyword,site=newspaper_url,date1=date1,date2=date2,urls_file=filename)
