class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        for i in range(len(nums)): #missing one number
            if i not in numSet:
                return i
        return len(nums)

