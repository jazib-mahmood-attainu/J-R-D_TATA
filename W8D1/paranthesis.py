#not brute force, using stacks

def is_valid(s):
    stack = list()
    for ch in s:
        if ch=="(":
            stack.append(ch)
        else:
            if len(stack)==0:
                return "INVALID"
            stack.pop()

    if len(stack)==0:
        return "VALID"
    else:
        return "INVALID"

s = "(())(()()"
res = is_valid(s)
print(res)