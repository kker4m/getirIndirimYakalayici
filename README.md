#Getir indirim yakalayici script 

Python scripti önce klasörde bir data oluşturuyor ve sonrasında giriş yapılması takdirinde tekrar şifre sorma işlemini ortadan kaldırıyor. Giriş sonrasında kampanyalar sayfasından indirim takibi yapılıyor ve indirim bulunması takdirinde belli bir frekansta ses çalınıyor. 30 Dakika içerisinde bir daha bulunan indirim yazılmıyor ve her beş dakika da bir yeni indirimler için sayfa yenileniyor.  

Gerekli teknolojiler : 
>BeautifulSoup
selenium
time
tqdm
winsound

### Çalıştırmadan önce

Python3'u yükledikten sonra terminali yönetici olarak çalıştırın ve indirdiğiniz klasörün içerisinde kodu çalıştırın ; 
> pip3 install -r requirements.txt
