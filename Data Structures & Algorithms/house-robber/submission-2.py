class Solution:
    def rob(self, nums: List[int]) -> int:
        second = 0  
        most = 0    

        for n in nums:
            cur = max(most, second + n)
            second = most
            most = cur

        return most
