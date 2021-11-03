l = [8,5,6,3,9,8,3,9,1,8]
#    0,1,2,3,4,5,6,7,8,9
ctr_e = 0
ctr_o = 0
for i in range(len(l)): #0,1,2,3,4,5,6,7,8,9
    if l[i]%2==0:
        ctr_e += 1 
    else:
        ctr_o += 1 

d = {}
d["Even"] = ctr_e
d["Odd"] = ctr_o

print(d)
