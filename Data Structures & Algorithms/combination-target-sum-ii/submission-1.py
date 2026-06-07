#SORT -> ACCOUNT FOR DUPLICATES
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i,curr,tot):
            if tot == target:
                res.append(curr.copy())
                return
            if tot > target or i >= len(candidates):
                return
        
            curr.append(candidates[i])
            dfs(i+1, curr, tot + candidates[i])
            
            #Not include
            curr.pop()
            while i+1<len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, curr, tot)

        dfs(0,[],0)
        return res
