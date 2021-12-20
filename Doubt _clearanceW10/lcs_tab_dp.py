def lcs(X,Y,m,n):
    L = dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]==0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i][j-1],L[i-1][j])

    l = L[m][n]
    ans = [" "]*(l+1)
    ans[l] = ""

    i = m
    j = n

    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            ans[l-1] = Y[j-1]
            i-=1
            j-=1
            l-=1
        elif L[i][j-1]<L[i-1][j]:
            i-=1
        else:
            j-=1

    return "".join(ans)

X = "AGGTAB"
Y = "GXTXAYB"
#LCS = GTAB
m = 6
n = 7

print(lcs(X,Y,m,n))