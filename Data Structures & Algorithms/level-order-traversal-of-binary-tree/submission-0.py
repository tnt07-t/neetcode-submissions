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
            
        res = []
        queue = collections.deque([root])

        while queue:
            level = []
            levelsize = len(queue)
            while levelsize > 0:
                child = queue.popleft()
                level.append(child.val)
                if child.left: queue.append(child.left)
                if child.right: queue.append(child.right)
                levelsize -= 1

            if level:
                res.append(level)
        
        return res
            

        