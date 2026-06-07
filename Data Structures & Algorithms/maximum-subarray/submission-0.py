class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        prefix = 0
        for n in nums:
            if prefix < 0:
                prefix = 0
            res = max(res,prefix + n)
            prefix += n
        return res
            