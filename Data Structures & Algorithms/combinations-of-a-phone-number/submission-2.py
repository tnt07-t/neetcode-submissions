class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2: ['a','b','c'], 
        3: ['d','e','f'], 
        4: ['g','h','i'], 
        5:['j','k','l'], 
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']}

        res = []
        def backtrack(index,curr):
            #base case
            if index == len(digits): 
                if curr:
                    res.append(curr)
                return

            values = mapping[int(digits[index])]
            for v in values:
                backtrack(index+1,curr + v)
            
        backtrack(0,"")
        return res

        #Time: O(N * 4^N)
        #Space: O(N) recursion stack depth"