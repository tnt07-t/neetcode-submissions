class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        from heapq import heappush,heappop
        res = [-1] * len(queries)
        heap = [] # (interval_length, end_time)
        i = 0

        #sort queries (val,index)
        queries = sorted((val,i) for i,val in enumerate(queries)) 
        intervals.sort()

        for q,index in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start,end = intervals[i]
                heappush(heap,(end-start+1, end)) #push all intervals that start before inclusive to query
                i+=1
            
            while heap and heap[0][1] < q: #pop invalid intervals -> q only increases in value -> no need revisit
                heappop(heap)
            
            if heap:
                res[index] = heap[0][0]
        return res
        

            


