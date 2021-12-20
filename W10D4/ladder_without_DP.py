import time
def ladder(start_pos,n):
    if start_pos==n:
        return 1
    if start_pos>n:
        return 0
    one_step = ladder(start_pos+1,n)
    two_step = ladder(start_pos+2,n)
    return one_step+two_step

n = 35

st = time.time()
res = ladder(0,n)
print(res)
end = time.time()

print("Time taken", end-st)
