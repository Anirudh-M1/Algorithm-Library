class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        

        while queue:
            req = queue.popleft()

            for dep in depmap[req]: 
                inCount[dep] -= 1 
                if inCount[dep] == 0:
                    queue.append(dep) 
                    del inCount[dep]
        
        
        return len(inCount) == 0
        

            

        

