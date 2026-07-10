class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount+1, 0); //ways to reach a value, [0,amount]
        dp[0] = 1;

        for (int coin : coins){
            for (int j = coin; j <= amount; j++){
                dp[j] += dp[j-coin];//for each amt, numways to reach it is added by j-coin
            }
        }
        return dp[amount];

        
    }
};
