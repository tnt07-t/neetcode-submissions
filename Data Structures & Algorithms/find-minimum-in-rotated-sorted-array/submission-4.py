class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        l,r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            m = (l + r)//2
            if nums[m] < nums[r]: #min is in left half or is nums[m]
                res = min(nums[m], res)
                r = m - 1
            else:  
                res = min(nums[m], res)
                l = m + 1
        return res
