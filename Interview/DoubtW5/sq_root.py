n = 32
s = 0
e = n

while s<=e:
    mid = (s+e)//2
    # print(mid**2)
    if mid**2 == n:
        ans = mid
        break

    elif mid**2<n:
        s = mid+1
        ans = mid
    else:
        e = mid - 1
    
print(ans)


