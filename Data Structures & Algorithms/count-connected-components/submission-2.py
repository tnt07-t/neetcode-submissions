class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()
        components = 0

        def bfs(node):
            q = collections.deque([node])

            while q:
                curr = q.popleft()
                visited.add(curr)
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            
        for i in range(n):
            if i not in visited:
                bfs(i)
                components += 1

        return components
                
