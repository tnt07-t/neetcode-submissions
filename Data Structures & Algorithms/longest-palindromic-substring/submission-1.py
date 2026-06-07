class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        resLen = 1

        for i in range(len(s)):
            curLen = 1
            cur = s[i]
            #odd length
            j = 1
            while i-j>=0 and i+j<len(s) and s[i-j] == s[i+j]:
                curLen += 2
                cur = s[i-j:i+j+1]
                j += 1
                if curLen > resLen:
                    resLen = curLen
                    res = cur

            #even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res


    