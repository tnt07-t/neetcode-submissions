class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n==0) return 0;
        //3 decisions u can make -> continue hold, sell, or rest 
        //-> 3 vars to track total profits so far. not prices
        int hold = -prices[0]; //price to buy
        int sold = 0;
        int rest = 0;

        for (int i = 0; i < n; i++){
            int prevHold = hold;
            int prevSold = sold;
            int prevRest = rest;

            
            hold = max(prevHold, prevRest - prices[i]);//keep holding, or buy today (from rest, not sold -> cooldown)
            sold = prevHold + prices[i]; //profit = when -price bought + price today
            rest = max(prevRest, prevSold);  
        }
        return max(sold,rest);
    }
};
