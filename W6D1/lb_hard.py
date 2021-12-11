def lower(arr,target):
    low = 0
    high = len(arr)-1
    if target == arr[0]:
        return 0
    if target>arr[high]:
        return high
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]==target and arr[mid-1]<target:#arr[mid+1]>target
            return mid
        elif arr[mid]==target and arr[mid-1]==target:
            high = mid-1
        elif arr[mid-1]<target and arr[mid+1]>target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1
arr = [1,1,1,3,3,4,5,5,5]
#      0 1 2 3 4 5 6 7 
target = 6
print(lower(arr,target))

