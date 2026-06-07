# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count list size
        curr = head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        
        pos = size - n

        if pos == 0:
            return head.next
        
        pointer = 0

        lst = head
        #move pointer to right before removed node
        while pointer < pos - 1:
            lst = lst.next
            pointer += 1
        
        lst.next = lst.next.next
        return head

        