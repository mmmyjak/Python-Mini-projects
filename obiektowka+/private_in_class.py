class Czlowiek(object):
    ile = 0
    def __init__(self, imie, nazwisko, rok_ur):
        Czlowiek.ile+=1
        self.__imie = imie
        self.nazwisko = nazwisko
        self.rok_ur = rok_ur
    def __str__(self):
        return self.__imie + " " + self.nazwisko + ", urodzony w " + str(self.rok_ur)
        
    def __ileMaszLat(self):
        return 2022 - self.rok_ur
    @staticmethod
    def ileLudu():
        return Czlowiek.ile

mietek = Czlowiek("Mietek", "Gaz", 1990)
print(mietek)
print(mietek._Czlowiek__ileMaszLat())
print(mietek.ileLudu())
print(mietek._Czlowiek__imie)