from abc import ABC, abstractmethod
from math import sqrt

class Animal(ABC):
    @abstractmethod
    def moveLeft(self):pass
    @abstractmethod
    def moveRight(self):pass
    @abstractmethod
    def moveUp(self):pass
    @abstractmethod
    def moveDown(self):pass

class Cat(Animal):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__()
    def moveLeft(self):
        self.x -= 1
        return self.x
    def moveRight(self):
        self.x += 1
        return self.x
    def moveUp(self):
        self.y += 1
        return self.y
    def moveDown(self):
        self.y -= 1
        return self.y

class Dog(Animal):
    def __init__(self,x,y):
        super().__init__(x,y)

    #def distance(p0, p1):
    #    return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def main():
    d = Dog(-7,-4)

    print("Dog(x =", d.x, "y =", d.y,")")

    c=Cat(17,6.5)
    print("Cat(x =", c.x, "y =", c.y,")")

    a=Animal()
    #dis = d.distance(c)
    #print(dis)

if __name__ == "__main__":
    main()
