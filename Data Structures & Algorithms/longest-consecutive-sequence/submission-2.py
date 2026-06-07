class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        
        for n in numSet:
            # only start counting if n is the start of a sequence
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                maxLen = max(maxLen, length)
        
        return maxLen