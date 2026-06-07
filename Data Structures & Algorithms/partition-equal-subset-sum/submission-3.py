#DP SOLUTION!
#Time: O(Nxtarget) -> iterate over n elements, dp hold at most target elements
#Space: O(target) -> dp holds at most target elements
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        dp = {0}
        for num in nums:
            dp = dp | {s + num for s in dp if s + num <= target}
            if target in dp:
                return True
                
        return False
        