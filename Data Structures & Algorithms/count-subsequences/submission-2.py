class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
            
        for each, have choice to use / skip. dp[i][j] = numways to form t[:j] from s[:i]



        '''
        m,n = len(s), len(t)
        
        dp = [[0] * (n+1) for _ in range(m+1)]

        dp[0][0] = 1 #take nothing

        # 1 way empty t from i chars -> take none
        for i in range(1,m+1):
            dp[i][0] = 1

        for i in range(1,m+1): 
            #can take from any char in s
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j] #ways to reach t[:j] with prev chars
                #if new char is equal:
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1] # a ways to get to prev char * (b+1) ways to get new subsequence
                
        return dp[m][n]

                


            


