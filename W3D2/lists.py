"""
syntax 
list_name = [1,2,3,4]
or 
list_name = []
or 
list_name = list()

"""

# A = [ 5,12,"raj", 15,5.02,"raj"]
#     # 0  1   2    3   4     5

# print(A[2],A[5])

A = [2,5,7,8,15,20,30]
#Q-> print elements at even index
for i in range(len(A)):
    if i%2 == 0:
        print(A[i])


A = [1,2,3,4,5,6,7,8,9,10]

print(A[0:len(A):2])
   #-4,-3,-2,-1    <-negative indexing
a = [1, 2, 3, 4]
    #0, 1, 2, 3     <-positive indexing
print(a[-4])

# print(A[2:6])#index 2,3,4,5
# print(A[1:6:2])

# print(len(A))

    #         -1
A = [8,5,6,3,9,8]
    #0,1,2,3,4,5

print(A[:4]) # 8 5 6 3
print(A[2:]) # 6 3 9 8
print(A)
print(A[::2])#0 2 4=> 8 6 9
print(A[:-1])#8 5 6 3 9 
#reversing a list
print(A[::-1]) #8 9 3 6 5 8

print("************")
A = [8,5,6,3,9,8]
    #0,1,2,3,4,5

# i = input("Enter value to be put in the list")
print(A)
A.append(10) #inserts an element at the end


print(A)

A.insert(4,100)# inserts element before specified index

print(A)
