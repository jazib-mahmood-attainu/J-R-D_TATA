def move(A):
    n = len(A)
    w = n-1
    r = n-1

    while(r>=0):
        if A[r]!=0:
            A[w] = A[r]
            w -= 1
        r -= 1

    while w>=0:
        A[w] = 0
        w -= 1
    print(A)

A = [1,10,20,0,59,63,0,88,0]
move(A)
