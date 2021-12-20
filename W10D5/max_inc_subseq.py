def max_len_subseq(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[j]+1,dp[i])
    return max(dp)

# arr = [5,1,7,8,2,15]
arr = [2,5,15,3,4,20,9,10]
res = max_len_subseq(arr)
print(res)