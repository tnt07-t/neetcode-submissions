# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #returns height of tree - BUT return is NOT result. 
        #1. recursively get height 
        #2. update res as recursing
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.res