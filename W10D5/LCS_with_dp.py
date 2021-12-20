dp = [[-1 for _ in range(1000)] for _ in range(1000)]

def LCS(str1,str2,idx1,idx2):
    if idx1>=len(str1) or idx2>=len(str2):
        return 0
    if dp[idx1][idx2]!=-1:
        return dp[idx1][idx2]

    if str1[idx1]==str2[idx2]:
        ans =  1 + LCS(str1,str2,idx1+1,idx2+1)
    else:
        c1 = LCS(str1,str2,idx1+1,idx2)
        c2 = LCS(str1,str2,idx1,idx2+1)
        ans =  max(c1,c2)
    
    dp[idx1][idx2] = ans
    return ans



res = LCS("ABCED","AED",0,0)
print(res)
