class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)

        def check(index):
            if index == len(s):
                return True

            if cache[index] is not None:
                return cache[index]

            for word in wordDict:
                if s.startswith(word, index):
                    if check(index + len(word)):
                        cache[index] = True
                        return True

            cache[index] = False
            return False

        return check(0)
                        

            
            

            
