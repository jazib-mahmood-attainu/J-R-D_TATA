def merge(A,B):
    p1 = 0
    p2 = 0
    m = len(A)
    n = len(B)
    C= []
    while p1<m and p2<n:#1st
        if A[p1]<B[p2]:
            C.append(A[p1])
            p1+=1
        else:
            C.append(B[p2])
            p2+=1

    while p1<m:#2nd when elements are left in A
        C.append(A[p1])
        p1+=1

    while p2<n:#3rd when elements are left in B
        C.append(B[p2])
        p2+=1

    return C

if __name__=="__main__":
    A = [1,3,3,3,3,5,7,9]#(n/2)
    B = [2,4,6,8,31,33,35]#(n/2)
    res = merge(A,B)
    print(res)
