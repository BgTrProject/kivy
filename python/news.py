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


class News(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected_one'
        self.manager.get_screen('login').resetForm()

    def news(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'news_search'
        self.manager.get_screen('login').resetForm()

    def news_date_search(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'news_date_search'
        self.manager.get_screen('login').resetForm()

    

    