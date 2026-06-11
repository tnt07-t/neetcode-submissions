class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))  # carry distance with node

        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 2**31-1:
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))