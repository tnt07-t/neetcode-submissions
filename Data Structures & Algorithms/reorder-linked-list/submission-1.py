# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast and fast.next!= None:
            fast = fast.next.next 
            slow = slow.next

        second = slow.next #either same size as first or smaller by one node
        slow.next = None #terminate first half

        #reverse linked list second
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        #merge
        l1,l2 = head,prev
        while l1 and l2: 
            next1 = l1.next
            next2 = l2.next
            #connect
            l1.next = l2
            l2.next = next1
            #update
            l1 = next1
            l2 = next2
            






