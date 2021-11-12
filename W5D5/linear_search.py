def linear_search(lst,target):
    for i in lst:
        if i == target:
            return True
    return False
    # for i in range(len(lst)):#[0,1,2]
    #     if lst[i] == target:
    #         return i
    # return -1
    ###########
    # if target in lst:
    #     return True
    # else:
    #     return False
    #  0 1 2 3 4 5 6 7 8 9
lst = [8,5,6,3,9,8,3,9,1,8]
target = int(input("Enter the number you want to search"))
res = linear_search(lst,target)
if res == True: #res!=-1
    print("Number is present in the list")#, at index",res)
else:
    print("Number is absent")


# T(n) = O(n)
# S(n) = O(1)
