class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ROWS, COLS = len(s), len(p)

        dp = [[False] * (COLS + 1) for _ in range(ROWS + 1)]

        dp[ROWS][COLS] = True

        for r in range(ROWS, -1, -1):
            for c in range(COLS-1, -1, -1):
                match = r < ROWS and (s[r] == p[c] or p[c] == '.')

                if c + 1 < COLS and p[c+1] == '*':
                    #use none(skip) or use as multiple chars
                    dp[r][c] = dp[r][c+2] or (match and dp[r+1][c])
                else:
                    dp[r][c] = match and dp[r+1][c+1]

        return dp[0][0]

                