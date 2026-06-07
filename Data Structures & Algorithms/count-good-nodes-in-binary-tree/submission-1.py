# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node, mvalue):
            if node.val >= mvalue:
                self.tot += 1
                mvalue = node.val
            if node.left:
                self.helper(node.left,mvalue)
            if node.right:
                self.helper(node.right,mvalue)

    def goodNodes(self, root: TreeNode) -> int:
        self.tot = 0
        self.helper(root,root.val)
        return self.tot