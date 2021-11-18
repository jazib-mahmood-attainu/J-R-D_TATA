def MotM(overs,runs):
    ABD = True
    VRT = False
    ctr = 0
    a_r = v_r = 0
    for i in runs:
        print(i,"runs",ctr,ABD,a_r,"ABD",VRT,v_r,"VRT")
        if ctr == 6:
            if ABD==True :
                VRT = True
                ABD = False
            else:
                VRT = False
                ABD = True
        if i%2!=0:

            if ABD==True :
                a_r+=i
                VRT = True
                ABD = False
            else:
                v_r+=i
                # print(v_r,i)
                VRT = False
                ABD = True
        else:
            if ABD==True :
                a_r+=i
                
            else:
                v_r+=i
                # print(v_r,i)
        ctr += 1
        # print(i,"runs",ctr,ABD,a_r,"ABD",VRT,v_r,"VRT")
    print(a_r,v_r)

MotM(2,[1,4,0,2,3,6,0,0,0,4,6,2])