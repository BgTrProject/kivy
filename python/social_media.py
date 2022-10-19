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


class Social_Media(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected_one'
        self.manager.get_screen('login').resetForm()

    def tweepy(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'newpage'
        self.manager.get_screen('login').resetForm()

    def sns_scrape(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'newpageTwo'
        self.manager.get_screen('login').resetForm()

    def facebook(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'facebook'
        self.manager.get_screen('login').resetForm()

    def eksi(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'eksi'
        self.manager.get_screen('login').resetForm()