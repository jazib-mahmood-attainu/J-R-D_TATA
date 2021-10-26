# print greatest among 3.
a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))

if a > b:# a=5 b=4
    if a > c: # a = 5 c = 3
        print("a is biggest")
    else:
        print("c is biggest")
else: # b > a
    if b > c:
        print(" b is biggest")
    else:#c > b
        print("c is biggest")

