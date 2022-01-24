def bit(num,bits):
    temp = 1<<bits
    temp = temp&num
    if temp == 0:
        return 0
    return 1

def get_subsets(v,subsets):
    count = 2**len(v)
    for i in range(count):
        st = set([])
        for j in range(len(v)):
            if bit(i,j) == 1:
                st.add(v[j])
        subsets.append(st)


v= [1,2,3]
subsets = []
get_subsets(v,subsets)

print(subsets)