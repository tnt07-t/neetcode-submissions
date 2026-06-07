class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        res = nums[0]

        for num in nums:
            if num == 0:
                curMax, curMin = 1,1
            tmp = curMax
            #max can be any of the 3 
            curMax = max(curMax * num, curMin * num, num)
            #min can be any of the 3
            curMin = min(tmp * num, curMin * num, num)

            if curMax > res:
                res = curMax

        return res




#if max is positive -> max * with positive num
#if minp is

