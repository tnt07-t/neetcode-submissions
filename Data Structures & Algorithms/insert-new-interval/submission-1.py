class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        i = 0
        n = len(intervals)

        #Step 1: append all intervals before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
    
        #Step 2:
        merged = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            merged[0] = min(intervals[i][0], newInterval[0])
            merged[1] = max(intervals[i][1], newInterval[1])
            i+=1
        res.append(merged)

        while i < n:
            res.append(intervals[i])
            i+=1

        return res