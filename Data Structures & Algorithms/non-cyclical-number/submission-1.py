class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num not in seen and num != 1:
            seen.add(num)
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num = num//10
            num = total
        return True if num == 1 else False
