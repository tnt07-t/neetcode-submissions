"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        nodeMap = {}

        #first pass - create deep copies of nodes
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        #second pass - assign next and random pointers
        
        curr2 = head
        while curr2:
            nodeMap[curr2].next = nodeMap.get(curr2.next)
            nodeMap[curr2].random = nodeMap.get(curr2.random)
            curr2 = curr2.next

        return nodeMap[head]