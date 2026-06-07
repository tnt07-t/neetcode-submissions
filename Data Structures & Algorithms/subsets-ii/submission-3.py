class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #FOR LOOP METHOD -> Which element do i pick next?  
        curr = []
        def dfs(i):
            #collect @ every node
            res.append(curr.copy())
            
            for j in range(i,len(nums)):
                #skip adding the same number to subset
                if j > i and nums[j-1] == nums[j]: 
                    continue 
                    
                curr.append(nums[j])
                dfs(j + 1)

                curr.pop()

        dfs(0)
        return res