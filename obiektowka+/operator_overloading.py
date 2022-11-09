import sys

class Lista(object):
    def __init__(self, a):
        if isinstance(a, list):
            self.a = a
        else:
            print("a nie jest listą")
            sys.exit()
    def __setitem__(self,key,value): self.a[key]=value
    def __getitem__(self,key): return self.a[key]
    def __len__(self): return len(self.a)
    def __add__(self, other):
        result = None
        if isinstance(other, Lista):
            uporz = [self.a, other] if (len(self.a) > len(other)) else [other, self.a]
            result = [0 for i in range(len(uporz[0]))]
            for i in range(len(uporz[1])):
                result[i] = uporz[1][i] + uporz[0][i]
            for i in range(len(uporz[1]), len(uporz[0])):
                result[i] = uporz[0][i]
            return result
        elif isinstance(other, int) or isinstance(other, float):
            result = [0 for i in range(len(self.a))]
            for i in range(len(self.a)):
                result[i] = self.a[i] + other
            return result
        else:
            return "Nie da się dodać"

    def __radd__(self, other):
        result = [0 for i in range(len(self.a))]
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.a)):
                result[i] = self.a[i] + other
        return result

l1 = Lista([3,4,5,6,7])
l2 = Lista([6,1,31,3])
print(l1+l2)
print(l1+4)
print(5+l2)