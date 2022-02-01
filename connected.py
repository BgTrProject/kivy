from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
        
    def page_one(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'googleSearch'
        self.manager.get_screen('login').resetForm()
    def page_two(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'googleTopik'
        self.manager.get_screen('login').resetForm()
    def page_three(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'bing'
        self.manager.get_screen('login').resetForm()