from callDrivers import *

class Getir():
    def __init__(self):
        self.driver = callUcDriver(True,None)
        print("Getir indirim yakalayici baslatiliyor.")
        print("https://github.com/linuxkerem")
        self.duration = 1000  # milliseconds
        self.freq = 440  # Hz
        self.sleepTime = 300
        self.data=[
            "Size özel, 30 TL ve üzeri siparişinize 20 TL indirim uygulanır.",
            "Size özel, 35 TL ve üzeri siparişinize 30 TL indirim uygulanır.",
            "Size özel, 120 TL ve üzeri siparişinize 20 TL indirim uygulanır.",
            "Size özel, 230 TL ve üzeri siparişinize 30 TL indirim uygulanır.",
            "Size özel, 40 TL ve üzeri siparişinize 30 TL indirim uygulanır.",
            "Size özel, 60 TL ve üzeri siparişinize 40 TL indirim uygulanır."
        ]

    def girisYap(self):
        self.driver.get("https://getir.com/kampanyalar/")

        time.sleep(0.4)

        if self.driver.current_url != "https://getir.com/kategoriler/":
            print("Daha once giris yapilmamis, giris yapiniz: ")

            telNo = (input("Telefon numaranızı girin : +90 "))

            telefonElement = self.driver.find_element(By.XPATH,'//input[@type="tel"][@name="gsm"]')

            telefonElement.click()

            time.sleep(0.2)

            telefonElement.send_keys(telNo)

            self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()

            dogrulamaKodu = input("Lütfen telefonunuza gelen doğrulama kodunu giriniz : ")

            dogrulamaElement = self.driver.find_element(By.XPATH,'//input[@type="text"]')

            dogrulamaElement.click()
            dogrulamaElement.send_keys(dogrulamaKodu)

            self.driver.find_elements(By.XPATH, '//button[@type="submit"]')[-1].click()

            time.sleep(3)

            self.driver.find_element(By.XPATH,'//a[@href="/kampanyalar/"]').click()

            print("Başarıyla giriş yapıldı")

        return True

    def indirimKontrol(self):

        time.sleep(10)

        print("Indirim kontrolu baslatiliyor.")

        while True:
            titles = self.driver.find_elements(By.XPATH, '//div[@data-testid="card"]')[1:]
            founded = []
            for title in titles:
                title = title.find_element(By.TAG_NAME,'span').get_attribute('innerHTML')
                if not founded.__contains__(title):
                    for d in self.data:
                        y = d.replace(',','')
                        if str(title).__contains__(d) or str(title) == d or str(title).__contains__(y) or str(title) == y:
                            founded.append(title)

            if len(founded) > 0:
                for indirim in founded:
                    print("Bulunan indirim : ",indirim)
                    winsound.Beep(self.freq, self.duration)
            else:
                print("Herhangi bir indirim bulunamadi")
            print(f"{self.sleepTime} Saniye sonra tekrar indirim aranacak.")
            time.sleep(300)
            self.driver.refresh()
            time.sleep(10)



if __name__=="__main__":
    getir = Getir()
    getir.girisYap()
    getir.indirimKontrol()