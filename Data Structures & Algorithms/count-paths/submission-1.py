class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numWays = defaultdict(int)
        directions = [(1,0),(0,1)]
        q = deque()
        q.append((0,0))
        numWays[(0,0)] = 1
        
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in numWays:
                    q.append((nr,nc))
                    numWays[(nr,nc)] = (numWays[(nr-1,nc)] if nr-1>=0 else 0) + (numWays[(nr,nc-1)] if nc-1>=0 else 0)
        
        return numWays[(m-1,n-1)]

            
                