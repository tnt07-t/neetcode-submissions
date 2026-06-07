# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        node = head
        node0 = None
        while node:
           dummy = node.next
           node.next = node0
           node0 = node
           node = dummy
        return node0
        