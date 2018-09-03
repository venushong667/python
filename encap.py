class Encap():
    def __init__(self):
        self.__x = 5
        self.y = 3
    def __printx(self):
        print(self.__x)
    def __printy(self):
        print(self.y)

y1 = Encap()
print(y1._Encap__x)
y1._Encap__printx()
y1._Encap__printy()
