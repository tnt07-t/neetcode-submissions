class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        so given a list of flights (fromi, toi) -> reconstruct flight path
        only one possible ans. need smallest first

        places stopped in itinerary = num tickets + 1 (each is like an edge -> num nodes = edges + 1)

        '''
        n = len(tickets)

        graph = defaultdict(list) #airport - possibel outgoings
        for f,t in sorted(tickets, reverse = True): #descending
            graph[f].append(t)
        
        res = []
        #a node is final destination no possible outgoings
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)

        dfs("JFK")
        return res[::-1]
        

            
        
            
        

