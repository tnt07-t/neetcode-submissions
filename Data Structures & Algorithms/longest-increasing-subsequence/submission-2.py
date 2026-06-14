class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = {}

        def dfs(index,curr_max):
            if index == len(nums):
                return 0
            if (index,curr_max) in memo:
                return memo[(index,curr_max)]

            res = 0
            if nums[index] > curr_max:
                res = max(res, 1 + dfs(index + 1, nums[index]))

            res = max(res, dfs(index+1,curr_max))
            memo[(index,curr_max)] = res
            return res
    
        return dfs(0,float('-inf'))




        


    


            

    