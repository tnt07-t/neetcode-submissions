class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #maxheap -> put all elems in then pop first k   
        #kth largest elem is smallest of k largest elems
        #min heap -> every time popped is smallest elem 
        from heapq import heappop,heappush
        heap = []
        for n in nums:
            heappush(heap, n)
            if len(heap) > k:
                heappop(heap) #pops smallest
        
        return heap[0]
