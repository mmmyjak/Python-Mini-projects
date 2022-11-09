from zope.interface import Interface

class IDom(Interface):
    def klient(a): """ustalamy dane klienta"""
    def wielkosc(a): """ustalamy wielkość domu"""
    def liczbapomieszczen(a): """ustalamy liczbę pokoi"""
    def garaz(wybor): """definiuje czy dostępny garaż"""
    def polozenie(miasto, dzielnica): """ustala lokalizację"""
    def cena(): """ustalamy cenę"""
    def zapis(f): """zapisujemy klienta do pliku"""

class IDom2(Interface):
    def ogrodek(wybor):
        """definiuje czy dostępny ogródek"""
    def cena():
        """ustalamy nową cenę"""
    def zapis(f):
        """zapisujemy klienta do pliku, uwzględniając zmiany"""
        