n = int(input("Enter row"))
m = int(input("Enter column"))
# A = []
# for i in range(n):
#     A.append([])
#     for j in range(m):
#         element = int(input(f"Enter element for row {i+1} and cloumn {j+1}"))
#         A[i].append(element)

A = [[0 for j in range(m)] for i in range(n)]


print(A)
