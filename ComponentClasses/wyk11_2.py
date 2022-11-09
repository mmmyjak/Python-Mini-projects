from zope.interface import Interface, implementer
from zope.component import provideUtility, getUtility

class IWprowadzaniedanych(Interface):
    def wprowadz():
        """wprowadzamy dane"""
class ISrednia(Interface):
    def obliczsrednia(a):
        """obliczamy srednia"""

@implementer(IWprowadzaniedanych)
class Wprowadzaniedanych(object):
    def wprowadz(self):
        a=[]
        n = int(input("Ile danych: "))
        for i in range(n):
            x = int(input("Podaj daną: "))
            a.append(x)
        return a

@implementer(ISrednia)
class Srednia(object):
    def obliczsrednia(self,a):
        suma = 0
        for i in a:
            suma += i
        return suma/len(a)

provideUtility(Wprowadzaniedanych())
l = getUtility(IWprowadzaniedanych)
x = l.wprowadz()
provideUtility(Srednia())
wynik = getUtility(ISrednia)
print("Średnia to:", wynik.obliczsrednia(x))