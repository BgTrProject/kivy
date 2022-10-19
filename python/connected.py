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


class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def page_one(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'tweetcollect'
        self.manager.get_screen('login').resetForm()

    def page_two(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'tweetquery'
        self.manager.get_screen('login').resetForm()

    def page_three(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'newpage'
        self.manager.get_screen('login').resetForm()

    def page_four(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'newpageTwo'
        self.manager.get_screen('login').resetForm()

    def page_five(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'facebook'
        self.manager.get_screen('login').resetForm()

    def page_six(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'eksi'
        self.manager.get_screen('login').resetForm()
    def page_seven(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'GoogleSearch'
        self.manager.get_screen('login').resetForm()
    def page_eight(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'googleTopik'
        self.manager.get_screen('login').resetForm()
    def page_nine(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'bing'
        self.manager.get_screen('login').resetForm()