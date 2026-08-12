class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        so each if u compare each index -> then yk which before which

        if conflict -> return ""

        else -> continue mapping 

        once graph[key] is None -> then latest char

        each char can have key: list of set of chars after it
        '''
        graph = defaultdict(set)
        chars = {c for word in words for c in word}

        for i in range(1,len(words)):
            prev = words[i-1]
            curr = words[i]
            

            for c1,c2 in zip(prev,curr):
                if c1 != c2:
                    #c1 is smaller than c2. then has to break
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                    break
            else:
                if len(prev) > len(curr): #not allowed
                    return ""
        
        visited = {} # 0 = currently visiting, 1 = done
        res = []

        def dfs(c): #respect order
            if c in visited:
                return visited[c] == 1 # ok if visited
            visited[c] = 0 #mark visiting
            for nxt in graph[c]:
                if not dfs(nxt):
                    return False
            visited[c] = 1 #mark visited
            res.append(c)
            return True
        
        for c in chars: #ensures visits all characters not j ordered ones
            if c not in visited:
                if not dfs(c):
                    return ""

        return "".join(res[::-1])


                


            