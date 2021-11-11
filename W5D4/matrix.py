A = [#col0,1,2
        [1,2,3],#row 0
        [4,5,6],#row 1
        [7,8,9],#row 2
        
    ]
#S(n) = O(n*m) if I dont know the matrix
#A[0][1] = 2
#A[2][2] = 9
#A[1][2] = 6

n = len(A)
m = len(A[0])
print("matrix is of size ",n,"x",m)

#printing the whole matrix
for i in range(n):
    for j in range(m):
        print(A[i][j],end=" ")
    print() #T(n) = O(n^2) or O(n*m)

#print diagonal elements
print("print diagonal elements")
for i in range(n):
    print(A[i][i],end=" ")
print()#T(n) = O(n)

#while loop to print a matrix

# r = 0
# c = 0

# while r<n and c<m:
#     print(A[r][c])
#     r+=1
# c+=1
