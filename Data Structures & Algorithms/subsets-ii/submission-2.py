class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #INCLUDE/EXCLUDE METHOD -> exclude duplicate
        #two branches, collect at bottom
        def backtrack(i,subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            #Include
            subset.append(nums[i])
            backtrack(i+1,subset)
    
            #Exclude
            subset.pop()
            while i + 1<len(nums) and nums[i+1] == nums[i]:
                i += 1
            backtrack(i+1,subset)

        backtrack(0,[])
        return res