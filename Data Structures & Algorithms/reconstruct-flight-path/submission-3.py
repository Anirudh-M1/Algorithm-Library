class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s,d in tickets: 
            adj[s].append(d)
        
        for s in adj.keys():
            adj[s].sort(reverse = True)

        ans = []
        def dfs(s): 
            while adj[s]:
                nextdest = adj[s].pop()
                dfs(nextdest)

            ans.append(s)

        dfs("JFK")

        return ans[::-1]
