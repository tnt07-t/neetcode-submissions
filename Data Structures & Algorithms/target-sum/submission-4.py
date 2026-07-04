class Solution:
    #2D OPTIMAL
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #for each nums, see +/- target in dp or not? add with count 
        from collections import defaultdict

        dp = defaultdict(int) # (index, tot) -> number of ways
    
        def ways(index, tot):
            if index == len(nums):
                return 1 if tot == target else 0
            if (index,tot) not in dp:
                dp[(index,tot)] = ways(index+1,tot + nums[index]) + ways(index+1, tot - nums[index])
                
            return dp[(index, tot)]

        ways(0,0)
        return dp[(0,0)]
        

