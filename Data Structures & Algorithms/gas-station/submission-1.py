class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = 0
        res = 0
        tot_gas = tot_cost = 0
        for i in range(len(gas)):
            tot_gas += gas[i]
            tot_cost += cost[i]
            curr = curr + gas[i] - cost[i]
            if curr < 0:
                res = i + 1
                curr = 0
        
        return res if tot_gas >= tot_cost else -1