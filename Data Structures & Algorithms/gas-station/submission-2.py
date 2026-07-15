class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy -> if start ... i fails, then any point 
        # j in range [start,i] is also invalid starting point
        tot = sum(gas) - sum(cost)
        tank = 0
        index = 0 

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            if tank < 0:
                index = i + 1 #start out of invalid range
                tank = 0
        
        return index if tot >= 0 else -1