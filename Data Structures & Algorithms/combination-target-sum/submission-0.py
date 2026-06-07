class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(i, currentList, total):
            if total == target:
                ret.append(currentList.copy())
                return
            if i >= len(nums) or total > target:
                return

            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])

            currentList.pop()
            dfs(i+1, currentList, total)

        dfs(0,[], 0)
        return ret
