from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charSet = defaultdict(int)
        res = 0

        for r in range(len(s)):
            total = r-l+1
            charSet[s[r]] += 1
            most = max(charSet.values())
            while (total - most) > k:
                charSet[s[l]] -= 1
                l += 1
                total = r-l+1
                most = max(charSet.values())

            res = max(res, r-l + 1)

        return res