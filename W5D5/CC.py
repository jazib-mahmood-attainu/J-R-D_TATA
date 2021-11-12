#Q1
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    
]

n = len(A)
m = len(A[0])
sum = 0
# for i in range(n):
#     sum = sum + A[i][n-i-1]
# print(sum)

#rect matrix
# if n<m:
#     limit = n
# else:
#     limit = m
# for i in range(limit):
#     sum = sum + A[i][m-i-1]
# print(sum)


# for i in range(min(n,m)):
#     sum = sum + A[i][m-i-1]
# print(sum)


#Q2

for i in range(n):
    for j in range(m):
        if i==0:
            sum += A[i][j]
        elif i == n-1:
            sum += A[i][j]
        elif j == 0:
            sum += A[i][j]
        elif j == m-1:
            sum += A[i][j]
        else:
            pass
print(sum)