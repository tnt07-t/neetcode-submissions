class Solution:
    def isValid(self, s: str) -> bool:
        keys = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c == ")" or c =="}" or c == "]":
                if not stack or keys[stack.pop()] != c:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        return False