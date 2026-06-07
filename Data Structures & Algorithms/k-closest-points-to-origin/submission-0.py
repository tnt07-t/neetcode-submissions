from heapq import heappush,heappop,heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return (x ** 2 + y ** 2, x, y)

        h = [(distance(x,y),x,y) for x,y in points]
        
        heapify(h)

        ret = [[x,y] for _, x, y in [heappop(h) for _ in range(k)]]
        return ret
