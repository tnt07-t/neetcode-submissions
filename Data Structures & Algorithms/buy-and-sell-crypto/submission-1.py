class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ret = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            ret = max(ret, profit)

            #finds lower selling price
            if prices[r] < prices[l]: 
                l = r
        return ret
