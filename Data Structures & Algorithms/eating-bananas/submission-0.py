class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def numHours(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time
        
        
        res = r 

        while l<=r:
            m = (l + r)//2
            hours = numHours(m)

            if numHours(m) <= h:
                res = m #update valid speed
                r = m - 1 #try smaller speed

            else:
                l = m + 1 #need bigger speed
            

        return res
           