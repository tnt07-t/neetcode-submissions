class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(-1,0), (0,1), (0,-1)]

        def dfs(r,c):
            grid[r][c] = 0
            tot = 1
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    tot += dfs(nr,nc)
            return tot

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        
        return res
                
            