# region ornek_1
"""
kg = float(input("kilonuz: "))
mt = float(input("boyunuz [mt] : "))
vki =round(kg/mt**2, 2)
if vki<18.49:
    print("ideal kilonun altı")
elif vki>18.5 and vki<24.99:
    print("ideal kilo")
elif vki>25 and vki<29.99:
    print("ideal kilo üzeri")
elif vki>30:
    print("ideal kilonun çok üzeri")
"""
# endregion


# region ornek_2

yg = float(input("yıllık geliriniz: "))
if yg<22000:
    ygv = yg * 0.15
elif yg>22000 and yg<49000:
    ygv = yg * 0.20
elif yg>49000 and yg<180000:
    ygv = yg * 0.27
elif yg>180000 and yg<600000:
    ygv = yg * 0.35
elif yg>600000:
    ygv = yg * 0.40
print(f"yıllık gelir verginiz {ygv}")

# endregion
