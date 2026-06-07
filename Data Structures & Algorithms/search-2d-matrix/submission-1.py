class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])

        l,r = 0, ROWS * COLS - 1
    
        def couple(idx):
            return idx // COLS, idx % COLS

        while l <= r:
            m = (l + r)//2
            row,col = couple(m)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1

        return False
                