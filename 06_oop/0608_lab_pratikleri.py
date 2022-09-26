

class Ders:
    derslerinToplamKredisi = 0
    def __init__(self, dKodu, ad, donem, kredisi) -> None:
        self.dKodu = dKodu
        self.ad = ad
        self.donem = donem
        self.kredisi = kredisi
        Ders.derslerinToplamKredisi += self.kredisi

    def __str__(self) -> str:
        return f"{self.dKodu}\t{self.ad}\t{self.donem}\t{self.kredisi}\t"

d1 = Ders(101, "mat.", 1, 5)
d2 = Ders(101, "fizik", 2, 4)
d3 = Ders(101, "prog.", 2, 6)
d4 = Ders(101, "fels.", 1, 2)
# print(d1)
# print(d2)
# print(d3)
dersler = [d1, d2, d3, d4]
for i in dersler:
    print(i)
print(f"\t\t\t{Ders.derslerinToplamKredisi}")