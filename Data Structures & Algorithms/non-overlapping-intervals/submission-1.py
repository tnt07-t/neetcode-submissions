class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #one way is to for each interval, if theyre not over lapping
        # -> append to that group then if it becomes 

        intervals.sort(key = lambda x: x[1]) #sort by end time
        res = 0
        final = []
        for itv in intervals:
            start,end = itv[0], itv[1]
            if final and start < final[-1][1]: #ends before the prev ends
                res += 1
            else:
                final.append(itv)
        return res

