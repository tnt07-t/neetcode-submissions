class Solution:
    # max amt of water determined by 
    # min(heights[l], heights[r]) and width
    # move taller -> guaranteed worse, thus move smaller
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxwater = 0
        while l < r:
            maxwater = max(maxwater, min(heights[r], heights[l]) * (r-l))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-= 1
        
        maxwater = max(r-l, maxwater)
        return maxwater
        