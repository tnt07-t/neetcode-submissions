class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #find min cost to connect all dots
        #from each, find closest dot to it to connect
        #all points -> make hashmap of points [0,n-1]
        #calculate distance from a point -> all others
        n = len(points)
        visited = [False] * n

        #next distances -> only modify unvisited ones each round
        dist = [float('inf')] * n
        dist[0] = 0 #start at 0, go to itself

        total = 0
        #n rounds -> each round adds one node to connected
        for _ in range(n):
            best = -1
            #each node check all nodes
            for i in range(n):
                if visited[i]:
                    continue
                if best == -1 or dist[i] < dist[best]:
                    best = i
            
            #absorb best
            visited[best] = True
            total += dist[best]

            #update distances
            x,y = points[best]
            for j in range(n):
                if visited[j]: #in connected
                    continue
                #calc dist from best to each -> replace if shorter
                x2,y2 = points[j]
                dist[j] = min(dist[j], abs(x-x2) + abs(y-y2))
        
        return total
            
            

        

        