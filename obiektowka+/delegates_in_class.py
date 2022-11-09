class Tablica(object):
    def __init__(self,n): self.a=[0 for i in range (n)]
    def __str__(self): return str(self.a)
    def oblicz(self,f): return f(self.a)
    @staticmethod
    def suma(a): return sum(a)
    @staticmethod
    def iloczyn(a):
        iloczyn=1
        for i in range(len(a)): iloczyn*=a[i]
        return iloczyn
    @staticmethod
    def sumakw(a):
        suma=0
        for i in range(len(a)): suma+=a[i]**2
        return suma

tab = Tablica(5)
print("Początkowa tablica:",tab)
tab.a[0]=1
tab.a[1]=2
tab.a[2]=3
tab.a[3]=4
tab.a[4]=5
print("Tablica po zmianie",tab)
print("Suma liczb w tab:",tab.oblicz(Tablica.suma))
print("Iloczyn liczb w tab:",tab.oblicz(Tablica.iloczyn))
print("Suma kw. liczb w tab:",tab.oblicz(Tablica.sumakw))