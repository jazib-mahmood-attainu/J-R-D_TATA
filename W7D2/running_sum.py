#Amazon SDE interview problem
def running_sum(A):
    R = []
    R.append(A[0])#R[0] = A[0]
    for i in range(1,len(A)):
        R.append(R[i-1]+A[i])
    return R

def solution(R,i,j):
    if i == 0:
        return R[j]
    return R[j]-R[i-1]

A = [1,5,-1,0,4,8,4]
#    0 1  2 3 4 5 6
R = running_sum(A)#O(n)
i = 2#O(1)
j = 5#O(1)
res = solution(R,i,j) #O(1)
print(res)#O(1)

"""
if n queries are there,this code takes O(n+n)
"""