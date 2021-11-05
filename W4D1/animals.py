class Animals:
    def __init__(self,name,legs,tail):
        self.name = name
        self.legs = legs
        self.tail = tail

    def runs(self):
        print(f"{self.name} with {self.legs} legs is running")

class Dog(Animals):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)
        
    def bark(self):
        print("Dog is barking")
        
obj = Dog("lab",4,True)
obj.bark()
obj.runs()

