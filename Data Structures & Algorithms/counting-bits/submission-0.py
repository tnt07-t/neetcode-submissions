class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            cur,count = i,0
            while cur > 0:
                if cur % 2 == 1:
                    count += 1
                cur //= 2
            res[i] = count

        return res
