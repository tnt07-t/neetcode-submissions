class MedianFinder:
    def __init__(self):
        #left = max heap of smaller half 
        #right = min heap of bigger half  
        #eg: left = [1 2 3] right = [4 5]
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        from heapq import heappush, heappop
        
        heappush(self.left, -num)
        # rule 1: left max must be <= right min
        if self.right and -self.left[0] > self.right[0]:
            heappush(self.right, -heappop(self.left))
        
        # rule 2: balance sizes
        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))
        elif len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))


    def findMedian(self) -> float:
        from heapq import heappush, heappop
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2
        
        