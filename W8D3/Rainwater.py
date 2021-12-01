class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        
        for i in range(n):
            if i==n-1:
                rhmax = 0
            else:
                
                rhmax = max(height[i+1:])
            if i==0:
                lhmax = 0
            else:
                lhmax = max(height[:i])
            Wcur = min(lhmax,rhmax)-height[i]
            
            if Wcur<0:
                Wcur = 0
            
            total+=Wcur
            
        return total
            