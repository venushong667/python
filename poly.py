class animal:
    def __init__(self,name = ""):
        self.name=name
        print(name)
    def sound(self):
        pass

class dog(animal):
    def __init__(self,name = ""):
        super().__init__(name)
    def sound(self):
        print ("Woof!")

class cat(animal):
    def __init__(self,name = ""):
        super().__init__(name)
    def sound(self):
        print ("Meow!")

d = dog("Jack")
d.sound()

c = cat("Miy")
c.sound()
