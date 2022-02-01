from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from connected import Connected
from googleSearch  import GoogleSearch
from googleTopik  import GoogleTopik
from bing  import Bing


class Login(Screen):
    def do_login(self, loginText, passwordText): #giriş işleminde tetiklenen metot
        app = App.get_running_app()

        app.username = loginText #burda kontrol işlemi olcak
        app.password = passwordText
            
        if app.username=='a' and app.password=='': #kullanıcı adı şifre belirleme
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

            app.config.read(app.get_application_config()) #get_application_config metodunu çağırıyor 
            app.config.write()
        else:
            #burda yukardaki değerin eşleşmesi gerekiyor
            return

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(GoogleSearch(name='googleSearch')) #id isim vermesi gibi düşünün
        manager.add_widget(GoogleTopik(name='googleTopik'))
        manager.add_widget(Bing(name='bing'))
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

if __name__ == '__main__':
    LoginApp().run()