def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)

if __name__=="__main__":
    n = 4
    res = Fibonacci(n)
    print(res)

