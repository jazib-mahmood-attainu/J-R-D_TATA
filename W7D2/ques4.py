def power(x):
    step = 0
    original_value = x
    while(x!=1):
        
        if x%2==0:
            x=x//2
        else:
            x = 3*x+1
        step+=1
        if x==original_value:
            return -1

    return step

# lo = int(input("lo"))
# hi = int(input("hi"))
lo = 12
hi = 15
res = dict()
for i in range(lo,hi+1):
    res[i] = power(i)
# print(res)

val_list = sorted(list(res.values()))

k = 2
print(val_list)
for key,value in res.items():
    if val_list[k-1]==res[key]:
        print(key)
    




