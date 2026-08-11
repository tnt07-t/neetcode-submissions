class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums) - 2                  # number of real balloons, at indices 1..n
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1
                lr = nums[l-1] * nums[r+1]
                best = 0
                row = dp[l]
                for i in range(l, r + 1):
                    coins = lr * nums[i] + row[i-1] + dp[i+1][r]
                    if coins > best:
                        best = coins
                dp[l][r] = best

        return dp[1][n]