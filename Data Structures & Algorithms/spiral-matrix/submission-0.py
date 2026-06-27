class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom = 0,len(matrix)-1
        left,right = 0, len(matrix[0])-1

        #Always 4 steps in a loop: right, down, left, up
        res = []
       #matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
       # 1 2  3  4  
       # 5 6  7  8 
       # 9 10 11 12

       #top = 1
       #bottom = 1
       #left = 1
       #right = 2

       #-> 1 2 3 4 -> 8 12 -> 11 10 9 -> 5


        while top <= bottom and left <= right:
            #going right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            
            #going down
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            
            #going left
            if top < bottom:
                for i in range(right-1, left -1, -1):
                    res.append(matrix[bottom][i])
            
            #going up
            if left < right:
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
            
            #shrink
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return res


        


