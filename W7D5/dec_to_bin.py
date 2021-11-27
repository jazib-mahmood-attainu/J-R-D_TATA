def dec_to_bin(dec):
    binary = ""
    while dec>0:
        rem = dec%2
        binary += str(rem)
        dec//=2

    return binary[::-1]


res = dec_to_bin(55)
print(res)