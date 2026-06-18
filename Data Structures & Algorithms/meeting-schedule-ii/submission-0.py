"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        from heapq import heappush, heappop, heapify

        #sort
        #sorted list, heap, deque by start time -> pop them. if 
        #next one begins before current one ends -> increment needed
        #

        intervals.sort(key = lambda interval: interval.start)

        heap = []
        res = 0
        for interval in intervals:
            start, end = interval.start, interval.end
            while heap and start >= heap[0]:
                heappop(heap)
            else: 
                heappush(heap,end)
            res = max(len(heap), res)
        return res
