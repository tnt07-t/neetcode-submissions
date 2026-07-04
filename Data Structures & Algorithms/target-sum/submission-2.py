class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #for each nums, go through add/subtract -> next -> save result at each index
        self.res = 0

        def sum(index,tot):
            if index == len(nums): #base
                if tot == target:
                    self.res += 1
                return
            
            #add
            sum(index + 1, tot + nums[index])
            #subtract
            sum(index + 1, tot - nums[index])

        sum(0,0)

        return self.res