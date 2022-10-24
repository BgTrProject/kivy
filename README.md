# Social_Media App
#Download your pc

git clone https://github.com/BgTrProject/kivy.git

#after Download before start please follow these steps

#firstly download chromedriver which is suitible with your google chrome version

#then if your os is linux => copy the chromedriver to '/usr/bin/'

#.....if your os is windows => copy the chromedriver to 'C://'


# Create virtual env
conda create --name env

# Activate virtualenvirement
conda activate env


# install modules which is required

conda install -c conda-forge tk

conda install -c conda-forge kivy

pip install -r requirements.txt

# Start Project 

python main.py



Uygulamanın Başlangıç Sayfası:



![](/Kivy_App_Picture/login.PNG)  




Kullanıcı adı ve şifre ile giriş yaptığınızda doğrulama işleminden sonra uygulamaya girebilirsiniz.


Arayüzdeki modullerin kullanımı için :


![](/Kivy_App_Picture/main_menu.PNG)  




Bu anamenüde sosyal medyada arama , arama motorlarında arama ve Gazetelerde arama arama yapacağınız yere göre seçim yapınız.




Sosyal Medya Menüsü:



![](/Kivy_App_Picture/social_media_menu.PNG) 





Bu menüde Tweepy,Query ile arama , Snscrape ile arama , Facebook arama , Ekşi Arama isteğinize göre seçim yapınız.


#Tweeepy modülü:


![](/Kivy_App_Picture/query_search.PNG)

Tweepy modulu kullanılarak arama gerçekleştirme:
Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili arama kelimesi (keyword) ve istenilen sonuçtan kaç adet talep edileceği (max result) ve hangi
dilde arama yapılacağı girildikten sonra ilgili sonuçların hangi dosya adında kaydedileceği (file name)
belirtip arama (search) butonuna tıklanır.





Tweepy modülünü kullanarak zaman şeridi üzerinde arama yapma:


![](/Kivy_App_Picture/timeline_search.PNG)

Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
İlgili zaman şeridi sonucu için sadece istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin
girilmesi yeterlidir. Daha sonra indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip
arama (search) butonu tıklanır.



Tweepy modülünü kullanarak coğrafik arama yapma:

![](/Kivy_App_Picture/geo_search.PNG)

Tweepy modulunde arama gerçekleştirmek için öncelikle kullanıcının tweepy’e kendi şifreleriyle
bağlanması gerekli bunun için (consumer key,consumer token, access token, access secret )
parametrelerin olması gereklidir. Bu sayede apiye bağlanılır. Api sayesende tweet aramaları
yapılabilinir.
Apinin modulunun coğrafik araması belirtilen cografik kod ait lokasyonda atılmış olan tweetleri
toplar. İlgili cografik kod (geo code) girilmesi ve indirilecek dosyaların hangi isimde kaydedileceği (file
name) belirtilip arama (search) butonu tıklanır.



#Snscrape Modulu:


1-Keyword'e göre Complex arama: 

![](/Kivy_App_Picture/complex_search.PNG)

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

keyworde göre arama:Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi, hangi
dilde(language) arama yapılacağı seçimi yapılıp, akabinde tarih (date) ve aranılacak kelime (keyword)
girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama (search) butonu
tıklanır.


2-Hastage göre Complex arama:



![](/Kivy_App_Picture/complex_search_user.PNG)


Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi, hangi
dilde(language) arama yapılacağı seçimi yapılıp, akabinde tarih (date) ve aranılacak hashtag başında
@ işareti ile girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama
(search) butonu tıklanır.


Simple Search Snscrape: 


![](/Kivy_App_Picture/simple_search.PNG)

Bu modülde ilgili istenilen sonuçtan kaç tane talep edileceği (max result) bilgisinin girilmesi akabinde tarih (date) ve aranılacak kelime (keyword) girilip indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama (search) butonu tıklanır. 

Facebook Modulu : 


![](/Kivy_App_Picture/facebook.PNG)



Facebook üzerinden arama yapmak istediğimizde keyword kısmı doldurulur. Ardından dosyayı hangi isimle kaydetmek istiyorsanız dosya adı verilir ve arama butonuna tıklanır.


Ekşi Modulu:


![](/Kivy_App_Picture/eksi.PNG)



Ekşi sözük üzerinden arama yapmak için kullanılan modüldür.
Arama yapacağımız konu hakkında keyword kısmına kelime girilir. Ardından filename kısmına dosyayı hangi isimle kayıt edeceksek dosya ismi girilip arama butonuna tıklanır.


Search Engine(Arama Motorunda Arama) Sayfası : 

![](/Kivy_App_Picture/search_engine_menu.PNG)

Bu menu hangi arama motorunda arama yapacağımızı seçtiğimiz sayfadır.


Google Search Modulu : 



![](/Kivy_App_Picture/google_search.PNG)



Googlede arama yapmak için tasarlanan bot ile normal kullanıcının Google arama motoruna girip herhangi bir şeyi araması taklit edilerek oluşturuldu. Bu botun tasarımında selenium modülünden faydalanılarak tasarlandı. Selenium botu sayesinde elde edilen linklerden gerekli haber yayınlanma tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) newsplease kullanılarak csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp kullanıcı bilgisayarına indirilip ilgili işlem son bulur. 
Google üzerinden arama yapmamızı sağlar. Arama yapmak için ilk önce arama yapacağımız konuyu keyword kısmına girmemiz gerekir.Link kısmı hangi link üzerinden arama yapmak istiyorsak o link girilir(http://www.nytimes.com gibi).Aramaya başlanacak tarih ise start date kısmıdır burayı doldurduktan sonra hangi tarihe kadar arama yapılmak isteniyorsa end date girilir.Sonra ise arama sonuçlarını hangi dosya adıyla kaydedilmek isteniyorsa filename kısmı doldurulup arama butonuna basılır.

Google Topik Modulu:



![](/Kivy_App_Picture/google_topik.PNG)


Googlede arama yapmak için tasarlanan bot ile normal kullanıcının Google arama motoruna girip herhangi bir şeyi araması taklit edilerek oluşturuldu. Bu botun tasarımında selenium modülünden faydalanılarak tasarlandı. Selenium botu sayesinde elde edilen linklerden gerekli haber yayınlanma tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) newsplease kullanılarak csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp kullanıcı bilgisayarına indirilip ilgili işlem son bulur. 
Söz konusu bot aranılacak kelimeyi (keyword) , hangi konunun aranılacağını (Topic name) , belirtilen başlangıç tarihi ve sonlanma tarihleri (start date & finish date) akabinde indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip arama (search) butonu tıklanır. Bu sayede selenium botu Chrome browserini açıp ilgili parametreleri (keyword, newspapers name, start date,finish date) browserın arama kısmına yazıp, ilgili sonuçları elde eder ve her sayfadaki linkleri alıp csv formatında dosyaya kaydeder. 
Kaydedilmiş dosyadan haber detaylarının çekilmesi için newsplease modulu kullanıldı. Bu module parametre olarak gönderilen adres (url) modülde işlenip çıktı olarak: haber yayınlanma tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) elde edilip. Bu çıktılar csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp kullanıcı bilgisayarına indirilir. 


Bing Modulu:


![](/Kivy_App_Picture/bing.PNG)



Bing Arama motoru üzerinde yapılan aramaların haber linklerinin toplanması için stack veri yapısı kullanılarak ram üzerinde fazla dinamik hafıza (heap) kullanımı engellenip Pythonun BeatifulSoup modulunden yararlanılarak her sayfadaki haber linki toplanılıp .txt formatında muhtelif dosyaya kaydedilip. Daha sonra newsplease modulunden yararlanıp ilgili haber linkine ait içerikler csv formatında dosyaya kaydedilip son aşamada zip halinde sıkıştırılıp kullanıcı bilgisayarına indirilir. 
Oluşturulmuş arayüzde görüldüğü üzere Bing haber araması için aranılacak kelime (keyword) ve hangi haber sitesinde(newspaper name) arama yapılacağı ve son olarak toplanılacak linklerin hangi isimde kaydedileceği (file name) parametreleri doldrulup Bing üzerinde Ara (Search on Bing) tuşuna tıklanılıp ilgili haberlerle alakalı haber linklerinin (urls) elde edilir. Elde edilen haber linkleri ilgili isimde oluşturulan .txt dosyasına kaydedilir. 
Daha sonra txt dosyasından çağrılan haber linkleri newsplease parametre olarak verilir ve çıktı olarak: haber yayınlanma tarihi(published date), haber başlığı (news title) ve haber içeriği (news article) elde edilip. Bu çıktılar csv formatında oluşturulan dosyaya kaydedilip ilgili dosya zip formatında sıkıştırılıp kullanıcı bilgisayarına indirilir. 



Get Newspaper on  Google Modulu:




![](/Kivy_App_Picture/news_on_google.PNG)


Haber sitesinin linkini girip başlangıç tarihi ve bitiş tarihi olmak üzere değerleri girdiğimzde ve dosyayı hangi adla kaydedeceğimizi karar verip dosya adı oluşturup arama yapabileceğimiz bir moduldur.


News Sayfası : 


![](/Kivy_App_Picture/news_menu.PNG)


Bu sayfada kategori yada kelimeye göre arama seçeneği sunan sayfadır



News Date Search Modulu : 


![](/Kivy_App_Picture/news_date_search.PNG)


Hergazetenin yapısı farklı olduğundan ve farklı dillerde farklı şekiller kodlandığından çoğu ulusal haber kaynaklarının içerikleri newsplease gibi scraperlar tarafından eksik olarak işlenip eksik verilerin oluşmasına neden olduğundan . Belirlediğimiz çeşitli ulusal gazetelerin yapıları tek tek incelenip kimisini gerek Python BeatifulSoup gereksede selenium’dan faydalanarak kendi yapılarına uygun kodlar ile ayrı ayrı modüller geliştirdik.Bu sayede Bu haber sitelerinin içeriklerinden verimli bir şekilde faydalanmayı başardık Bu gazetelerden bazıları: banker,bgnes,cumhuriyet,dailymail,dailysabah,dnevnik,duvar,dwnews,ensonhaber,evrensel,guardian,haberler,hürriyet, independent,memurlar,milli,odatv4,sabah,sega,sozcu,trud,turkiye…vb 
Başlangıç tarihi (start date) , sonlanma tarihi (finish date), kategory (bu parametre gazeteden gazeteye göre değişmekle beraber şöyle ki: girilen kategory aranılan gazetede mevcutsa spesifik olarak o kategoride haber araması yapar aksi taktirde tüm sonuçları döndürür.), gazete ismi (newspaper name) ve akabinde indirilecek dosyaların hangi isimde kaydedileceği (file name) belirtilip tarihe göre arama (search by date) butonu tıklanır. Bu sayede gönderilen parametreler yazmış olduğumuz modul ile hangi gazete ismi ile arama yapılmış ise o sınıfı bulup o sınıfa ait başlangıç değer atamalarını (initialize) atayıp sınıf içerisinde tarih oluşturma (Date Creator) fonksiyonu ile ilgili gazete url ine uygun formattaki tarihi oluşturup bu sayede haber linki elde etme (Get Link) fonksiyonunu çağırıp ilgili tarihteki gazete linkleri elde ediliyor. Toplanılan linklerden haber içeriklerinin alınması için ilgili fonksiyon olan (Creator) ile elde edilip sözkonusu sonuçlar .txt formatında dosyaya kaydedilip son aşamada da bu dosya zip formatında sıkıştırılıp kullanıcı bilgisayarına indiriliyor. 



News Search Modulu : 



![](/Kivy_App_Picture/news_search.PNG)

Haber sitelerinde kelimeye göre arama yapmamızı sağlayan modüldür. Aranmak istenilen kelimeyi keyword kısmı doldurulduktan sonra hangi gazeteden arama yapılacaksa newspaper name kısmı doldurulur.Arama yapılabilen gazetelerden bazıları:
banker,bgnes,cumhuriyet,dailymail,dailysabah,dnevnik,duvar,dwnews,ensonhaber,evrensel,guardian,haberler,hürriyet, independent,memurlar,milli,odatv4,sabah,sega,sozcu,trud,turkiye…vb 
Gazete adı girildikten sonra sonuçları hangi dosya adıyla kaydetmek istiyorsak filename kısmı girilir ve arama butonuna basılır. 



iyi çalışmalar ....
