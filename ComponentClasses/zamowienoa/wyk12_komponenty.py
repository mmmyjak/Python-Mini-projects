from zope.interface import implementer
from zope.component import provideUtility, adapter, provideAdapter
from wyk12_interfejsy import *

@implementer(IDom)
class Dom(object):
    def klient(self, a):
        self.k = a
    def wielkosc(self, a):
        self.w = a
    def liczbapomieszczen(self, a):
        self.l = a
    def garaz(self, wybor):
        self.wybor = wybor
        if wybor == 1:
            return 20000
        else:
            return 0
    def polozenie(self, miasto, dzielnica):
        self.m = miasto
        self.d = dzielnica
    def cena(self):
        return self.w*5000+self.l*2000+self.garaz(self.wybor)
    def zapis(self, f):
        f.write(str(self.k) + (20-len(self.k))* " ")
        f.write(str(self.w)+(4-len(str(self.w)))* " ")
        f.write(" " + str(self.l)+ (6 - len(str(self.l)))* " ")
        f.write(str(self.wybor)+ (4-len(str(self.wybor)))* " ")
        f.write(str(self.m)+","+str(self.d)+(22-len(self.m)-len(self.d))* " ")
        f.write(str(self.cena())+ " PLN\n")
provideUtility(Dom())

@implementer(IDom2)
@adapter(IDom)
class Dom2(object):
    def __init__(self, adaptee):
        self.adaptee=adaptee
    def ogrodek(self, wybor):
        self.wybor = wybor
        if wybor==1:
            return 5000
        else:
            return 0
    def cena(self):
        c = self.adaptee.cena()+self.ogrodek(self.wybor)
        if self.adaptee.m == "Warszawa":
            return int(1.2*c)
        else:
            return c
    def zapis(self,f): #przebudowany zapis
        self.adaptee.zapis(f)
        if self.wybor==1 and self.adaptee.m=="Warszawa":
            print("halos")
            f.write("Klient wybrał dodatkowo ogródek oraz Warszawę. ")
            f.write("Cena zwiększona wynosi teraz:"\
            +str(self.cena())+"PLN\n")
        elif self.wybor==1:
            f.write("Klient wybrał dodatkowo ogródek. ")
            f.write("Cena zwiększona wynosi teraz:"\
            +str(self.cena())+"PLN\n")
provideAdapter(Dom2)
