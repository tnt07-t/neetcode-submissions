class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(i, currentList, total):
            if total == target:
                #if no .copy() then storing a reference to the list
                ret.append(currentList.copy())
                return
            if i >= len(nums) or total > target:
                return


            #include current number
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])

            #or skip move forward from current number
            currentList.pop()
            dfs(i+1, currentList, total)

        dfs(0,[], 0)
        return ret
