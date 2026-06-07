# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            val = cur.val
            #p and q in left subtree
            if p.val < val and q.val < val:
                cur = cur.left
            #p and q in right subtree
            elif p.val > val and q.val > val:
                cur = cur.right
            #p and q on diff sides of subtree OR node is p or q
            else:
                return cur
