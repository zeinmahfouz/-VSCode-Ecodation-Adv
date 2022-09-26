
def hastaKart(ad, soyad):
    print(f"sağlıklı günler dileriz {ad} {soyad}")


hastaKart(soyad = "Kemal", ad = "Ali")


# region ornek



def urunSatistaMi(urunKodu, urunAdi, fiyat, satistaMi):
    if satistaMi:
        print(f"ürün kodu {urunKodu} olan {urunAdi} isimli ürünümüz {fiyat} TL. fiyat ile satıştadır")
    else:
        print(f"ürün kodu {urunKodu} olan {urunAdi} isimli ürünümüz satışta değildir")


urunSatistaMi(satistaMi=True,fiyat=80.75, urunAdi="Filtre Kahve", urunKodu="v60")
