"""importy"""
from wyk12_komponenty import *
from zope.component import getUtility
"""czynnosci przygotowujące"""
f = open("zamowienoa/zamowienia.txt", "w", encoding="utf-8")
f.write("Imię i nazwisko\t\t"+"Pow\t"+"L.pom\t"+"G\t"+"Lokalizacja"+"\t"*4+"Cena\n")
x=getUtility(IDom)
x2 = IDom2(x)
#zamówienie A.Nowak
x.klient("Anna Nowak")
x.wielkosc(120)
x.liczbapomieszczen(6)
x.garaz(1)
x2.ogrodek(1) #wywołanie nowej metody
x.polozenie("Warszawa","Bemowo")
x2.zapis(f) #wywołanie przebudowanej metody


#zamówienie J.Kowalski
x.klient("Jarosław Kowalski")
x.wielkosc(250)
x.liczbapomieszczen(7)
x.garaz(0)
x.polozenie("Wrocław","Psie Pole")
x.zapis(f)

#zamówienie A.Duda
x.klient("Aneta Duda")
x.wielkosc(60)
x.liczbapomieszczen(5)
x.garaz(1)
x.polozenie("Poznań","Garbary")
x.zapis(f)
f.close()