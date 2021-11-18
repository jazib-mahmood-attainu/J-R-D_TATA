def reverse(s):
    if len(s)==0:
        return
    print(s[-1],end=" ")
    n = len(s)
    reverse(s[:-1])
    print()



s = "hello"
reverse(s)