# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([root])
        ret = []

        while q:
            size = len(q)
            level = []
            while size > 0:
                node = q.popleft()
                level.append(node.val)
                left,right = node.left, node.right
                #add children to q
                if left:
                    q.append(left)
                if right:
                    q.append(right)
                size -= 1
            ret.append(level)

        return ret