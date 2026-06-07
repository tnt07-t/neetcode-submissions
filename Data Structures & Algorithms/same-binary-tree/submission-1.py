# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
                
            l1,r1 = node1.left, node1.right
            l2,r2 = node2.left, node2.right

            if node1.val != node2.val:
                return False
            return check(l1,l2) and check(r1,r2)
        
        return check(p,q)