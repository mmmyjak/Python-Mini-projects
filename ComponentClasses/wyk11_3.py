from zope.interface import Interface, implementer
from zope.component import provideUtility, getUtility

class IForemny(Interface):
    def set(a):
        """Ustawia atrybut boku"""
    def get():
        """Pobiera bok""" 
    def pole(): """Oblicza pole"""
    def obwod(): """Oblicza obwód"""

@implementer(IForemny)
class Kwadrat(object):
    def set(self,a):
        self.a__=a
    def get(self):
        return self.a__
    def pole(self):
        return self.a__**2
    def obwod(self):
        return 4*self.a__

@implementer(IForemny)
class Trojkat(object):
    def set(self,a):
        self.a__=a
    def get(self):
        return self.a__
    def pole(self):
        return (self.a__**2)*(3**(1/2))/4
    def obwod(self):
        return 3*self.a__

provideUtility(Kwadrat(), IForemny, "kw")
provideUtility(Trojkat(), IForemny, "tr")
kw = getUtility(IForemny, "kw")
a = float(input("Podaj bok kwadratu: "))
kw.set(a)
print("Pole kwadratu:", kw.pole())
print("Obwód kwadratu:", kw.obwod())

tr = getUtility(IForemny, "tr")
a = float(input("Podaj bok trójkąta: "))
tr.set(a)
print("Pole trójkąta:", tr.pole())
print("Obwód trójkąta:", tr.obwod())
