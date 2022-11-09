from zope.interface import implementer
from zope.component import provideUtility
from interfejsy import *

@implementer(IBramka)
class Bramka(object):
    def NOT(self,a):
        return not a
    def OR(self,a,b):
        return (a or b)
    def AND(self,a,b):
        return (a and b)
    def NOR(self, a,b):
        return not (a or b)
    def NAND(self,a, b):
        return not (a and b)
provideUtility(Bramka())