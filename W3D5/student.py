class Student:
    def __init__(self,name,age,birth_year):
        self.name = name
        self.age = age
        self.birth_year = birth_year #it can have any number of attributes

    def read(self):
        print(f"student {self.name} is reading, who is {self.age} years old")
    
    def write(self):
        print(f"student {self.name} is writing")

rohit = Student("Rohit",21,2000)
shanmukh = Student("Shanmukh",19,2001)
sudhakar = Student("Sudhakar",24,1997)
aniket = Student("Aniket",18,2003)

rohit.read()
shanmukh.read()
sudhakar.read()
aniket.read()



print(f"Rohit is {rohit.age} years old")