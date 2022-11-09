from zope.interface import Interface, implementer
from zope.component import provideUtility, getUtility

class ISuma_Iloczyn(Interface):

    def suma(a,b):
        """oblicza sumę liczb naturalnych od a do b"""
    def iloczyn(a,b):
        """oblicza iloczyn liczb naturalnych od a do b"""

@implementer(ISuma_Iloczyn)
class Suma_Iloczyn(object):

    def suma(self,a,b):
        suma = 0
        for i in range(a,b+1):
            suma +=i
        return suma
    
    def iloczyn(self,a,b):
        iloczyn = 1
        for i in range(a,b+1):
            iloczyn*=i
        return iloczyn

provideUtility(Suma_Iloczyn())
obiekt = getUtility(ISuma_Iloczyn)
s=obiekt.suma(20,80)
s2=obiekt.suma(5,10)
i=obiekt.iloczyn(10,20)
i2=obiekt.iloczyn(2,5)
print("Suma liczb od 20 do 80 wynosi:",s)
print("Suma liczb od 5 do 10 wynosi:",s2)
print("Iloczyn liczb od 10 do 20 wynosi:",i)
print("Iloczyn liczb od 2 do 5 wynosi:",i2)  
