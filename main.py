import os
# os.system("python.trypackage.py")
from python.newpageTwo import NewPageTwo
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from turtle import title
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.properties import StringProperty


from python.tweetcollect import TweetCollect
from python.newpage import NewPage
from python.newpageTwo import NewPageTwo
from python.eksi import EksiKV
from python.facebook import FacebookKV
from python.googleSearch import GoogleSearch
from python.googleTopik import GoogleTopik
from python.bing import Bing
from python.connected_one import Connected_one
from python.social_media import Social_Media
from python.search_engine import Search_Engine
from python.news import News
from python.news_search import News_Search
from python.news_date_search import News_Date_Search
from python.news_on_google import NewsGoogle

# from python.tweetquery import TweetQuery
import webbrowser
import pkg_resources
import sys
import subprocess


# Set the app size
Window.size = (1000, 800)
Window.top = 30

# Designate Our .kv design file
# Builder.load_file('login.kv')

class Login(Screen):
    
    def do_login(self, loginText, passwordText):  # giriş işleminde tetiklenen metot
        app = App.get_running_app()
        
        app.username = loginText  # burda kontrol işlemi olcak
        app.password = passwordText

        if app.username == '' and app.password == '':  # kullanıcı adı şifre belirleme
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected_one'

            # get_application_config metodunu çağırıyor
            app.config.read(app.get_application_config())
            app.config.write()
        else:
            return


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def git(self):
        webbrowser.open('https://github.com/doukansurel')
        webbrowser.open('https://github.com/BgTrProject/')


    

class LoginApp(MDApp):
    title ="Scraping"
    icon ="image/twit.png"
    username = StringProperty(None)
    password = StringProperty(None)
    def build(self):
        self.theme_cls.theme_style= "Dark"
        
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
       
        manager.add_widget(Connected_one(name='connected_one'))
        manager.add_widget(NewPage(name='newpage'))
        manager.add_widget(NewPageTwo(name='newpageTwo'))
        manager.add_widget(TweetCollect(name='tweetcollect'))
        manager.add_widget(FacebookKV(name='facebook'))
        manager.add_widget(EksiKV(name='eksi'))
        manager.add_widget(GoogleSearch(name='googleSearch'))  # id isim vermesi gibi düşünün
        manager.add_widget(GoogleTopik(name='googleTopik'))
        manager.add_widget(Bing(name='bing'))
        manager.add_widget(Social_Media(name='social_media'))
        manager.add_widget(Search_Engine(name='search_engine'))
        manager.add_widget(News(name='news'))
        manager.add_widget(News_Search(name='news_search'))
        manager.add_widget(News_Date_Search(name='news_date_search'))
        manager.add_widget(NewsGoogle(name='news_on_google'))
        # manager.add_widget(TweetQuery(name='tweetquery'))
        
        return manager

    def get_application_config(self):
        
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        
        )



LoginApp().run()
