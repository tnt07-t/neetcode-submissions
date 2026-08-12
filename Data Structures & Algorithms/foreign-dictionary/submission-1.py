class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #kAHNS TOPOLOGICAL SORT
        from collections import deque

        graph = defaultdict(set) #char : set of bigger chars
        chars = {c for word in words for c in word}
        inOrder = {c:0 for c in chars} #26 possible chars; if inOrder[c] == 0 -> can visit

        for i in range(1, len(words)):
            prev,curr = words[i-1], words[i]
            for c1,c2 in zip(prev,curr):
                if c1 != c2: #there is ordering
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        inOrder[c2] += 1
                    break
            else:
                if len(curr) < len(prev):
                    return ""


        q = deque([c for c in chars if inOrder[c] == 0]) #contains visitable
        res = []
        
        while q:
            curr = q.popleft()
            res.append(curr)
            for nxt in graph[curr]:
                inOrder[nxt] -= 1
                if inOrder[nxt] == 0: #already visited
                    q.append(nxt)


        return "".join(res) if len(res) == len(chars) else ""






        