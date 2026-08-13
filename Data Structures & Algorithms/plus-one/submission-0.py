class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        for i in range(n-1,-1,-1):
            d = digits[i]
            if d != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
    
        return digits if digits[0] != 0 else [1] + digits
