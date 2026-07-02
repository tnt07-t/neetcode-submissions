class TrieNode:
    def __init__(self):
        self.children = {} # char : TrieNode
        self.endOfWord = False #track word ends
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children: #if not exist
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True #doesnt need to be @ end of word
        
        