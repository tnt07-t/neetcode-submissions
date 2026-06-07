class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check columns
        for col in range(9):
            values = set()
            for r in range(9):
                if board[r][col] != ".":
                    num = board[r][col]
                    if num in values:
                        return False
                    values.add(num)

        #check rows
        for row in range(9):
            values = set()
            for c in range(9):
                if board[row][c] != ".":
                    num = board[row][c]
                    if num in values:
                        return False
                    values.add(num)
                
        
        #check grid
        def check_grid(row,col):
            values = set()
            for c in range (col, col + 3):
                for r in range (row, row + 3):
                    if board[r][c] != ".":
                        if board[r][c] in values:
                            return False
                        values.add(board[r][c])
            return True

        for i in range(3):
            for j in range(3):
                if not check_grid(i*3,j*3):
                    return False
        
        return True







            


        
