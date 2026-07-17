class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                #if hasnt been used -> use / not use
                curr.append(nums[i])
                used[i] = True
                backtrack(curr)

                curr.pop()
                used[i] = False

        backtrack([])
        return res