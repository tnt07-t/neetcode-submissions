class Solution:
    def checkValidString(self, s: str) -> bool:
        #hi = max ), lo = min )
        hi = lo = 0
        
        for c in s:
            if c == "(":
                hi, lo = hi+1, lo+1
            elif c == ")":
                hi, lo = hi-1, lo-1
            else: #is *
                hi = hi + 1
                lo = lo - 1

            if hi < 0:
                return False
            lo = max(lo, 0)

        return lo == 0
