class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        l,r = 0, len(nums) - 1
        res = nums[0] 

        while l <= r:
            #in sorted order
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            
            m = (l + r) // 2
            res = min(res, nums[m])

            #left half is sorted -> search right
            if nums[m] >= nums[l]:
                l = m + 1
            #right half is sorted -> search left
            else:
                r = m -1
                
        return res


        