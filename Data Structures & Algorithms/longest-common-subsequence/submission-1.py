class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        #dp[i][j] = lcs between text1[i:] and text2[j:]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] #diagonal -> both move on 1 char
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
