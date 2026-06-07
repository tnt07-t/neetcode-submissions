from heapq import heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapmax
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            s1 = heappop(h)
            s2 = heappop(h)
            if s1 != s2:
                heappush(h, s1-s2)
            
        return -h[0] if h else 0

        