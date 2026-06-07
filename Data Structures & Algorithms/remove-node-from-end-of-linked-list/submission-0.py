# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#count list size -> figure position from beginning of list -> remove

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, size = head, 0
        while curr != None:
            size += 1
            curr = curr.next

        
        pos = size - n + 1

        #if remove head
        if pos == 1:
            return head.next


        curr = head
        prev = None
        while pos > 1:
            prev = curr
            curr = curr.next
            pos -= 1 

        prev.next = curr.next
        return head

        