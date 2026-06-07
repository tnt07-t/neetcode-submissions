# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        val = root.val
        if p.val == val or q.val == val:
            return root
        #p and q on different sides of tree
        if (p.val < val and q.val > val) or (p.val > val and q.val < val):
            return root
        #p and q in left subtree
        elif p.val < val and q.val < val:
            return self.lowestCommonAncestor(root.left,p,q)
        #p and q in right subtree
        return self.lowestCommonAncestor(root.right,p,q)
