class NotAFunctionError(Exception):
    pass
class Tablica(object):
    def __init__(self,n):
        self.a=[0 for i in range (n)]
    def __str__(self):
        return str(self.a)
    def oblicz(self,f): #definicja delegata
        try:
            if str(type(f)) != "<class 'function'>":
                raise NotAFunctionError
        except NotAFunctionError:
            print("It's not a function")
        except:
            print("Probably it doesn't exist")
        else:
            return f(self.a)
def suma(a):
    return sum(a)
def iloczyn(a):
    iloczyn=1
    for i in range(len(a)):
        iloczyn*=a[i]
    return iloczyn
def sumakw(a):
    suma=0
    for i in range(len(a)):
        suma+=a[i]**2
    return suma

def main():
    tab = Tablica(5) #utworzenie pustej tablicy
    print("Początkowa tablica:",tab)
    tab.a[0]=1 #przypisanie wartości elementów
    tab.a[1]=2
    tab.a[2]=3
    tab.a[3]=4
    tab.a[4]=5
    print("Tablica po zmianie",tab)
    print("Suma liczb w tablicy:",tab.oblicz(suma)) #wyw. del.
    print("Iloczyn liczb w tablicy:",tab.oblicz(iloczyn))
    print("Suma kwadratów liczb w tablicy:",tab.oblicz(sumakw))
main()
