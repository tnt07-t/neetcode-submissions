class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(speed):
            time = 0
            for pile in piles:
                time += (pile+speed - 1)//speed
            return time

        l,r = 1, max(piles) #slowest,quickest speeds
        #binary search on speeds
        res = r
        while l <= r:
            m = (l+r)//2
            need = check(m)
            if need <= h: #valid
                res = m 
                r = m - 1 #try slower
            else:
                l = m  + 1
        return res
        
            
            
                