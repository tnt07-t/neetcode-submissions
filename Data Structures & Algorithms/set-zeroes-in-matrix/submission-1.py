class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        #cannot edit as u go -> false more 0's. track needed 0's and rows, cols

        rows, cols = set(), set()

        #handle (0,0)
        first_row_zero = False
        first_col_zero = False

        for c in range(COLS):
            if matrix[0][c] == 0:
                first_row_zero = True

        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_zero = True

        #mark rows and cols need to change at beginning of row/col
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 #mark row
                    matrix[0][c] = 0 #mark col
        
        #handle rows and cols
        
        for r in range(1,ROWS):
            if matrix[r][0] == 0: #if beginning of row == 0 -> zero the whole row
                for c in range(1,COLS):
                    matrix[r][c] = 0
    
        for c in range(1,COLS):
            if matrix[0][c] == 0: #if beginning of col == 0 -> zero the whole col
                for r in range(1,ROWS):
                    matrix[r][c] = 0


        #Time: O(mn)
        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0

        

            