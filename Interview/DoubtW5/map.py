# s = input()
# A = list(map(int,s.split()))
# print(A)

s = "abcdefg"
s2 = ""
for i in range(len(s)):
    if i<4:
        s2+="$"
    else:
        s2+=s[i]


print(s2)
