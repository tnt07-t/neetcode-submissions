# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush,heappop
        
        #heap -> minheap
        #val to linkedlist hashmap
        #-> pop for result
        h = []
        count = 0
        #create heap by node value
        for lst in lists: #must have i for tiebreaker in case equal vals
            head = lst 
            while head: #all values in heap r valid node, no nil
                heappush(h,(head.val,count, head))
                head = head.next
                count += 1
        
        #recreate res linked list
        dummy = res = ListNode()
        
        while h:
            val,count,node = heappop(h)
            dummy.next = node
            dummy = dummy.next
        
        return res.next
        
        



        
            