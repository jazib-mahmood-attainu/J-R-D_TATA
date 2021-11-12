def binary_search(arr,target):
    l = 0
    h = len(arr)-1

    while l<=h:
        mid = (l+h)//2
        if arr[mid] < target:
            l = mid+1
        elif arr[mid] > target:
            h = mid-1
        else:
            return mid
    return -1
#      0 1  2 3  4  5  6 
arr = [2,8,32,40,60,80,86]
target = int(input("Enter the number you want to search"))
res = binary_search(arr,target)
print(res)

# T(n) = O(logn)
# S(n) = O(1)