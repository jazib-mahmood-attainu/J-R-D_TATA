A = [1,2,3,4]
n =  len(A)
swapped = False

for i in range(n):#step 3
    for j in range(n-1):#step 2
        if A[j]>A[j+1]:#step 1
            A[j],A[j+1] = A[j+1],A[j]
            swapped = True
    if swapped == False:
        print("List already sorted")
        break


print(A)

#worst = O(n^2)
#best case= O(n)
