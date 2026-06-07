from heapq import heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k 

        heapify(nums)

        count = 0
        while count <= k:
            res = heappop(nums)
            count += 1
        
        return res