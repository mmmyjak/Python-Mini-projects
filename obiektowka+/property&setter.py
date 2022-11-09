class Vector3D(object):
    def __init__(self,a,b,c): 
        self.__a,self.__b,self.__c=a,b,c
    def __str__(self): 
        return str([self.__a,self.__b,self.__c])
    @property
    def A(self): 
        return self.__a
    @A.setter
    def A(self,x): 
        self.__a=x
    @property
    def B(self):
         return self.__b
    @B.setter
    def B(self,x):
         self.__b=x
    @property
    def C(self): 
        return self.__c
    @C.setter
    def C(self,x):
         self.__c=x
    @property #wł. tylko do odczytu
    def DL(self): 
        return (self.A**2+self.B**2+self.C**2)**(1/2)
def main():
    v = Vector3D(4,5,6)
    print("Twój wektor:",v)
    print("Współrzędne:",v.A,v.B,v.C)
    print("Zmieniamy")
    v.A, v.B, v.C = 8, 9, 10
    print("Wektor po zmianie:",v)
    print("Długość nowego wektora:",v.DL)
    print(v._Vector3D__a)
main()
