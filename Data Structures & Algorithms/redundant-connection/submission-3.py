class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges) #num nodes = num edges + 1. one redundant edge in edges

        #extra because nodes are 1-indexed -> want to line up
        par = [i for i in range(N+1)]
        rank = [0] * (N+1) 

        def find(n):
            if par[n] == n:
                return n
            return find(par[n])
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2: #cycle detected
                return False 
            elif rank[p1] < rank[p2]:
                #merge p1 into p2
                par[p1] = p2
                rank[p1] += rank[p2]
            else:
                par[p2] = p1
                rank[p2] += rank[p1]
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        
        