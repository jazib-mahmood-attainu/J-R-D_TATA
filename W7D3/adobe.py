#Brute Force
def char_repeated(sub):
    for i in range(len(sub)):
        if sub[i] in sub[:i]+sub[i+1:]:
            return True
    return False
        

def solve(st):
    n = len(st)
    max_len = 0
    for i in range(n):
        for j in range(i,n):
            sub =  st[i:j+1]#substring
            if not char_repeated(sub):
                max_len = max(max_len,len(sub))

    return max_len
                                
l = solve("ADOBECODEBANC")
print(l)
