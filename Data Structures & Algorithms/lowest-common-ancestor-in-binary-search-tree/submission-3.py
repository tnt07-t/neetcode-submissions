# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while True:
            val = cur.val
            if p.val == val or q.val == val:
                return cur
            #p and q on different sides of tree
            if (p.val < val and q.val > val) or (p.val > val and q.val < val):
                return cur
            #p and q in left subtree
            elif p.val < val and q.val < val:
                cur = cur.left
            #p and q in right subtree
            else:
                cur = cur.right
