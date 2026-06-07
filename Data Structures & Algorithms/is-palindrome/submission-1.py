class Solution:
    def isPalindrome(self, s: str) -> bool:

        lower = [c.lower() for c in s if c.isalnum()]
        cleaned = ''.join(lower)

        return cleaned == cleaned[::-1]