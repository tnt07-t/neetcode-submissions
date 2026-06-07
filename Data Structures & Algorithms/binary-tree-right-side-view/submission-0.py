# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        q = deque()
        if root:
            q.append(root)

        while q:
            size = len(q)
            while size > 0:
                node = q.popleft()
                size -= 1

                #add next level to queue
                l,r = node.left, node.right
                if l: q.append(l)
                if r: q.append(r)

                if size == 0:
                    ret.append(node.val)
        return ret