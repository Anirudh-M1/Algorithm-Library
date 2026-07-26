class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        counts = defaultdict(int)
        dependants = defaultdict(list)

        for dep, req in prerequisites:
            dependants[req].append(dep)
            counts[dep] += 1
        
        queue = deque()
        for i in range(numCourses): 
            if not i in counts:
                queue.append(i)
            
        while queue:
            req = queue.popleft()

            for dep in dependants[req]:
                counts[dep] -= 1
                if counts[dep] == 0: 
                    del counts[dep]
                    queue.append(dep)
        
        if counts:
            return False
        else:
            return True