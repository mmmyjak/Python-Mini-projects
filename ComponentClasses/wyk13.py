from zope.interface import Interface, implementer, Attribute, invariant
from zope.component import getUtility, provideUtility

def walidacja(kw):
    if kw.a <= 0:
        print("Bok kwadratu ma być dodatni, obiekt nie zostanie utworzony")
    else:
        print("Utworzono kwadrat o boku", kw.a)

class IKwadrat(Interface):
    a = Attribute("długość boku kwadratu")
    def pole():
        """oblicza pole"""
    def obwod():
        """oblicza obwod"""
    invariant(walidacja)

@implementer(IKwadrat)
class Kwadrat(object):
    a=35 #ustalenie atrybutu obiektu (domyślnego)
    def pole(self):
        return self.a**2
    def obwod(self):
        return self.a*4

provideUtility(Kwadrat())
x=getUtility(IKwadrat)
x.a=5
IKwadrat.validateInvariants(x) #walidacja
if x.a>0:
    print("Pole kwadratu wynosi:",x.pole())
    print("Obwód kwadratu wynosi:",x.obwod())
y=getUtility(IKwadrat)
y.a=-10
IKwadrat.validateInvariants(y) #walidacja
if y.a>0:
    print("Pole kwadratu wynosi:",y.pole())
    print("Obwód kwadratu wynosi:",y.obwod())
provideUtility(Kwadrat()) #jeszcze raz rejestrujemy komponent
z=getUtility(IKwadrat) #tworzymy komponent (atrybut domyślny)
IKwadrat.validateInvariants(z) #walidacja
if z.a>0:
    print("Pole kwadratu wynosi:",z.pole())
    print("Obwód kwadratu wynosi:",z.obwod())
