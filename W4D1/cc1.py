class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name of the student is {self.name}, and roll number is {self.roll}")
    
    def setAge(self,age):
        self.age = age
    
    def setMarks(self,marks):
        self.marks = marks
        
    
s1 = Student("Jazib","1")
s2 = Student("Imran","2")

s2.display()
s1.setAge(30)
print(s1.age)
s1.setMarks(500)
print(s1.marks)
