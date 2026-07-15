from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        indegree = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1
        
        dp = [[1] * COLS for _ in range(ROWS)]
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    queue.append((r, c))
        
        res = 1
        while queue:
            r, c = queue.popleft()
            res = max(res, dp[r][c])
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        queue.append((nr, nc))
        
        return res