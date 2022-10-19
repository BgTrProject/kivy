from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.properties import StringProperty


class Search_Engine(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected_one'
        self.manager.get_screen('login').resetForm()

    def google_search(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'googleSearch'
        self.manager.get_screen('login').resetForm()

    def google_topik(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'googleTopik'
        self.manager.get_screen('login').resetForm()

    def bing(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'bing'
        self.manager.get_screen('login').resetForm()

    def news_google(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'news_on_google'
        self.manager.get_screen('login').resetForm()

    