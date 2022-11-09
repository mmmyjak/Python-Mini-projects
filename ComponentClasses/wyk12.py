from sys import exit
from math import pi
from zope.interface import *
from zope.component import provideUtility, provideAdapter, adapter, getUtility

# klasa interfejsu
class ITrojkat(Interface):
    def obwod():
        """oblicza obwod trojkata"""
    def pole():
        """oblicza pole"""

# klasa komponentu

@implementer(ITrojkat)
class Trojkat(object):
    def __init__(self,a,b,c):
        if a>0 and b>0 and c>0 and a<b+c and a>abs(b-c):
            print("Trojkąt o bokach",a,b,c,"utworzono")
            self.a,self.b,self.c=a,b,c
        else:
            exit("Nie ma takiego trójkąta!")
    def obwod(self):
        return self.a+self.b+self.c
    def pole(self):
        p = self.obwod()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

# main

provideUtility(Trojkat(3,4,5), ITrojkat, "tr1")
t1 = getUtility(ITrojkat, "tr1")
print("Pole trojkata:", t1.pole())
print("Obowd trojkata:", t1.obwod())

# klasa nowego interfejsu
class ITrojkat2(Interface):
    def pole_opisanego():
        """oblicza pole koła opisanego"""
    def pole_wpisanego():
        """"oblicza pole koła wpisanego"""

@implementer(ITrojkat2)
@adapter(ITrojkat)
class Trojkat2(object):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    def pole_opisanego(self):
        R = self.adaptee.a*self.adaptee.b*self.adaptee.c/(4*self.adaptee.pole())
        return pi*R**2
    def pole_wpisanego(self):
        r=2*self.adaptee.pole()/self.adaptee.obwod()
        return pi*r**2

provideAdapter(Trojkat2)
t2 = ITrojkat2(t1)
print("Pole koła opisanego:",t2.pole_opisanego())
print("Pole koła wpisanego:",t2.pole_wpisanego())