def factorial(n):
    if n == 1:
        return 1
    f = n*factorial(n-1)
    return f

if __name__=="__main__":
    n = int(input("Enter the number you want factorial of "))
    if n < 1:
        print("Wrong input, give value > 1")
    else:
        res = factorial(n)#24
        print(res)



