class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #bfs, from each treasure outwards
        ROWS,COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        steps = 1
        while q:    
            size = len(q)
            for i in range(size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 2**31 - 1: #reach land
                        grid[nr][nc] = steps #modify in place
                        q.append((nr,nc))
            steps += 1
                
                

