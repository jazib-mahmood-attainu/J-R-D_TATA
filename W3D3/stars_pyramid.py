n = int(input("enter rows for the star"))
s = n-1
for i in range(n):
    
    for j in range(s):
        print(end=" ")
    s-=1
    for j in range(i+1):
        print("*",end = " ")
    print()

