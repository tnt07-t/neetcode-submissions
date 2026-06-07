class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    
        max_heap = [-stone for stone in stones]
        #Syntax: heapq.heapify(heap) 
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)

            if heaviest == second_heaviest:
                continue
            else:
                remaining = (heaviest - second_heaviest)
            #Syntax: heapq.heappush(heap, x) 
            heapq.heappush(max_heap,-remaining)
        return -max_heap.pop() if max_heap else 0

            