class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        nonzero_prod = 1
        count0 = 0
        ret = [0] * len(nums)
        for i in range(len(nums)):
            product *= nums[i]
            if nums[i] != 0:
                nonzero_prod *= nums[i]
            if nums[i] == 0:
                count0 += 1

        if count0 > 1:
            return [0] * len(nums)

        for r in range(len(nums)):
            if nums[r] == 0:
                ret[r] = nonzero_prod
            else:
                ret[r] = int(product / nums[r])
        return ret
