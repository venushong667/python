from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def moveLeft(self):pass
    @abstractmethod
    def moveRight(self):pass
    @abstractmethod
    def moveUp(self):pass
    @abstractmethod
    def moveDown(self):pass

class Dog(Animals):
    def __init__(self):
        self.x = 0
        self.y = 0
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

class Cat(Dog):
    def __init__(self):
        super().__init__()

def main():
    d = Dog()
    d.moveLeft()
    d.moveLeft()
    d.moveRight()
    d.moveUp()
    print("Dog move, x =", d.x, "y =", d.y)

    c=Cat()
    c.moveRight()
    c.moveDown()
    c.moveRight()
    print("Cat move, x =", c.x, "y =", c.y)

if __name__ == "__main__":
    main()
