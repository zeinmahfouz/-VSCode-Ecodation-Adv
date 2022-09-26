# region args_giris


def topla(a, b, c):
    print(f"{a} + {b} + {c} = {a+b+c}")

topla(a=2, b=3)

# endregion



# region degisken_sayida_parametre_gonderimi


def topla(*args):
    print(type(args))
    topla = 0
    for i in args:
        topla += i
    print(topla)

topla(2,3,5)
topla(2,3,5,5)


# endregion

# region ornek_1


# sum yöntemi liste elemanlarını kolayca toplayacaktır
def topla(*args):
    print(f"liste elemanları toplamı → {sum(args)}")

topla(2, 3, 5)
topla(2, 3)
topla(2, 3, 6, 8, 10)

# endregion

# region ornek_2

def ortalama(*args):   
    print(f"liste elemanlarının ortalaması → {sum(args)/len(args)} ")


ortalama (6, 8, 10, 12, 20)

# endregion

# region ornek_3

def tekilListe(*args):
    yeniListe = []
    for i in args:
        if i not in yeniListe:
            yeniListe.append(i)
    print(yeniListe)



tekilListe(3, 5, 5, 10, 12, 3, 13)

# endregion




def favDerslerim(*args):
    for i in args:
        print(i)

favDerslerim("matematik","biyoloji", "fizik", "kimya")



"""
def hobilerim(*args, ad):
    print(f"{ad} öğretmeniminin hobileri")
    for i in args:
        print(i, end= " ")


hobilerim("basketbol", "koşu", "gezi", "müzik", ad = "Aziz")
"""