/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        string res;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()){
            TreeNode* node = q.front(); q.pop();
            if (node){
                res += to_string(node->val) + " ";
                q.push(node->left); //push even if null -> make null child
                q.push(node->right);
            }
            else{
                res += "# "; //mark null
            }
        }
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        stringstream ss(data);
        string item; //empty
        getline(ss, item, ' ');//item is first part before first ','

        TreeNode* root = new TreeNode(stoi(item));
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()){
            TreeNode* node = q.front(); q.pop();
            //if pass -> change nullptr children to Treenodes
            if (getline(ss, item, ' ') && item != "#"){
                node->left = new TreeNode(stoi(item));
                q.push(node->left);
            }
            if (getline(ss, item, ' ') && item != "#"){
                node->right = new TreeNode(stoi(item));
                q.push(node->right);
            }
        }

        return root;
    }
};
