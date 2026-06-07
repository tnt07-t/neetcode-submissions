class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            prev2,prev1 = nums[0],max(nums[0],nums[1])

            for i in range(2,len(nums)):
                curr = max(prev2 + nums[i], prev1)
                prev2,prev1 = prev1, curr

            return prev1

                
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:       
            return max(nums)

        return max(helper(nums[:-1]), helper(nums[1:]))
        
    
            