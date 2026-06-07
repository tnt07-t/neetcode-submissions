class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque() # stores indices, largest value at front
        res = []
        l = r = 0

        #pop from right smaller values
        while r  < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)
        
            #pop outside window
            while dq[0] < l:
                dq.popleft()
            
            #window is full
            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
            r += 1
            

        return res


            