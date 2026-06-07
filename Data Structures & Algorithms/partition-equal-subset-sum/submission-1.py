class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums)%2 != 0:
            return False
        used = [False] * len(nums)

        def backtrack(i, subsetSum):
            if subsetSum == target:
                return True
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue

                #include nums[j]
                used[j] = True
                if backtrack(j+1, subsetSum + nums[j]):
                    return True
                
                #not include nums[j]
                used[j] = False
                if subsetSum == 0:
                    return False
            
            return False
        return backtrack(0,0)

