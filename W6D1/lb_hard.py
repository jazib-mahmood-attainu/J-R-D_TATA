def lower(arr,target):
    low = 0
    high = len(arr)-1
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
arr = [1,1,1,3,3,3,5,5]
target = 4
print(lower(arr,target))

