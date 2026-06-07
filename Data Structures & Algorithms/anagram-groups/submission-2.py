class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\
    #implement hashmap : list of indices in s
        groups = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
        

        

        