class Solution:
    def rob(self, nums: List[int]) -> int:
        second = 0  #max until prev
        most = 0    #max until before prev

        for n in nums:
            cur = max(most, second + n)
            second = most 
            most = cur

        return most
