class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #going clockwise?
        n = len(matrix)

        for turn in range(n//2): #num of layers
            #begin to 
            first = turn 
            last = n - first - 1 
            for i in range(first, last): # num swapped per layer
                offset = i - first
                top = matrix[first][i]

                 # left -> top
                matrix[first][i] = matrix[last - offset][first]

                # bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]

                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]

                # top -> right
                matrix[i][last] = top
