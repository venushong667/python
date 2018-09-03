class Animals():
    def __init__(self):
        print("It is a 4 legs animal.")

    def gettype(self):
        print("Is it a cat or dog?")

#class Dog(Animals):
#    def __init__(self):
#        Animals.__init__(self)
#        self.gettype()

#    def type(self):
#        print("It is a dog")

#x = Dog()
#x.type()

class Cat(Animals):
    def __init__(self):
        super().__init__()       #Super method calling
        self.gettype()

    def gettype(self):           #Overriding gettype from Animals
        print("This is a cat")

y = Cat()
