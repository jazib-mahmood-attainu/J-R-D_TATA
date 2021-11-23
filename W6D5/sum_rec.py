def mul(x,y):
    if y==1:
        return x
    else:
        return x+mul(x,y-1)

res=mul(100,5)
print(res)