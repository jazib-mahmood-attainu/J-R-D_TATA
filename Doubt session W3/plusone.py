class Solution:
    def conv_int_list(self,n):
        r = list()
        s = str(n)
        for i in s:
            r.append(int(i))
        return r
        
    
    def plusOne(self, digits):
        
        if digits[-1]==9:
            wt = 1
            sum = 0
            for i in digits[::-1]:
                sum = sum + i*wt
                wt = wt*10
            print(sum)
            return self.conv_int_list(sum+1)
        else:
            digits[-1] += 1
            
        return digits
    
    