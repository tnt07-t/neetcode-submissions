class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        reach = 0 # furthest index reachable from any index seen so far
        boundary = 0 # furthest index reachable within current jump
        for i in range(len(nums)-1): #range -> no need to jump @ end
            reach = max(reach, i + nums[i])
            if i == boundary:
                res += 1
                boundary = reach
        return res
            