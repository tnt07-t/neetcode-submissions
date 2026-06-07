class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(2,len(nums)):
            if i>=3:
                nums[i] = max(nums[i-3] + nums[i], nums[i-2] + nums[i], nums[i])
            else:
                nums[i] = max(nums[i-2] + nums[i], nums[i])

        
        return max(nums[-1], nums[-2])