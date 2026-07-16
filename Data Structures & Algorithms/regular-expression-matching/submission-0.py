class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from collections import defaultdict

        memo = defaultdict(int)

        def match(indexS, indexP):
            if (indexS, indexP) in memo: #check dp
                return memo[(indexS, indexP)]

            if indexP == len(p): #base case
                return indexS == len(s)
            
            first_match = (indexS < len(s)) and (p[indexP] == s[indexS] or p[indexP] == '.')

            if indexP + 1 < len(p) and p[indexP + 1] == '*':
                # zero occurrences OR one+ if first_match
                ans = match(indexS, indexP+2) or (first_match and match(indexS + 1, indexP))
            else:
                ans = first_match and match(indexS + 1, indexP + 1)

            memo[(indexS, indexP)] = ans
            return ans

        match(0,0)
        return memo[(0,0)]



