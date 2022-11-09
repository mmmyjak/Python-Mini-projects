from komponenty import *
from zope.component import getUtility

x = getUtility(IBramka)

#pierwsza bramka
print("Pierwsza bramka")
a=int(input("Podaj sygnał na pierwszym wejściu:"))
b=int(input("Podaj sygnał na drugim wejściu:"))
wybor={"OR":x.OR(a,b),"AND":x.AND(a,b),\
"NOR":x.NOR(a,b),"NAND":x.NAND(a,b)}
br1=input("Którą bramkę pierwszą podłączamy:")
w1=wybor[br1]
print("Na wyjściu pierwszej bramki:",w1)

#druga bramka
print("Druga bramka:")
a=int(input("Podaj sygnał na pierwszym wejściu:"))
b=int(input("Podaj sygnał na drugim wejściu:"))
wybor={"OR":x.OR(a,b),"AND":x.AND(a,b),\
"NOR":x.NOR(a,b),"NAND":x.NAND(a,b)}
br2=input("Którą bramkę drugą podłączamy:")
w2=wybor[br2]
print("Na wyjściu drugiej bramki:",w2)

#trzecia bramka
print("Trzecia bramka:")
wybor={"OR":x.OR(w1,w2),"AND":x.AND(w1,w2),\
"NOR":x.NOR(w1,w2),"NAND":x.NAND(w1,w2)}
br3=input("Którą bramkę trzecią podłączamy:")
w3=wybor[br3]
print("Na wyjściu trzeciej bramki:",int(w3))