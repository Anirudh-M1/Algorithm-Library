class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        dependants = defaultdict(list)
        for dep, req in prerequisites:
            dependants[req].append(dep)
            counts[dep] += 1 
        
        queue = deque()
        ans = []
        for i in range(numCourses): 
            if i not in counts:
                queue.append(i)
        

        while queue:
            c = queue.popleft()
            ans.append(c)

            for d in dependants[c]:
                counts[d] -= 1
                if counts[d] == 0:
                    queue.append(d)
                    del counts[d]
        
        print(counts)
        if counts:
            return []
        else:
            return ans


            