#question was wrong,only number of ones should be the same to give YES as output
A = list(map(int,input().split()))
b1 = bin(A[0])[2:]
b2 = bin(A[1])[2:]
zb1 = ob1 = 0
for i in b1:
    if i == "0":
        zb1+=1
    else:
        ob1+=1
zb2 = ob2 = 0
for i in b2:
    if i == "0":
        zb2+=1
    else:
        ob2+=1
        
if ob1==ob2:
    print("YES")
else:
    print("NO")