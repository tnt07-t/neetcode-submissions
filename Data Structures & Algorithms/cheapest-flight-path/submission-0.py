class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airports = defaultdict(set)
        for from_i, to_i, price_i in flights:
            airports[from_i].add((to_i, price_i))

        dist = [float('inf')] * n
        dist[src] = 0

        q = deque()
        q.append((src, 0))              # src, not root
        for _ in range(k + 1):          # bound the levels
            size = len(q)
            while size > 0:
                curr, price = q.popleft()
                size -= 1
                for airport, p in airports[curr]:
                    if price + p < dist[airport]:
                        dist[airport] = price + p
                        q.append((airport, price + p))

        return dist[dst] if dist[dst] != float('inf') else -1