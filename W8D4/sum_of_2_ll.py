cur1 = head1
cur2 = head2
cur3 = head3
c = 0
while(cur1!=None and cur2!=None):
    s = cur1.data+cur2.data
    if s+c>9:
        c = s//10
        s = s%10
    
    else:
        c = 0
    cur3.data = s
    cur3 = cur3.next
    cur1 = cur1.next
    cur2 = cur2.next
    



    