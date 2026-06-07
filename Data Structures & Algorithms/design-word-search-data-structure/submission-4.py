#Make a TrieNode class!!
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        """Initialize data structure"""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        "Add a word"
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        """Search a word"""
        if self.root.word == True:
            return True
        
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False    
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            
            # if cur.word is False, then word is a prefix of an added
            # word but not a word added itself
            return cur.word

        return dfs(0,self.root)
