# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node,minval,maxval):
            if not node:
                return True
            if node.val <= minval or node.val >= maxval:
                return False
            return check(node.left, minval, node.val) and check(node.right, node.val, maxval)
        
        return check(root,float('-inf'), float('inf'))