class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1,len(intervals)):
            s2,e2 = intervals[i]
            s1,e1 = merged[-1]

            if s2<=e1:
                merged[-1][1] = max(e1,e2)
            else:
                merged.append([s2,e2])
        return merged