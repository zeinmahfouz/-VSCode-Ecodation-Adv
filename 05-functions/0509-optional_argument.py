

a= 2
b = 3
c = 10
def topla(a, b, c=5):
    print(f"{a} + {b} + {c} = {a+b+c}")


topla(a=2, b=3)



def topla(a=2):
    print(f"{a} + {b} + {c} = {a+b+c}")


topla(b=3, c= 10)



# region ornek_2


def topla(a, b, c=5):
    print(f"{a} + {b} + {c} = {a+b+c}")


topla(a= 2, b=3, c= 10)

# endregion