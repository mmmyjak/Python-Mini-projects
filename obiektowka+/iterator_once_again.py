class Tablica(object):
    def __init__(self,n):
        self.n,self.a=n,[0 for i in range(n)]
    def __setitem__(self,key,value): self.a[key]=value
    def __getitem__(self,key): return self.a[key]
    def __str__(self): return str(self.a)
    def __iter__(self):
        k=0
        while k<len(self.a):
            yield self.a[k]
            k+=1
tabliczka = Tablica(5)
tabliczka[0]=1
tabliczka[1]=2
tabliczka[2]=3
tabliczka[3]=4
tabliczka[4]=5
for i in tabliczka:
    print(i)