class Solution:
    def countSubstrings(self, s: str) -> int:
        #odd length -> each char is middle
        res = len(s)

        for i in range(len(s)):
            l,r = i-1, i + 1

            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    res += 1
                    #increment
                    l -= 1
                    r += 1
                else:
                    break
        
        #even length 
        for i in range(len(s)):
            l,r = i,i+1
            while l>= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        return res
            
        
        