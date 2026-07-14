class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)

        # dp[i][j] = min operations to convert word1[:i] to word2[:j]
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        #Base cases
        for j in range(COLS+1): #if no chars, then to match j chars -> j inserts
            dp[0][j] = j 
        for i in range(ROWS+1):
            dp[i][0] = i

        #go through -> fill table
        for r in range(ROWS):
            for c in range(COLS):
                if word1[r] == word2[c]:
                    dp[r+1][c+1] = dp[r][c]
                else: #try all 3 -> insert/replace/delete
                    dp[r+1][c+1] = 1 + min(dp[r][c+1], dp[r][c], dp[r+1][c])
        return dp[ROWS][COLS]



        