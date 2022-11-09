from zope.interface import Interface, implementer, Attribute, invariant
from zope.component import provideUtility
from zope.component.factory import Factory
def walidacja(pr):
    if not (pr.imie and pr.nazw):
        print("Nie podano imienia lub nazwiska pracownika")
class IPracownik(Interface):
    imie = Attribute("imię pracownika")
    nazw = Attribute("nazwisko pracownika")
    staz = Attribute("staż pracownika")
    wynzas = Attribute("wynagrodzenie zasadnicze pracownika")
    def pensja(): """pensja brutto"""
    def premia(procent): """dodanie premii"""
    invariant(walidacja)

@implementer(IPracownik)
class Pracownik(object):
    imie=""
    nazw=""
    staz=0 
    wynzas = 2600 
    def pensja(self):
        if self.staz<=20:
            return round(self.wynzas*(1+self.staz/100),2)
        else:
            return round(self.wynzas*1.2,2)
    def premia(self,procent):
        return round(self.pensja()*(1+procent/100),2)

fac=Factory(Pracownik,"Fabryka pracowników","pr")
#tworzymy fabrykę funkcji
fac2=Factory(lambda x:print(x),"Fabryka napisów","wypisz")
pr1=fac("Adam","Nowak",10,3000) #uruchomienie fabryki klas
dane1=pr1.imie+" "+pr1.nazwisko+" "+str(pr1.pensja())
y=fac2(dane1) #uruchomienie fabryki funkcji
pr2=fac("Marek","Nowicki")
dane2=pr2.imie+" "+pr2.nazwisko+" "+str(pr2.premia(30))
y=fac2(dane2)
