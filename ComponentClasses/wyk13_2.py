from zope.interface import Interface, Attribute, invariant, implementer
from zope.component import provideUtility, getUtility
from math import sin,pi
from sys import exit
def walidacjabok(r):
    if r.a<=0 or r.b<=0:
        print("Przynajmniej jeden z boków jest niepoprawny")
    else:
        print("Boki równoległoboku poprawne")
def walidacjakat(r):
    if r.k<=0 or r.k>=180:
        print("Zły kąt!")
    else:
        print("Kąt między bokami poprawny")

class IRownoleglobok(Interface):
    a=Attribute("długość pierwszego boku")
    b=Attribute("długość drugiego boku")
    k=Attribute("kąt w stopniach")
    def pole():
        """oblicza pole"""
    def obwod():
        """oblicza obwod"""
    def h1():
        """oblicza pierwszą wysokość"""
    def h2():
        """oblicza drugą wysokość"""
    invariant(walidacjabok)
    invariant(walidacjakat)

@implementer(IRownoleglobok)
class Rownoleglobok(object):
    try:
        a=float(input("Podaj pierwszy bok:"))
        b=float(input("Podaj drugi bok:"))
        k=float(input("Podaj kąt:"))
    except:
        print("Błędny atrybut!")
        exit()
    def pole(self):
        print("to jest pole")
        #return round(self.a*self.b*sin(self.k*pi/180),2)
    def obwod(self):
        return round(2*self.a+2*self.b,2)
    def h1(self):
        return round(self.pole()/self.a,2)
    def h2(self):
        return round(self.pole()/self.b,2)

provideUtility(Rownoleglobok())
x=getUtility(IRownoleglobok)
IRownoleglobok.validateInvariants(x)
x.pole()