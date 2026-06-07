class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            q = deque()
            #change value to 0
            grid [r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    #check bounds
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    
                    grid[nr][nc] = "0"
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands