import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
import os
import time
from tqdm import tqdm
from selenium.webdriver.common.by import By
import winsound

duration = 1000  # milliseconds
freq = 440  # Hz


user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/99.0.4844.51 Safari/537.36"
language="tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"

current_path=os.path.dirname(os.path.abspath(__file__))
current_path=current_path.replace("\\","\\\\")

chromeOptions= webdriver.ChromeOptions()
#chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("user-data-dir="+str(current_path)+"\\chromeprofile")

header={
    "accept-language": "tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'
}

chrome=webdriver.Chrome(executable_path=str(current_path)+"\\chromedriver.exe",options=chromeOptions)
link=("https://getir.com/kampanyalar/")


data=["Size özel, 30 TL ve üzeri siparişinize 20 TL indirim uygulanır.","Size özel, 30 TL ve üzeri siparişinize 20 TL indirim uygulanır.",
      "Size özel, 35 TL ve üzeri siparişinize 30 TL indirim uygulanır.","Size özel, 120 TL ve üzeri siparişinize 20 TL indirim uygulanır.",
      "Size özel, 230 TL ve üzeri siparişinize 30 TL indirim uygulanır."
      ]
checkbox=[]

def indirimreplace(text):
    text = text.split()
    return str(text[2]) + " " + str(text[3]) + "'ye" + " " + str(text[-4]) + " " + str(text[-3]) + " indirim"+" bulundu !"



chrome.get(link)

if (chrome.current_url)=="https://getir.com/":
    print("Daha önce giriş yapılmamış, lütfen giriş yapınız.")
    telefonnumarasi =(input("Telefon numaranızı girin : +90 "))
    telefonnumarakutu=chrome.find_element(By.XPATH,'//*[@id="__next"]/div[3]/main/section/div/section[1]/div/div/form/div[1]/div/div[2]/div/div/input')
    telefonnumarakutu.click()
    telefonnumarakutu.send_keys(telefonnumarasi)
    chrome.find_element(By.XPATH,'/html/body/div[1]/div[3]/main/section/div/section[1]/div/div/form/div[2]/div/button').click()

    with tqdm(total=(200),unit=" saniye",desc="Telefonunuza gelecek olan doğrulama kodunu bekleyiniz.. ") as bar:
        for i in range(10):
            time.sleep(1)
            bar.update(20)

    dogrulamakodu=input("Lütfen doğrulama kodunu giriniz : ")

    dogrulamakutu=chrome.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/input')
    dogrulamakutu.click()
    dogrulamakutu.send_keys(dogrulamakodu)
    chrome.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div[2]/div[2]/form/div[2]/div/button').click()
    time.sleep(3)

    print("Başarıyla giriş yapıldı")
    chrome.get("https://getir.com/kampanyalar/")
else:
    print("Zaten giriş yapılmış, hoşgeldiniz.")



soup=chrome.page_source
r=BeautifulSoup(soup,"lxml")
basliklar=r.find_all('span',attrs={'class':'style__Text-sc-__sc-1nwjacj-0 bVIbWZ style__Description-sc-18gp6r5-1 hoCfWW'})
while True:
    for _ in range(6):
        count=0
        chrome.refresh()
        soup = chrome.page_source
        r = BeautifulSoup(soup, "lxml")
        basliklar = r.find_all('span', attrs={'class': 'style__Text-sc-__sc-1nwjacj-0 bVIbWZ style__Description-sc-18gp6r5-1 hoCfWW'})
        for baslik in basliklar:
            indirim=baslik.text
            if data.__contains__(indirim)==True:
                if checkbox.__contains__(indirimreplace(indirim))==True:
                    continue
                else:
                    count+=1
                    checkbox.append(indirimreplace(indirim))
                    print(indirimreplace(indirim))
                    winsound.Beep(freq, duration)
        if count==0:
            print("\nYeni indirim bulunamadı.\n")
        with tqdm(total=(300),unit=" second",desc="Sonra ki indirim kontrolüne kalan süre  ") as bar:
            for i in range(300):
                time.sleep(1)
                bar.update(1)
    checkbox=[]

