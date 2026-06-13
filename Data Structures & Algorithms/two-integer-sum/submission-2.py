class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #maps complement : index in nums

        for i,n in enumerate(nums):
            diff = target-n

            if diff in indices:
                return [indices[diff], i]

            indices[n] = i
        return []
        