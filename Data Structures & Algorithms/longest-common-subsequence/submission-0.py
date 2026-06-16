class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        #grid m x n = [len(text2) + 1] x [len(text1) + 1]
        #extra space + 1 for r,c for 0's -> base case 
        for i in range(len(text1) - 1,-1,-1):
            for j in range(len(text2) - 1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

