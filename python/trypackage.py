import pkg_resources
import sys
import os
import subprocess


def controlpackage():
    for package in ['kivy','kivymd', 'pandas', 'tweepy', 'dtale', 'templates', 'snscrape','credentials','pyplotlib<3.3.0','requests_html','dateparser','demjson3','selenium','environ']:
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




