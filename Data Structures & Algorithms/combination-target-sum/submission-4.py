class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        tot = 0
        def dfs(i,tot):
            if tot == target:
                res.append(curr.copy())
                return
            if tot > target or i>= len(nums):
                return
            
            curr.append(nums[i])
            tot += nums[i]

            dfs(i,tot)

            curr.pop()
            tot -= nums[i]
            dfs(i+1,tot)

        dfs(0,tot)
        return res