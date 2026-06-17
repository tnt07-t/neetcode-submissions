class Solution:
    def checkValidString(self, s: str) -> bool:
        #TWO PASSES
        # 1. left -> right: treat * as )
        bal = 0
        for c in s:                      # left to right
            bal += 1 if c in "(*" else -1
            if bal < 0:
                return False
        # 2. right -> left: treat * as (
        bal = 0
        for c in reversed(s):            # right to left
            bal += 1 if c in ")*" else -1
            if bal < 0:
                return False
        return True