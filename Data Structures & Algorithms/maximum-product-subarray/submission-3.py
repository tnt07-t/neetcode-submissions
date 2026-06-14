class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curr_max = nums[0]
        curr_min = nums[0]

        for n in nums[1:]:
            if n == 0:
                curr_min, curr_max = 1,1
                continue
            tmp = curr_max * n
            curr_max = max(tmp, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)

            res = max(res,curr_max)
        return res