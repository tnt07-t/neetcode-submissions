class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #build amount from any num of of each coin in coins
        #distinct combos  -> backtracking -> recomputes a lot of cases because, for example, you do one path, then pop and theres another path from midway to end -> recalculate all
        # dp -> diff combos -> {1,2} and {2,1} are the same. thus instead of iterating by amt i will do by coin type -> can only add one at a time

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(amount): #0 - amount - 1
                if j + coin <= amount: 
                    dp[j + coin] += dp[j]
                else:
                    print(j+coin)
                    break

        return dp[amount]
