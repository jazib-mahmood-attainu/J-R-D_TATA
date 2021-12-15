import time

def Fib(n,dp):
    if n == 1 or n == 2:
        return 1

    if dp[n]!=-1:
        return dp[n]
    ans = Fib(n-1,dp)+Fib(n-2,dp)
    dp[n] = ans
    return ans


st = time.time()
dp = [-1]*1000 #dp = [-1,-1,-1,-1,......]
res = Fib(40,dp)
end = time.time()

print("Time taken", end-st)