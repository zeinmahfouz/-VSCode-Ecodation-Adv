# region ornek_1
"""
delta örneği
a = 1
b = 4
c = 2
delta = b**2 - 4*a*c
print("delta değeri " , delta)
"""
# endregion


# region ornek_2
"""
ortalama
s1 = 2
s2 = 4
ort = (s1 + s2) / 2
print("oralama değeri ", ort)
"""
# endregion


# region ornek_3
"""
saat bilgisini saniyeye dönüştürsün
saat = 2
saniye = 3600
print("Saat: ", saat)
print("Ekrandaki saat biriminin saniye karşılığı →", saat*saniye, " sn.")
"""
# endregion

# ipucu → formatter shift + alt + f

# region ornek_4
"""
sayi = 562
kalan = sayi % 10
birler = kalan // 1
kalan = sayi % 100
onlar = kalan // 10
kalan = sayi % 1000
yuzler = kalan //100
toplamDegeri = birler + onlar + yuzler
print(yuzler, onlar, birler)
print(sayi, " sayısının basamakları toplamı " , toplamDegeri)
"""
# endregion




# ödev →
"""""
boy =165 

print ("boyum", boy ,"santim")

"""""

# ödev →
"""
Lütfen Günlük Ortalama Adım Sayınızı Giriniz; 5000
Harcanan Kalori
Günlük; ...
Haftalık; ...
Aylık; ... 
"""
adimsyaisi = int(input("adım sayısı girinz:\t "))
print ("günlük ", adimsyaisi*0.05, "cal.")
print("haftalık",adimsyaisi*0.05*7,"cai.")
print("aylık",adimsyaisi*0.05*30,"cal.")

