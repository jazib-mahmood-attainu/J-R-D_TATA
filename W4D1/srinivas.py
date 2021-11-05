# t = int(input("Enter how many values you want?"))
# A = []
# for i in range(t):
#     A.append(int(input("Enter the value")))

# print(A)
A = []
wish = True
while(wish==True):
    A.append(int(input("Enter the value")))
    choice = input("Do you want to continue?y/n")
    if choice=="y":
        continue
    elif choice=="n":
        wish = False
    else:
        print("enter valid value, only 'y' or 'n'")

print(A)
