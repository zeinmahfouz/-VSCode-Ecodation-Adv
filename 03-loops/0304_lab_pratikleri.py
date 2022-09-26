# region ornek_1
"""


metin = input("Ekrana Yazılacak Metni Giriniz: ")
i = 1
while i<=5:
    print(metin)
    i += 1
"""
# endregion

# region ornek_2
"""


i = 0
while i<10:
    print(" * ", end= "")
    i += 1
"""
# endregion

# region ornek_3
"""



i = 0
while i<10:
    if i%2==0:
        print(" * ", end= "")
    else:
        print(" $ ", end= "")
    i += 1
"""
# endregion

# region ornek_4
"""

i, j = 0, 0
while i<10:
    while j<10:
        if i%2 ==0:
            print(" * ", end= "")
        else:
            print(" $ ", end= "")
        j += 1
    i +=1
    j = 0
    print()
"""
# endregion

# region ornek_5
"""

i = 1
s = 0
while i < 100:
    if s % 10 == 0:
        print()
    print(i, end=" ")
    s += 1
    i += 2
"""
# endregion

# region ornek_6


"""

i = 1
toplam = 0
while i < 100:
    toplam += i
    i += 2
print(f"[1-99] arası tek sayıların toplamı → {toplam}")
"""
# endregion

# region ornek_7
"""

i = 1
sayi = int(input("Lütfen Sayı Giriniz: "))
while i <= 10:
    print(f"{sayi } x {i} = {sayi*i}")
    i += 1
"""
# endregion

# region ornek_8
"""

2→  sonsuz döngü içinde kelimeyi bulmaya çalışırken, bulduğu anda döngüden çıkacak
gizliKelime = input("açıl .... açıl!!! lütfen boşluğu doldurun: \t")
while gizliKelime != "susam":
    print("hahahahahah ne oldu bilemedin ama :-)")
    gizliKelime = input("açıl .... açıl!!! lütfen boşluğu doldurun: \t")
print("başardın!!!")
"""
# endregion

# region ornek_9
"""

adet, toplam = 0, 0
sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
while sayi:
    toplam += sayi
    adet += 1
    sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
print(f"girdiğiniz sayıların ortalaması → {toplam/adet}")
"""
# endregion

# region ornek_10
"""

rakam = int(input("lütfen [1-9] arası rakam giriniz: "))
while i<6:
    print(f"{rakam * i}", end=" ")
    i += 1
"""
# endregion

# region ornek_11
"""

i = 1
sonuc = 1
while i<6:
    sonuc *= i
    print(f"{i} \t {sonuc}")
    i += 1
"""
# endregion

# region ornek_12_algoritmalar_kitabından
"""

i = 100
while i<1000:
    kalan = i % 10
    birler = kalan // 1
    kalan = i % 100
    onlar = kalan // 10
    kalan = i % 1000
    yuzler = kalan //100
    haneleriToplami = birler + onlar + yuzler
    if haneleriToplami == 3:
        print(f"{i} (3 haneli, haneleri toplamı 3)")
    i += 1
"""
# endregion

# region ornek_13
"""
import random   
uretilenSayi = random.randint(1, 99)   # [1-99] arası sayı üretir
print(uretilenSayi)
i = 0
enKucukFark=99999999999
while i<3:
    tahmin = int(input("lütfen [1-99] arası tahmininizi giriniz: \t"))    
    fark = uretilenSayi - tahmin
    if fark<0:
        fark *= -1
    if fark<enKucukFark:
        enKucukFark = fark
        enYakinTahmin = tahmin
    i += 1
print(enYakinTahmin)
"""



# endregion

# region ornek_14
"""

i, j = 0, 10
while i<10:
    while j>0:
        print(" * ", end= "")
        j -= 1
    i += 1
    j = 10 -i
    print()

i, j = 0, 0
while i < 10:
    while j < i:
        print(" * ", end="")
        j += 1
    i += 1
    j = 0
    print()
"""
# endregion

# region ornek_15
"""


i, j = 0, 4
n = 0
while i<4:
    while n>0:
        print("   ", end= "")
        n -=1
    while j>0:
        print(" * ", end="")
        j -=1
    i +=1
    n = i
    j = 4-i
    print()
i, j, n = 0, 0, 0
while i<4:
    while j<4:
        if n<i:
            print("   ", end="")
        else:
            print(" * ", end="")
        j +=1
        n +=1
    i +=1
    j = 0
    n = 0
    print()
"""
# endregion

# region ornek_16

i, j, n = 0, 0, 5
while i < 5:
    while j <=5:
        if n>0:
            print(".", end="")
        else:
            print(" *", end="")     
        j += 1
        n -=1
    i += 1
    n = 5- i
    j = 0
    print()
    
    
# endregion