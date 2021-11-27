def solve(A,target):#O(nlogn)
    A.sort()#O(nlogn)
    p1 = 0
    p2 = len(A)-1
    while p1<p2:#O(n)
        if (A[p1]+A[p2])<target:
            p1+=1
        elif (A[p1]+A[p2])>target:
            p2-=1
        else:
            s = f"Pair exists {A[p1]} and {A[p2]}"
            return s
    
    s = "Pair doesnt exist"
    return s

A = [8,4,6,3,9]
target = 7
res = solve(A,target)
print(res)



