from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
import sys
from kivy.properties import StringProperty
import webbrowser
from kivy.clock import Clock

import csv
import dtale
import pandas as pd

import time
from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time
import numpy as np

import requests

from newspaper_codes.dnevnik import *
from newspaper_codes.trud import *
from newspaper_codes.bgnes import *
from newspaper_codes.banker import *
from newspaper_codes.sega import *



from newspaper_codes.dwnews import *
from newspaper_codes.guardian import *
from newspaper_codes.independent import *
from newspaper_codes.dailymail import *
from newspaper_codes.dailysabah import *

from newspaper_codes.ensonhaber import *
from newspaper_codes.sozcu import *
from newspaper_codes.haberler import *
from newspaper_codes.evrensel import *
from newspaper_codes.hurriyet import *
from newspaper_codes.memurlar import *
from newspaper_codes.turkiye import *
from newspaper_codes.sabah import *
from newspaper_codes.milli import *
from newspaper_codes.duvar import *
from newspaper_codes.odatv4 import *
from newspaper_codes.cumhuriyet import *

class News_Date_Search(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'news'
        self.manager.get_screen('login').resetForm()
    def open_page(self):
        
        webbrowser.open('html_files\\news_date_search.html')
    def run(self, cat, d1, d2, n_name, fname):
        self.function_interval = Clock.schedule_interval(self.nd_update_label, 0.05)
        self.fname = fname
        self.filname4 = self.fname + ".txt"
        self.os_send=""


        self.d1 = d1
        self.d2 = d2
        self.cat = cat
        self.n_name = n_name
        # self.cat=cat

        # try:
        #     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        #     print(desktop)
        # except:
        #     print("Linux Veya Unix Yolu Bulunamadı")
        # h = os.getcwd()
        # filname5 = self.filname4
        # if (h.startswith("/home")):
        #
        #     try:
        #         ff=str(self.filname4)
        #         filname44=desktop+"/"+self.filname4
        #         print("filname4 = {}".format(filname44))
        #         with open(filname44, 'a', newline='', encoding="utf-8") as f:
        #             f.write("ok completed {} {} {} {} {}".format(self.cat,self.fname,self.d1,self.d2,self.newspaper_name))
        #         # print("Directory '%s' created successfully" % fname)
        #
        #         print("ok")
        #         print("cccccccccccccccccccccccccc")
        #         self.ids.deneme.text == "Succes."
        #         self.nd_update_label2("Succes.")
        #     except:
        #         pass
        # else:
        #     pass

        # self.fname=fname
        # self.filname4=fname

        fn = []
        link_list = []
        content_list = []
        file_list = []

        # cl = cl_names_all.split(",")
        cl = self.n_name.split(",")

        try:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            print(desktop)
        except:
            print("Linux Veya Unix Yolu Bulunamadı")
        h = os.getcwd()
        # self.fnames = desktop + "/" + fname + '_content.txt'
        self.fnames = desktop + "/" + fname + '_content.csv'
        # self.fnames = "{}{}".format(fname, "_content.txt")
        # self.fnames=desktop+self.fnames
        filname5 = self.filname4
        if (h.startswith("/home")): ## linux için
            self.os_send="/usr/bin/chromedriver"

            try:
                ff = str(self.filname4)
                filname44 = desktop + "/" + self.filname4
                way = filname44
                print("filname4 = {}".format(way))

                # try:
                #     os.makedirs(way, exist_ok=True)
                #     print("Directory '%s' created successfully" % fname)
                # except OSError as error:
                #     newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname

                for i in cl:
                    h_link = "{}{}_{}_link.txt".format(fname, fname, i)#way
                    h_content = "{}{}_{}_content.txt".format(fname, fname, i)
                    link_list.append(h_link)
                    content_list.append(h_content)

                    file_list.append(h_link)
                    file_list.append(h_content)

                    h = "{}".format(i.strip())
                    print(h)
                    print(h_link)
                    print(h_content)
                    print("--------hhhhhhh ---------------")
                    fn.append(h)
                ss = []
                print(type(d1))
                for i in range(len(cl)):
                    print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
                    print(i)
                    print(cl[i])
                    print(fn[i])
                    print(fname)
                    print(filname44)
                    print(way)
                    print(self.filname4)

                    ii = '{}={}("{}","{}","{}","{}","{}","{}")'.format(cl[i], cl[i], self.d1, self.d2, self.cat, fn[i],
                                                                  fname,self.os_send) #fname
                    print(ii)
                    print("zzzzzzzzzzzzzzzzzzzzzzzz")
                    ss.append(ii)
                zeta = []
                sayac = 0
                for i in ss:
                    print(i)
                    # i=str(i)
                    print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")

                    # a = "virus"
                    # b = "2020-10-11"
                    # c = "2020-11-11"
                    # d = "milli"
                    # e = "iiiii909"
                    # h = i(b, c, a, d, e)
                    # # h.main()
                    # # h.main()
                    # # milli.main()
                    # s = "h.main()"
                    # exec(s)
                    print("============----------------==========")
                    exec(i)
                    print("============----------------==========")
                    # try:
                    #     # exec(str(i))
                    #     exec(i)
                    #
                    # except:
                    #     print("haaaaaaaaaaaaaataaaaaaaa")
                    d_link = "{}".format(link_list[sayac])
                    print("---------------------------------- dlink---------")
                    print(d_link)
                    print("???????????????????????")

                    z = i.split("=")
                    print(z)
                    zet = "{}{}".format(z[0], ".main()")
                    zeta.append(zet)
                    print("zeeeeeeeeeeettttttttttt")
                    print(zet)
                    exec(str(zet))
                    d_content = ("{}".format(content_list[sayac]))
                    print(" ***************** d_content ****************")
                    print(d_content)
                    print(" ***************** d_content ****************")
                    # zipped_file = zipFiles(d_content)
                    # download_file_g(d_content)
                    sayac += 1

                newspaper_result = "succesfully completed try another search"
                print(newspaper_result)

                df = pd.read_csv(self.fnames)
                d = dtale.show(df)
                d.open_browser()
                #
                # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
                # # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                # # file_path = BASE_DIR + '/g_upload/' + fname
                # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
                # print(file_path)
                # zf = "{}/{}".format(file_path, fname)
                # print(zf)
                # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
                # shutil.make_archive(zf, 'zip', file_path, '{}.csv'.format(fname))

                # shutil.make_archive(zf, 'zip', file_path, '{}_{}_content.txt'.format(fname, cl[0]))  # ,'{}'.format(fname))
                # zf_s = "{}{}".format(zf, '.zip')
                # print(zf_s)
                #
                # file = open(zf_s, 'rb')
                # response = FileResponse(file)
                # response['Content-Type'] = 'application/octet-stream'
                # response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)

                # return response
            except:
                pass
        else:   # windows için
            self.os_send = "C:\\"
            try:
                ff = str(self.filname4)
                filname44 = desktop + "\\" + self.filname4   #değiştirilecek yer
                way = filname44
                print("filname4 = {}".format(filname44))

                for i in cl:
                    h_link = "{}{}_{}_link.txt".format(fname, fname, i)  ##way->fname
                    h_content = "{}{}_{}_content.txt".format(fname, fname, i)
                    link_list.append(h_link)
                    content_list.append(h_content)

                    file_list.append(h_link)
                    file_list.append(h_content)

                    h = "{}".format(i.strip())
                    print(h)
                    print("--------hhhhhhh ---------------")
                    fn.append(h)
                ss = []
                print(type(d1))
                for i in range(len(cl)):
                    print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
                    print(i)

                    ii = '{}={}("{}","{}","{}","{}","{}","{}")'.format(cl[i], cl[i], self.d1, self.d2, self.cat, fn[i],
                                                                  fname,self.os_send)
                    print(ii)
                    print("zzzzzzzzzzzzzzzzzzzzzzzz")
                    ss.append(ii)
                zeta = []
                sayac = 0
                for i in ss:
                    print(i)
                    print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
                    exec(i)
                    d_link = "{}".format(link_list[sayac])
                    print("---------------------------------- dlink---------")
                    print(d_link)
                    print("???????????????????????")

                    z = i.split("=")
                    print(z)
                    zet = "{}{}".format(z[0], ".main()")
                    zeta.append(zet)
                    print("zeeeeeeeeeeettttttttttt")
                    print(zet)
                    exec(zet)
                    d_content = ("{}".format(content_list[sayac]))
                    print(" ***************** d_content ****************")
                    print(d_content)
                    print(" ***************** d_content ****************")
                    # zipped_file = zipFiles(d_content)
                    # download_file_g(d_content)
                    sayac += 1

                newspaper_result = "succesfully completed try another search"
                print(newspaper_result)
                #
                # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
                # # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                # # file_path = BASE_DIR + '/g_upload/' + fname
                # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
                # print(file_path)
                # zf = "{}/{}".format(file_path, fname)
                # print(zf)
                # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
                # shutil.make_archive(zf, 'zip', file_path, '{}.csv'.format(fname))

                # shutil.make_archive(zf, 'zip', file_path, '{}_{}_content.txt'.format(fname, cl[0]))  # ,'{}'.format(fname))
                # zf_s = "{}{}".format(zf, '.zip')
                # print(zf_s)
                #
                # file = open(zf_s, 'rb')
                # response = FileResponse(file)
                # response['Content-Type'] = 'application/octet-stream'
                # response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)

                # return response
            except:
                pass

    def nd_update_label2(self, txt, filname4, *args):  # eklenecek
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        filname4 = desktop + "/" + filname4 + ".csv"
        self.ids.deneme.text = txt
        print("-------")
        print(self.ids.deneme.text)
        print("*******")
        if (self.ids.deneme.text == "Succes."):
            print("girdi")
            self.ids.deneme.text = "finished successfully at PATH : {} ".format(filname4)
            print(self.filname4)
            self.function_interval.cancel()
        else:
            print("nanay")
            print(self.ids.deneme.text)
            self.ids.deneme.text = "finished . PATH: " + self.filname4
            print(self.filname4)
            self.function_interval.cancel()

    def nd_update_label(self, *args):  # eklenecek
        print(self.ids.deneme.text)
        if (self.ids.deneme.text == "Loading..."):
            print("girdi")
            self.function_interval.cancel()
            News_Date_Search.run(self, self.keyword, self.d1, self.d2, self.newspaper_name, self.fname)
            self.nd_update_label2("Succes.", self.filname4)

    def nd_router(self, keyword, d1, d2, newspaper_name, fname):   # kv den gelen root.x()
        self.keyword = keyword
        self.d1 = d1
        self.d2 = d2
        self.fname = fname
        self.newspaper_name = newspaper_name

        self.ids.deneme.text = "Loading..."
        self.function_interval = Clock.schedule_interval(self.nd_update_label, 0.05)





    # def run(self, cat, d1, d2, n_name, fname):
    #     self.function_interval = Clock.schedule_interval(self.nd_update_label, 0.05)
    #     self.fname = fname
    #     self.filname4 = self.fname + ".txt"
    #
    #     self.d1 = d1
    #     self.d2 = d2
    #     self.cat = cat
    #     self.n_name = n_name
    #     # self.cat=cat
    #
    #     # try:
    #     #     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    #     #     print(desktop)
    #     # except:
    #     #     print("Linux Veya Unix Yolu Bulunamadı")
    #     # h = os.getcwd()
    #     # filname5 = self.filname4
    #     # if (h.startswith("/home")):
    #     #
    #     #     try:
    #     #         ff=str(self.filname4)
    #     #         filname44=desktop+"/"+self.filname4
    #     #         print("filname4 = {}".format(filname44))
    #     #         with open(filname44, 'a', newline='', encoding="utf-8") as f:
    #     #             f.write("ok completed {} {} {} {} {}".format(self.cat,self.fname,self.d1,self.d2,self.newspaper_name))
    #     #         # print("Directory '%s' created successfully" % fname)
    #     #
    #     #         print("ok")
    #     #         print("cccccccccccccccccccccccccc")
    #     #         self.ids.deneme.text == "Succes."
    #     #         self.nd_update_label2("Succes.")
    #     #     except:
    #     #         pass
    #     # else:
    #     #     pass
    #
    #     # self.fname=fname
    #     # self.filname4=fname
    #
    #     fn = []
    #     link_list = []
    #     content_list = []
    #     file_list = []
    #
    #     # cl = cl_names_all.split(",")
    #     cl = self.n_name.split(",")
    #
    #     try:
    #         desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    #         print(desktop)
    #     except:
    #         print("Linux Veya Unix Yolu Bulunamadı")
    #     h = os.getcwd()
    #     filname5 = self.filname4
    #     if (h.startswith("/home")): ## linux için
    #
    #         try:
    #             ff = str(self.filname4)
    #             filname44 = desktop + "/" + self.filname4
    #             way = filname44
    #             print("filname4 = {}".format(way))
    #
    #             try:
    #                 os.makedirs(way, exist_ok=True)
    #                 print("Directory '%s' created successfully" % fname)
    #             except OSError as error:
    #                 newspaper_result = "Directory '%s' can not be created. Allready exist please change name and try again" % fname
    #
    #             for i in cl:
    #                 h_link = "{}{}_{}_link.txt".format(way, fname, i)#way
    #                 h_content = "{}{}_{}_content.txt".format(way, fname, i)
    #                 link_list.append(h_link)
    #                 content_list.append(h_content)
    #
    #                 file_list.append(h_link)
    #                 file_list.append(h_content)
    #
    #                 h = "{}".format(i.strip())
    #                 print(h)
    #                 print(h_link)
    #                 print(h_content)
    #                 print("--------hhhhhhh ---------------")
    #                 fn.append(h)
    #             ss = []
    #             print(type(d1))
    #             for i in range(len(cl)):
    #                 print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
    #                 print(i)
    #                 print(cl[i])
    #                 print(fn[i])
    #                 print(fname)
    #                 print(filname44)
    #                 print(way)
    #                 print(self.filname4)
    #
    #                 ii = '{}={}("{}","{}","{}","{}","{}")'.format(cl[i], cl[i], self.d1, self.d2, self.cat, fn[i],
    #                                                               fname) #fname
    #                 print(ii)
    #                 print("zzzzzzzzzzzzzzzzzzzzzzzz")
    #                 ss.append(ii)
    #             zeta = []
    #             sayac = 0
    #             for i in ss:
    #                 print(i)
    #                 print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
    #                 try:
    #                     # exec(str(i))
    #                     exec(i)
    #
    #                 except:
    #                     print("haaaaaaaaaaaaaataaaaaaaa")
    #                 d_link = "{}".format(link_list[sayac])
    #                 print("---------------------------------- dlink---------")
    #                 print(d_link)
    #                 print("???????????????????????")
    #
    #                 z = i.split("=")
    #                 print(z)
    #                 zet = "{}{}".format(z[0], ".main()")
    #                 zeta.append(zet)
    #                 print("zeeeeeeeeeeettttttttttt")
    #                 print(zet)
    #                 exec(str(zet))
    #                 d_content = ("{}".format(content_list[sayac]))
    #                 print(" ***************** d_content ****************")
    #                 print(d_content)
    #                 print(" ***************** d_content ****************")
    #                 # zipped_file = zipFiles(d_content)
    #                 # download_file_g(d_content)
    #                 sayac += 1
    #
    #             newspaper_result = "succesfully completed try another search"
    #             print(newspaper_result)
    #             #
    #             # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
    #             # # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #             # # file_path = BASE_DIR + '/g_upload/' + fname
    #             # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    #             # print(file_path)
    #             # zf = "{}/{}".format(file_path, fname)
    #             # print(zf)
    #             # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    #             # shutil.make_archive(zf, 'zip', file_path, '{}.csv'.format(fname))
    #
    #             # shutil.make_archive(zf, 'zip', file_path, '{}_{}_content.txt'.format(fname, cl[0]))  # ,'{}'.format(fname))
    #             # zf_s = "{}{}".format(zf, '.zip')
    #             # print(zf_s)
    #             #
    #             # file = open(zf_s, 'rb')
    #             # response = FileResponse(file)
    #             # response['Content-Type'] = 'application/octet-stream'
    #             # response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
    #
    #             # return response
    #         except:
    #             pass
    #     else:   # windows için
    #         try:
    #             ff = str(self.filname4)
    #             filname44 = desktop + "\\" + self.filname4   #değiştirilecek yer
    #             way = filname44
    #             print("filname4 = {}".format(filname44))
    #
    #             for i in cl:
    #                 h_link = "{}{}_{}_link.txt".format(way, fname, i)
    #                 h_content = "{}{}_{}_content.txt".format(way, fname, i)
    #                 link_list.append(h_link)
    #                 content_list.append(h_content)
    #
    #                 file_list.append(h_link)
    #                 file_list.append(h_content)
    #
    #                 h = "{}".format(i.strip())
    #                 print(h)
    #                 print("--------hhhhhhh ---------------")
    #                 fn.append(h)
    #             ss = []
    #             print(type(d1))
    #             for i in range(len(cl)):
    #                 print("rrrrrrrrrrrrrrrrrrrrrrrrrr")
    #                 print(i)
    #
    #                 ii = '{}={}("{}","{}","{}","{}","{}")'.format(cl[i], cl[i], self.d1, self.d2, self.cat, fn[i],
    #                                                               fname)
    #                 print(ii)
    #                 print("zzzzzzzzzzzzzzzzzzzzzzzz")
    #                 ss.append(ii)
    #             zeta = []
    #             sayac = 0
    #             for i in ss:
    #                 print(i)
    #                 print("yyyyyyyyyyzyzyzyzyyzyzyzyzyzy***********")
    #                 exec(i)
    #                 d_link = "{}".format(link_list[sayac])
    #                 print("---------------------------------- dlink---------")
    #                 print(d_link)
    #                 print("???????????????????????")
    #
    #                 z = i.split("=")
    #                 print(z)
    #                 zet = "{}{}".format(z[0], ".main()")
    #                 zeta.append(zet)
    #                 print("zeeeeeeeeeeettttttttttt")
    #                 print(zet)
    #                 exec(zet)
    #                 d_content = ("{}".format(content_list[sayac]))
    #                 print(" ***************** d_content ****************")
    #                 print(d_content)
    #                 print(" ***************** d_content ****************")
    #                 # zipped_file = zipFiles(d_content)
    #                 # download_file_g(d_content)
    #                 sayac += 1
    #
    #             newspaper_result = "succesfully completed try another search"
    #             print(newspaper_result)
    #             #
    #             # file_path = os.path.join(settings.DOWNLOAD_G_ROOT, fname)
    #             # # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #             # # file_path = BASE_DIR + '/g_upload/' + fname
    #             # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    #             # print(file_path)
    #             # zf = "{}/{}".format(file_path, fname)
    #             # print(zf)
    #             # print("+-+--+-+--+-+-+--+-+-+--+-+--+-+--+--+-+-+-+-+--+")
    #             # shutil.make_archive(zf, 'zip', file_path, '{}.csv'.format(fname))
    #
    #             # shutil.make_archive(zf, 'zip', file_path, '{}_{}_content.txt'.format(fname, cl[0]))  # ,'{}'.format(fname))
    #             # zf_s = "{}{}".format(zf, '.zip')
    #             # print(zf_s)
    #             #
    #             # file = open(zf_s, 'rb')
    #             # response = FileResponse(file)
    #             # response['Content-Type'] = 'application/octet-stream'
    #             # response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(fname)
    #
    #             # return response
    #         except:
    #             pass