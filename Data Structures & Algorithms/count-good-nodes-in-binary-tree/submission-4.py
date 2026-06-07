# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mvalue):
            if not node:
                return 0
            mvalue = max(mvalue, node.val)
            good = 1 if node.val >= mvalue else 0  # note: check BEFORE updating mvalue
            return good + dfs(node.left, mvalue) + dfs(node.right, mvalue)

        return dfs(root,root.val)

       