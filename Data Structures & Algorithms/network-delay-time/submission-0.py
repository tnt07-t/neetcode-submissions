from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #starting k is 
        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))

        minHeap= [(0,k)]
        visited = set()
        t = 0

        while minHeap: #every time pop -> w1 is shortest time to n1
            #pop (weight, node)
            w1,n1 = heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            t = max(t,w1)

            if len(visited) == n:
                return t

            for n2,w2 in edges[n1]:
                heappush(minHeap, (w1+w2, n2))

        return -1
            


             