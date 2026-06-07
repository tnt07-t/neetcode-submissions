class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        most,second= 0,0
        for num in nums:
            curr = max(second + num, most)
            second= most
            most = curr

        return most

            