class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #one way is to for each interval, if theyre not over lapping
        # -> remove if overlap
        #greedy -> remove by overlapping

        intervals.sort(key = lambda x: x[1]) #sort by end time
        res = 0
        prev = None
        for itv in intervals:
            start,end = itv[0], itv[1]
            if prev and start < prev: #starts before the prev ends
                res += 1
            else:
                prev = end
        return res

        #Time: O()
        #Space: O(n)