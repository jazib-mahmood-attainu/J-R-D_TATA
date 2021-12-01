def solve(A):
    n = len(A)
    stack = list()#[]

    B = [0]*n

    for idx,val in enumerate(A):
        if len(stack)==0:
            stack.append(idx)
        else:
            while(len(stack)!=0 and A[stack[-1]]<val):
                x = stack.pop()
                B[x] = val
            stack.append(idx)

    while len(stack)!=0:
        x = stack.pop()
        B[x] = -1

    return B

A = [2,1,7,4,6,8,1,9]
res = solve(A)
print(res)


