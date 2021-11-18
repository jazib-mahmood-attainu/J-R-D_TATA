def Tiling(N):
    if N==0:
        return 1
    if N<0:
        return 0
    return Tiling(N-1)+Tiling(N-2)


res = Tiling(1)
print(res)
