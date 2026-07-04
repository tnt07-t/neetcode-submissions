class WordDictionary {
    struct Node {
        unordered_map<char,Node*> children;
        bool isEnd = false;
    };
    Node* root;

public:
    WordDictionary() {
        root = new Node();
    }
    
    void addWord(string word) { //Time:len(w); Space: len(w)
        //curr is not a node, but pointer to a node; & gets address of root node
        Node* curr = root; 

        for (char c : word){
            if (!curr->children.count(c)){
                curr->children[c] = new Node(); //new node
            }
            curr = curr->children[c]; //move to child
        }
        curr->isEnd = true; //mark end
    }
    
    bool search(string word) {//Time:O(26^w) -> worst case '.', space:O(w) -> recursion stack
        return dfs(root, 0, word);
    }

    private:
    bool dfs(Node* node, int pos, string word){
        if (pos == word.size())return node->isEnd;

        char c = word[pos];

        if (c == '.'){ //any ch works 
            for (auto& [ch,next] : node->children)
                if (dfs(next, pos + 1, word)) return true;
            return false;
        }
        else{ // ch must match c
            //check exist -> dfs
            if (node->children.count(c) and dfs(node->children[c], pos+1,word)) return true;
            return false;
            }
        }
};

