class Solution:
    def getSum(self, a: int, b: int) -> int:
        #XOR -> where no 1 & 1 collision
        #and -> where both are 1's -> shift left one position 
        MASK    = 0xFFFFFFFF
        INT_MAX = 0X7FFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        #1x.... is negative number, 0... is positive. 
        #to get a negative number's abs val: flip all bits, then add 1 
        return a if a <= INT_MAX else ~(a ^ MASK)

            