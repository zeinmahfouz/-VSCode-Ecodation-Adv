
#region ornek_1
"""
n1, n2 = int(input("lütfen 1. snv notunu giriniz \t : ")), int(input("lütfen 2. snv notunu giriniz \t : "))
ort = (n1+n2)/2
if ort>=85:
    print(f"yıl sonu notunuz {ort}, başarı durumu PEKİYİ")
elif ort>=70:
    print(f"yıl sonu notunuz {ort}, başarı durumu İYİ")
elif ort>=55:
    print(f"yıl sonu notunuz {ort}, başarı durumu ORTA")
elif ort>=45:
    print(f"yıl sonu notunuz {ort}, başarı durumu GEÇER")
else:
    print(f"yıl sonu notunuz {ort}, başarı durumu GEÇEMEZ")
"""
#endregion

#region ornek_2

s1 = int(input("l. s1. giriniz : "))
s2 = int(input("l. s2. giriniz : "))
s3 = int(input("l. s3. giriniz : "))
if s1<s2:
    s1, s2 = s2, s1
if s1<s3:
    s1, s3 = s3, s1
if s2<s3:
    s2, s3 = s3, s2
print(f"{s1}>{s2}>{s3}")

#endregion

#region ornek_3

a = int(input("lütfen a kenarını giriniz \t : "))
b = int(input("lütfen b kenarını giriniz \t : "))
if a==b:
    print(f"karenin alanı {a*b}")
else:
    print(f"dikdörtgenin alanı {a*b}")

#endregion



kisaKenar = int(input("lütfen kısa kenarını giriniz \t : "))
uzunKenar = int(input("lütfen uzun kenarını giriniz \t : "))
if kisaKenar>uzunKenar:
    print("kısa kenar uzun girilemez")
else:
    print(f"dörtgenin çevresi {2*(kisaKenar + uzunKenar)}")
#endregion
#region ornek_5
a = int(input("lütfen 1. s giriniz \t : "))
b = int(input("lütfen 2. s giriniz \t : "))
if a%b==0:
    print(f"{a} sayısı {b} sayısına tam bölünür")
else:
    print(f"{a} sayısı {b} sayısına tam bölünemez")

#endregion


