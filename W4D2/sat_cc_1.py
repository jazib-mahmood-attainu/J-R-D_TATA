class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

A = [0 for i in range(3)] # A = [0,0,0]

for i in range(3):
    n = input(f"Enter name {i+1}")
    r = input(f"Enter roll {i+1}")
    A[i] = Student(n,r)

for i in range(3):
    print(A[i].name, "has roll number " ,A[i].roll)


