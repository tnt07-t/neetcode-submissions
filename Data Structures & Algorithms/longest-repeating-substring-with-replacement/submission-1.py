import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replacements = length of substring - freq most common
        char_count = collections.defaultdict(int)
        l = 0
        max_freq = 0
        max_length = 0
        for r in range(len(s)):
            char_count[s[r]] += 1
            max_freq = max(max_freq, char_count[s[r]])

            # if invalid window, shrink it
            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)

        return max_length

            