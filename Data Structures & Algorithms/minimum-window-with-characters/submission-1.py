class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
    
        need = Counter(t) 
        window = defaultdict(int) #freq of chars in window
        have, total = 0, len(need)

        res = ""

        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in need:
                window[c] += 1

                if window[c] == need[c]:
                    have += 1
                
                while have == total: #window is valid, try shrink
                    if not res or (r -l + 1) < len(res):
                        res = s[l:r + 1]

                    # l at char in need 
                    if s[l] in need:
                        window[s[l]] -= 1
                        if window[s[l]] < need[s[l]]:
                            have -= 1
                    l += 1
        return res
                        

