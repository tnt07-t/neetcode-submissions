class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #scan -> find treasure chest -> bfs

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        #validate cells to add
        def addCell(r,c):
            if (min(r,c) < 0 
            or r == ROWS or c == COLS 
            or (r,c) in visit or grid[r][c] == -1):
                return 
            visit.add((r,c))
            q.append([r,c])
            
        #step 1: add all gates to queue (dist = 0)
        for r in range(ROWS):
            for c in range(COLS):
               if grid[r][c] == 0:
                q.append([r,c])
                visit.add((r,c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                #add neighbors to queue -> validated by addCell() method
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            #once queue is empty -> all cells in layer is visited
            dist += 1


                    
        