class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for p in prerequisites:
            preMap[p[0]].append([p[1]])

        visited = set()
        self.canfin = True


        def dfs(i): 
            if preMap[i] == []: 
                return True
            
            if i in visited:
                self.canfin = False
                return False
            
            visited.add(i)

            for j in preMap[i]: 
                if dfs(j[0]): 
                    preMap[i].remove(j)
        
            visited.remove(i)


        for p in range(numCourses):
            dfs(p)

        return self.canfin
