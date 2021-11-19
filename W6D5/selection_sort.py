A = [8,5,6,3,9,8,3,9,1,8]
B = []

for i in range(len(A)):#step 4->go to step 1
    min_ele = A[0]
    min_ele_indx = 0
    for indx in range(len(A)):#step 1->finding minimum element
        if A[indx]<min_ele:
            min_ele = A[indx]
            min_ele_indx = indx
    B.append(A[min_ele_indx])#step 2->put it in it's correct position
    A.remove(A[min_ele_indx])#step 3-> remove from original list

print(B)
print(A)
#T(n) = O(n^2)
#S(n) = O(n)