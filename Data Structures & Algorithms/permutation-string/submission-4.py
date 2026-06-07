from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        charSet, windowSet = defaultdict(int), defaultdict(int)

        for i in range(len(s1)):
            charSet[s1[i]] += 1
            windowSet[s2[i]] += 1

        if charSet == windowSet:
            return True 

        for i in range(len(s1), len(s2)):
            windowSet[s2[i]] += 1 #increment new char
            windowSet[s2[i-len(s1)]] -= 1 #decrement 

            #clean up for comparison
            if windowSet[s2[i - len(s1)]] == 0:
                del windowSet[s2[i - len(s1)]]

            if charSet == windowSet:
                return True 

        return charSet == windowSet
                
            