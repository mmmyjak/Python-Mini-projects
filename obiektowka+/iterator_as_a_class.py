class Tablica(object):

    def __init__(self,n):
        self.n,self.a=n,[0 for i in range(n)]

    def __setitem__(self,key,value): self.a[key]=value
    def __getitem__(self,key): return self.a[key]
    def __str__(self): return str(self.a)
    def __iter__(self): return IteratorNormalny(self)
    def __len__(self): return len(self.a)

class IteratorNormalny(object):
    def __init__(self,tab):
        self.tab,self.n=tab,-1
    def __iter__(self):
        return self
    def __next__(self):
        self.n+=1
        if self.n<len(self.tab):
            return self.tab[self.n]
        raise StopIteration
        
tab=Tablica(5)
tab[0]=1
tab[1]=2
tab[2]=3
tab[3]=4    
tab[4]=5
print(tab)
for i in tab:
    print(i)
