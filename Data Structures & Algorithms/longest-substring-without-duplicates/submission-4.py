class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        maxcount = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen: #restart window to no duplicates
                    seen.discard(s[l]) #remove leftest character
                    l += 1 
            seen.add(s[r])
            maxcount = max(maxcount, r-l+1)
            r += 1
        return maxcount