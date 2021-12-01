def valid(s):
    ob = cb = 0
    step = 0
    for i in s:
        step += 1
        print(step)

        if i == "(":
            ob+=1
        elif i == ")":
            cb+=1
        if ob>=cb:
            continue
        else:
            return "INVALID","cb > ob"

    if ob==cb:
        return "Valid"
    else:
        return "INVALID","ob > cb"

s = "()()))((("
res = valid(s)
print(res)
    