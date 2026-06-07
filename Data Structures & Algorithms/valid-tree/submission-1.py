class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #DFS -> checks for cycle

        if len(edges) != n-1:
            return False 

        graph = {i: [] for i in range(n)}

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.pop()
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n
            


        
