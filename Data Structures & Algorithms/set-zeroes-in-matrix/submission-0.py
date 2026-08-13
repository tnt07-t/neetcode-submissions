class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        #cannot edit as u go -> false more 0's. track needed 0's and rows, cols

        rows, cols = set(), set()

        #mark rows and cols need to change
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        

        for r in rows:
            for c in range(COLS):
                matrix[r][c] = 0
        
        for c in cols:
            for r in range(ROWS):
                matrix[r][c] = 0

        

            