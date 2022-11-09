class TABINT(object): #klasa modelująca tablicę int
    def __init__(self,n): self.a=[0 for i in range(n)]
    def __str__(self): return str(self.a)
    def __getitem__(self,key): #indeksator - odczyt
        if key<len(self.a):
            return self.a[key]
        else:
            return "Błąd. Indeks poza zakresem tablicy"
    def __setitem__(self,key,value): #indeksator - zapis
        if key<len(self.a) and isinstance(value,int):
            self.a[key]=value
        elif key>=len(self.a):
            print("Błąd. Indeks poza zakresem tablicy")
        else:
            print("Błąd. Wartość w tablicy musi być typu int")
    def __len__(self): #definicja metody specjalnej długość
        return len(self.a)
def main():
    tab = TABINT(5)
    tab[0]=2
    tab[1]=4
    tab[2]=6
    tab[3]=8
    tab[4]=10
    tab[5]=11 #przekroczony zakres
    tab[4]=4.5 #nieodpowiedni typ
    print(tab)
    print(tab[2])
    print(tab[9]) #przekroczony zakres
    print("Długość tablicy:",len(tab))

    # a = 3
    # print(isinstance(a, int))

    print(tab.a[2]) #alternatywa
    tab.a[2] = 3
    print(tab.a[2])
main()

