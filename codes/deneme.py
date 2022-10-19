    # q=request.GET.get("newspaper_keyword")
    # fname=request.GET.get("newspaper_filename") #use as directory
    # cl_names=request.GET.get("newspaper_names")

from django.http.response import HttpResponse
from django.shortcuts import redirect
import os
import sys
import mimetypes
from io import StringIO
import zipfile
import requests
import csv
import json_normalize
import pandas as pd
import dtale
import time
from datetime import datetime
from datetime import timedelta
import numpy as np
from webapp.codes.dailySabah import *
from webapp.codes.dailyHurriyet import *
q="corona"
fname="denemee"
cl_names='dailySabah,dailyHurriyet'
fn = []
link_list=[]
content_list=[]
# fname="denemef"
way=""
cl = cl_names.split(",")
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
print(desktop)
way="{}{}{}/".format(desktop[:-7],"websites/rubic/webapp/g_upload/",fname)
print(way)

os.makedirs(way)
print("Directory '% s' created" % fname)

for i in cl:
    h_link = "{}{}_{}_link.txt".format(way,fname,i)
    h_content = "{}{}_{}_content.txt".format(way,fname,i)
    link_list.append(h_link)
    content_list.append(h_content)
    h = "{}".format(i.strip())
    print(h)
    print("--------hhhhhhh ---------------")
    fn.append(h)
ss = []
for i in range(len(cl)):
    print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
    print(i)
    ii = '{}={}(q,"{}","{}")'.format(cl[i], cl[i], fn[i],fname)
    print(ii)
    print("zzzzzzzzzzzzzzzzzzzzzzzz")
    ss.append(ii)
zeta = []
sayac=0
for i in ss:
    print(i)
    print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
    exec(i)
    d_link="{}".format(link_list[sayac])
    print("---------------------------------- dlink---------")
    print(d_link)
    print("???????????????????????")
    # download_file_g(d_link)

    # zipped_file = zipFiles(d_link)


    # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/',i)
    # r = requests.get(url, allow_redirects=True)
    # open('i', 'wb').write(r.content)

    z = i.split("=")
    print(z)
    zet = "{}{}".format(z[0], ".main()")
    zeta.append(zet)
    print("zeeeeeeeeeeettttttttttt")
    print(zet)
    exec(zet)
    d_content=("{}".format(content_list[sayac]))
    print(" ***************** d_content ****************")
    print(d_content)
    print(" ***************** d_content ****************")
    # zipped_file = zipFiles(d_content)
    # download_file_g(d_content)
    sayac+=1

    # url = "{}{}".format('/home/bilgi/websites/rubic/webapp/g_upload/', zet)
    # r = requests.get(url, allow_redirects=True)
    # open('zet', 'wb').write(r.content)

# newspaper_result="succesfully completed"
# response = HttpResponse(way, content_type='application/octet-stream')
# response['Content-Disposition'] = "attachment; filename=%s" % way[:-1]
# # response['Content-Disposition'] = 'attachment; ' filename=%s" % filename
# return response

