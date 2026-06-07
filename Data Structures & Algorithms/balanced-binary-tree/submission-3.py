# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #returns height of subtree node
        def dfs(node):
            if not node:
                return [True,0]
            
            left = dfs(node.left)
            right = dfs(node.right)


            if abs(left[1]-right[1]) > 1 or left[0] == False or right[0] == False:
                return [False,1+max(left[1],right[1])]
            
            return [True,1 + max(left[1], right[1])]

            
        return dfs(root)[0]