nums = [1,1,1,2,2,2,4,4,4,4,4]
#index  0 1 2 3 4 5 6 7 8 9 10
#expected lower bound = 3
target = 3
l = 0
h = len(nums)-1
while l<=h:
    mid = (l+h)//2
    if nums[mid]<target:
        l = mid+1
    elif nums[mid]>target:
        h = mid - 1
    else:#nums[mid] == target
        ans = mid
        h = mid-1 # to make it upper bound => l = mid+1

print(ans)

