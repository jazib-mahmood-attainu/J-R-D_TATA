def merge(A,start_l,end_l,start_r,end_r):
    p1 = start_l
    p2 = start_r

    C = []

    while p1<=end_l and p2<=end_r:
        if A[p1]<A[p2]:
            C.append(A[p1])
            p1+=1
        else:
            C.append(A[p2])
            p2+=1
        
    while p1<=end_l:#2nd when elements are left in left side
        C.append(A[p1])
        p1+=1

    while p2<=end_r:#3rd when elements are left in right side
        C.append(A[p2])
        p2+=1

    idx = 0
    while idx<len(C): #  A = C, creating a copy of C in A
        A[start_l+idx] = C[idx]
        idx+=1  


def merge_sort(A,low,high):#sort list A from low to high
    mid = (low+high)//2
    if low==high:
        return
    merge_sort(A,low,mid)#sort list A from low to mid
    merge
    merge_sort(A,mid+1,high)#sort list A from mid+1 to high
    merge(A,low,mid,mid+1,high)#low = strat_l,end_l,start_r,end_r
    print(A)




A = [8,5,6,3,9,8,3,9,1,8]
merge_sort(A,0,len(A)-1)
print(A)


# A = [1,3,5,7,2,4,6,8]
# #    0 1 2 3 4 5 6 7 
# start_l = 0
# start_r = 4
# end_l = 3
# end_r = 7
# merge(A,start_l,end_l,start_r,end_r)