class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses that depend on a course
        depmap = defaultdict(list)
        # number of prereqs a course has
        inCount = defaultdict(int)

        for dep, req in prerequisites:
            depmap[req].append(dep)
            inCount[dep] += 1
        
        queue = deque()
        for c in range(numCourses): 
            if c not in inCount: 
                queue.append(c)
        
        ans = []
        while queue:
            req = queue.popleft()
            ans.append(req)
            for dep in depmap[req]: 
                inCount[dep] -= 1 
                if inCount[dep] == 0:
                    queue.append(dep) 
                    del inCount[dep]
        
        
        return ans if len(inCount) == 0 else []
        

            

        

