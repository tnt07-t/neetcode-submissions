class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        from heapq import heappush, heappop
        '''
        grid[i][j] = elevation at cell
        rain falls @ t = 0 -> waterlevel only increases. @ time t = t

        pathfinding -> find path with smallest highest num to m-1,n-1
        @ time t, need all reachable cells 
        '''
        
        n = len(grid)
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        visited = set()
        visited.add((0,0))

        h = []
        heappush(h,(grid[0][0],0,0)) # t = water level @(r,c)
        
        curr_t = 0
        while h:
            t,r,c = heappop(h)

            curr_t = max(curr_t, t)
            #base case
            if (r, c) == (n-1, n-1):
                return curr_t

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                
                #for all unvisited neighbors -> push in heap
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heappush(h,(grid[nr][nc],nr,nc))
            
            







            

