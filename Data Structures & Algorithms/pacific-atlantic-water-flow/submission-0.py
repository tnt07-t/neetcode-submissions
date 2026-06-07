class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        pac = set()
        atl = set()


        #starts is list of coordinates adj to pacific/atlantic

        def bfs(starts, visited):
            q = deque(starts)
            for s in starts:
                visited.add(s)

            while q:
                r,c = q.pop()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if (nr,nc) in visited:
                        continue
                    if heights[r+dr][c+dc] < heights[r][c]:
                        continue

                    visited.add((nr,nc))
                    q.append((nr,nc))
        
        pac_starts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atl_starts = [(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS)]

        bfs(pac_starts, pac)
        bfs(atl_starts, atl)
        return list(pac & atl)
                
                        

                
                    