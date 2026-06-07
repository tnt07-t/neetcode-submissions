class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pair: index, height
        max_area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                max_area = max(max_area, area)
                start = index
            stack.append((start,h))
        
        while stack:
            i,h = stack.pop()
            area = (len(heights) - i) * h # this not - i - 1 
            max_area = max(max_area, area)
        return max_area
            