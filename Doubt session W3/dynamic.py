def length():
    A = []
    wish = True
    i = 1
    while(wish==True): #False==True -> False
        print("Enter number",i)
        n = int(input())
        A.append(n)
        i+=1
        ch = input("Do you wish to add more numbers?y/n:")
        if ch=='y':
            pass
        elif ch=='n':
            wish=False
        else:
            print("wrong choice")
    print("size of this list is", len(A))


length()
    





