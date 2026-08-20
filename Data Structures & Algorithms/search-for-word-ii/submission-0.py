class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self,word):
        curr = self #current node
        for c in word: 
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        for each cell, check if the initial exists in root -> traverse donw. all possible combos   
        then go through each word in words -> check if in dict
        '''
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        #make all words -> trie
        for w in words:
            root.addWord(w)

        #only dfs if up-to is prefix in trie
        res, visit = set(), set()

        def dfs(r,c,node,word):
            if (r < 0 or c < 0
            or r == ROWS or c == COLS
            or (r,c) in visit or board[r][c] not in node.children):
                return
        
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            #backtrack
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
            
        return list(res)

        