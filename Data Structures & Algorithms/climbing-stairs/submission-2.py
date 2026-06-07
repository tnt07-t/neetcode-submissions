class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # ways(n) = ways(n-1) + ways(n-2)
        prev2, prev1 = 1, 2 #ways to reach 2 steps ago or 1 step ago

        #why?
        #reach n from prev2 by +2 to each way
        #reach n from prev1 by +1 to each way
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1