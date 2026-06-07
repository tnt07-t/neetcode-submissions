class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #IDEA: appeared hashes (hashmap of count) : (index in ret)
        appeared = {}
        ret = []
        num_sublists = 0
        for string in strs:
            count = {}
            for c in string:
                count[c] = 1 + count.get(c, 0)


            key = tuple(sorted(count.items()))
            if key in appeared: #add to existing sublist
                ret[appeared[key]].append(string)
            else:#new sublist
                appeared[key] = len(ret)
                ret.append([string])

        return ret
            