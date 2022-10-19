import requests
import random
from collections import OrderedDict


# List of header that contain User-Agent
def list_header():
    headers_list = [
    # Firefox 24 Linux
        {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        },
        # Firefox Mac
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    ]

    return headers_list


def list_dict():
    # Get headers list
    headers_list = list_header()
    # Create ordered dict from Headers above
    ordered_headers_list = []
    for headers in headers_list:
        h = OrderedDict()
        for header, value in headers.items():
            h[header] = value
        ordered_headers_list.append(h)
    return ordered_headers_list


def list_test():
    headers_list = list_dict()
    max = len(headers_list)
    url = 'https://httpbin.org/headers'
    for i in range(0, max):
        # Pick a random browser headers
        headers = random.choice(headers_list)
        # Create a request session
        r = requests.Session()
        r.headers = headers

        response = r.get(url)
        print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:" % (i, headers['User-Agent']))
        print(response.json())
        print("-------------------")


def random_header():
    headers_list = list_dict()
    headers = random.choice(headers_list)
    return headers