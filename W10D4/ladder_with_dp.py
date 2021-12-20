import time
dp = [None for _ in range(1000)]
def ladder(start_pos,n):
    if start_pos==n:
        return 1
    if start_pos>n:
        return 0
    if dp[start_pos]!=None:
        return dp[start_pos]
    one_step = ladder(start_pos+1,n)#1
    two_step = ladder(start_pos+2,n)#0
    ans = one_step+two_step #1
    dp[start_pos] = ans #dp[2] = 2
    return ans

n = 35

st = time.time()
res = ladder(0,n)
print(res)
end = time.time()

print("Time taken", end-st)
