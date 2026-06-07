class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0
        while l<r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                res += lmax - height[l]
                l += 1
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                res += rmax - height[r]
                r -= 1
        return res
            
