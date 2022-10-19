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


class Connected_one(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def social_media(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'social_media'
        self.manager.get_screen('login').resetForm()

    def search_engine(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'search_engine'
        self.manager.get_screen('login').resetForm()

    def news(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'news'
        self.manager.get_screen('login').resetForm()