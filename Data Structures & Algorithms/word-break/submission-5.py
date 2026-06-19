class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #wordDict -> reusable bank of words
        #s -> breaks up -> return True if can be composed of w's from wordDict.
        #s can be broken up at any index i for i in range(len(s)) -> subproblem that can be cached -> dp

        #s = "l e e t c o d e"
        #     ^  
        #           ^  
        words = set(wordDict)
        n = len(s)
        
        dp = [False] * (n+1)
        dp[n] = True #past last index -> broke up whole string
        for i in range(n-1,-1,-1):
            for j in range(i,n+1): # check s[i:j]
                if s[i:j] in words and dp[j]:
                    dp[i] = True
                    break

        return dp[0]
