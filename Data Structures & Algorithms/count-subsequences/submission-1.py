class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #num ways -> find an instance of letter -> 
        m,n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m+1): #ways to reach "" at any index -> just take none
            dp[r][0] = 1 

        #at each index, see how many ways to achieve parts of t
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] != t[j-1]: #then ways to reach is ways u reached at prev index in s
                    dp[i][j] = dp[i-1][j]
                else:
                    #equal -> you can either use it OR ignore it -> add up
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        return dp[m][n]


