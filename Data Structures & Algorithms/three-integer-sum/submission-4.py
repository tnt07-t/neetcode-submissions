class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort ascending order
        nums.sort(key = lambda x:x)
        l = 0
        ret = []
        for l in range(len(nums) - 2):
            #because nums is sorted, we can do this to skip duplicate
            if l > 0 and nums[l] == nums[l-1]:
                continue
        
            m,r = l + 1, len(nums) - 1

            while m < r:
                s = nums[l] + nums[m] + nums[r]
                if s == 0:
                    ret.append([nums[l],nums[m],nums[r]])
                    #no break cuz there might be other valid pairs
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    m += 1
            l += 1
        return ret