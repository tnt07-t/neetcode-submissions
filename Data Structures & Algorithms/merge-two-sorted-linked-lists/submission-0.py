# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2 = list1,list2
        
        if h1 and h2:
            if h1.val < h2.val:
                h3 = h1
                h1 = h1.next
            else:
                h3 = h2
                h2 = h2.next
            ret = h3
        elif h1:
            return h1
        else:
            return h2



        while h1 and h2:
            if h1.val < h2.val:
                dummy = h1.next
                h3.next = h1
                h1 = dummy
            else:
                dummy = h2.next
                h3.next = h2
                h2 = dummy

            h3 = h3.next #advance h3
        if h1:
            h3.next = h1
        if h2:
            h3.next = h2
    
        return ret
            