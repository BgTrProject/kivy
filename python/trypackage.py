import pkg_resources
import sys
import os
import subprocess


def controlpackage():
    for package in ['kivy','credentials', 'requests-oauthlib','pandas','dtale','templates','kivymd','selenium','bs4','requests-html','dateparser','demjson3','chromedriver-binary', 'Unidecode', 'feedparser', 'tldextract', 'Scrapy','dotmap','PyMySQL','psycopg2','elasticsearch','hjson','cchardet','webdriver-manager','html5lib']:   
        try:
            dist = pkg_resources.get_distribution(package)
            print('{} ({}) is installed'.format(dist.key, dist.version))
        except pkg_resources.DistributionNotFound:
            print('{} is NOT installed'.format(package))
            python = sys.executable
            print(package)
            subprocess.check_call(
                [python, '-m', 'pip', 'install', package], stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    controlpackage()
    os.sys('python main.py')




