import datetime
import json
import requests


urlCustomers = "https://northwind.netcore.io/customers.json"

rCustomers = requests.get(url = urlCustomers)


if not rCustomers.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rCustomers.status_code, rCustomers.text))


#print(rCustomers.text)


jsonCustomers = json.dumps(urlCustomers)

urlOrders = "https://northwind.netcore.io/query/orders.json"

rOrders = requests.get(url = urlOrders)


if not rOrders.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rOrders.status_code, rOrders.text))


#print(rOrders.text)


jsonOrders = json.dumps(urlOrders)


mainMapApiUrl= "http://www.mapquestapi.com/staticmap/v5/map?key=0mdie7oKF7peAqc2RFIvlICvVtRSVPkm&type=map&size=225,160&locations=41.076602,29.052495|marker-sm-50318A-2&scalebar=true&zoom=5&rand=1593913467"
                

mapApiKey="0mdie7oKF7peAqc2RFIvlICvVtRSVPkm"



def metinKontrol(metin):
    if len(metin)>15:
        return f"{metin}"
    else:
        return f"{metinKontrol}"


def musteriListele():
    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

    for i in jsonCustomers["<Gerekli Key İle Değiştir>"]:
        print(f"Gerekli Output İçin Formatla")

    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")


def musteriAra(musteriId):
    for i in jsonCustomers["musteriId"]:
        if i['id']==musteriId:
            print(f"{musteriId} ID'li müşteri bulundu. Detay Listesi")
            print("==========================")
            print(f"{musteriListele}")          
            break
    else:
        print(f"{musteriId} ID'li müşteri bulunamadı")


def siparisListele():  
    print("Sipariş Listesi")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CustomerId     |OrderDate                      |ShipAddress            |ShipCity               |ShipCountry            |")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    for i in jsonOrders:
        epochSaniye = datetime(1998,1,1)
        gunumuzZamani = datetime
        print(f"Gerekli Output İçin Formatla")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")


def siparisAra(siparisId):
    for i in jsonOrders["<Gerekli Key İle Değiştir>"]:
        if i['order']['id']==siparisId:
            epochSaniye =  datetime(1970, 1, 1)
            gunumuzZamani = datetime 
            print(f"{siparisId} ID'li sipariş bulundu. Detay Listesi")
            print("==========================")
            print(f"{musteriListele}") 
            nereye = "https://www.mapquestapi.com/geocoding/v1/address?key=0mdie7oKF7peAqc2RFIvlICvVtRSVPkm&location=istanbul"          
            cevap = input(f"Kargo Rotasını {nereye.upper()} Şehri İçin Görmek İster misiniz? [e/E] :")
            if cevap.lower()=="e":
                while True:                    
                    print(f"Varış Noktası {nereye} için Rota Hesaplanacak")
                    nereden = input("Nereden Çıkacak: ")
                    
                    break
            break
    else:
        print(f"{siparisId} ID'li sipariş bulunamadı")


while True:
    for i in range(5):
        print()
    secim = int(input("""
    Seçiminiz:
    [1]     → MÜŞTERİ LİSTELE
    [2]     → MÜŞTERİ ARA <MÜŞTERİ ID'E GÖRE>
    [3]     → SİPARİŞ LİSTELE
    [4]     → SİPARİŞ ARA <SİPARİŞ ID'E GÖRE>
    [5]     → ÇIK
    """))
    if secim==1:
        pass
    elif secim==2:
        pass
    elif secim==3:
        pass
    elif secim==4:
        pass
    elif secim==5:
        pass
    else:
        pass