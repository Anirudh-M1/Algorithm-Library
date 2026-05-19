class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        for c, p in prerequisites: 
            nodes[c].append(p)

        visited = set()
        cycle = set()
        self.cyclePresent = False
        ans = []
        def dfs(node): 
            if node in visited: 
                return True
            if node in cycle: 
                self.cyclePresent = True
            if self.cyclePresent == True:
                return
            cycle.add(node)
            for preReq in nodes[node]: 
                if preReq not in visited: 
                    dfs(preReq)
            
            visited.add(node)
            ans.append(node)
            return True

        for n in range(numCourses): 
            if n not in visited: 
                dfs(n)

        return ans if self.cyclePresent == False else []
        