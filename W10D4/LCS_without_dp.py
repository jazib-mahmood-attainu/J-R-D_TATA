
def LCS(str1,str2,idx1,idx2):
    if idx1>=len(str1) or idx2>=len(str2):
        return 0
    if str1[idx1]==str2[idx2]:
        return 1 + LCS(str1,str2,idx1+1,idx2+1)
    else:
        c1 = LCS(str1,str2,idx1+1,idx2)
        c2 = LCS(str1,str2,idx1,idx2+1)
        return max(c1,c2)



res = LCS("ABCED","AED",0,0)
print(res)
