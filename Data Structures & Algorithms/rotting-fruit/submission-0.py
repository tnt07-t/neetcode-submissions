class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        directions = [(1,0),(-1,0),(0,1), (0,-1)]

        #get all rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2: #rotten
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        #bfs
        time = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr <ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))   
            time += 1
        return time if fresh == 0 else -1