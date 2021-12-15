import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        l = 0
        for i in nums:
            heapq.heappush(heap,i)
            l += 1
            if l>k:
                heapq.heappop(heap)
                l-=1
                
                   
        
        return heapq.heappop(heap)