def merge(A,B):
    C = A+B#O(n)
    C.sort()#O(nlogn)
    return C #T(n) = O(nlogn)


if __name__=="__main__":
    A = [1,3,3,3,3,5,7,9]#(n/2)
    B = [2,4,6,8,31,33,35]#(n/2)
    res = merge(A,B)
    print(res)
