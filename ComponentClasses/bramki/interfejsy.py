from zope.interface import Interface

class IBramka(Interface):
    def NOT(a): """oblicza negacje"""
    def OR(a, b): """oblicza sumę logiczną"""
    def AND(a, b): """oblicza iloczyn logiczny"""
    def NOR(a, b): """oblicza negację sumy logicznej"""
    def NAND(a, b): """oblicza negację iloczynu logicznego"""
    