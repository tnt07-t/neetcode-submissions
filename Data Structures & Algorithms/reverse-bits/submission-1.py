class Solution:
    def reverseBits(self, n: int) -> int:
        #n read right to left
        #ans' bits are added to right
        ans = 0 #initiate
        for _ in range(32): #bit length max 32
            ans = ans << 1 | n & 1 #shifts ans left one spot -> right most becomes 0
            # | adds n or with 1
            n >>= 1
        return ans