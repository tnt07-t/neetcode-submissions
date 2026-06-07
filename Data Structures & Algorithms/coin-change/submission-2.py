class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        #amounts reachable w/ n coins
        q = deque([0])

        #array of values seen [0...amount]
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0


        while q:
            res += 1
            for i in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1