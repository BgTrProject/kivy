# Social_Media App
#after Download before start please follow these steps

#firstly download chromedriver which is suitible with your google chrome version

#then if your os is linux => copy the chromedriver to '/usr/bin/'

#.....if your os is windows => copy the chromedriver to 'C://'


# Create virtual env
python -m venv venv

# install modules which is required
python python/trypackage.py

# Start Project 
python main.py



iyi çalışmalar ....



Arayüzdeki modullerin kullanımı için :


Tweepy modülü:

![](/kivy_pictures/s_teepy_q.png)

Tweepy modulu kullanılarak arama gerçekleştirme:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili arama kelimesi (keyword) ve istenilen sonuçtan kaç adet talep edileceği (max result) ve hangi
dilde arama yapılacağı girildikten sonra ilgili sonuçların hangi dosya adında kaydedileceği (file name)
belirtip arama (search) butonuna tıklanır.

