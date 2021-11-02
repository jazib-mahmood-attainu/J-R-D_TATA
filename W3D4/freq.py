l = [1,2,1,1,1,2,3,4,5,5]
d = dict() #{}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i] += 1

print(d)

max = float("-inf")
for k in d.keys(): 
    if d[k] > max: 
        max = d[k]
        max_key = k
print(max,"value")
print(max_key,"key")
