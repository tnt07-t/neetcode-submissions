class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}" : "{",
            "]" : "[",
            ")" : "("}

        open_brackets = deque()

        for c in s:
            if c in brackets:
                if not open_brackets or open_brackets.pop() != brackets[c]:
                    return False
            else: #open bracket
                open_brackets.append(c)

        return not open_brackets


