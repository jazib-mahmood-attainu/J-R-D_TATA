from inherit import Parent

class Child(Parent):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def hair_color(self):
        print("Black")

obj = Child(5,10,15)

obj.hair_color()




        