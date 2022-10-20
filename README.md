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

![](/kivy_pictures/s_teepy_t.png)

Tweepy modülünü kullanarak zaman şeridi üzerinde arama yapma:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili zaman şeridi sonucu için sadece istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin
girilmesi yeterlidir. Daha sonra indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip
arama (search) butonu tıklanır.

![](/kivy_pictures/sns.png)

Tweepy modülünü kullanarak coğrafik arama yapma:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
Apinin modulunun coğrafik araması belirtilen cografik kod ait lokasyonda atılmış olan tweetleri
toplar. İlgili cografik kod (geo code) girilmesi ve indirilecek dosyaların hangi isimde kaydedileceği (file
name) belirtilip arama (search) butonu tıklanır.


![](/kivy_pictures/s_teepy_q.png)

Snscrape Modulu:
Snscrape, sosyal ağ hizmetleri için bir (scraper) kazıyıcıdır. Kullanıcı profilleri, hashtag’lar gibi şeyleri
aratır ve ilgili sonuçları (tweetleri) geri döndürür.
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles,
hashtags, or searches and returns the discovered items, e.g. the relevant posts.
Basit arama (Simple Search snscrape):
Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi akabinde
tarih (date) ve aranılacak kelime (keyword) girilip indirilecek dosyaların hangi isimde kaydedileceği
(file name) belirtilip arama (search) butonu tıklanır.
Karmaşık arama (Complex Search snscrape):
Bu modul iki farklı şekilde kullanılır. 1-keyworde göre arama 2-hashtage göre arama
1-keyworde göre arama:Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi, hangi
dilde(language) arama yapılacağı seçimi yapılıp, akabinde tarih (date) ve aranılacak kelime (keyword)
girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama (search) butonu
tıklanır.
2- hashtage göre arama:
Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi, hangi
dilde(language) arama yapılacağı seçimi yapılıp, akabinde tarih (date) ve aranılacak hashtag başında
@ işareti ile girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama
(search) butonu tıklanır.

KJABFASKJFNASKLFNASFKASLKSFFSA
