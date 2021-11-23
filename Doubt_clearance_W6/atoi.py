def atoi(s,wt=1):
    if len(s)==1:
        return int(s)*wt
    return int(s[-1])*wt +  atoi(s[:-1],wt*10)


def myAtoiRecursive(st): 
    if len(st) == 1: 
        return int(st) 
    else: 
        return myAtoiRecursive(st[:-1])*10+int(st[-1]) 


print(atoi("999"))