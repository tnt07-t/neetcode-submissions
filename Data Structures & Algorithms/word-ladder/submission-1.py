class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #checking if endWord in wordlist -> if not return 0. or not for now
        #min -> bfs
        #if it is, going from  beginword -> endword
        #hashmap -> word to its possible words
        from collections import defaultdict
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(len(word)): #generate possible mappings
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)
            

        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        res = 1
        while q:
            size = len(q)

            while size > 0:
                curr = q.popleft()
                if curr == endWord:
                    return res

                for i in range(len(curr)):
                    pattern = curr[:i] + '*' + curr[i+1:]
                    for p in patterns[pattern]:
                        if p not in visited: #check before appending
                            visited.add(p)
                            q.append(p)

                size -= 1
            res += 1

        return 0


        


        