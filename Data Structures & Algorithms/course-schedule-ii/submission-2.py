class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]        
        for d,s in prerequisites: 
            adj[s].append(d)

        ans = []
        visit = [0]*numCourses
        def dfs(courses): 
            nonlocal ans
            if visit[courses] == 1: 
                return False
            if visit[courses] == 2: 
                return True

            visit[courses] = 1 
            
            for nxt_course in adj[courses]: 
                if not dfs(nxt_course): 
                    return False

            visit[courses] = 2
            ans.append(courses)
            return True

        for i in range(numCourses): 
            if not dfs(i): 
                return []
        return ans[::-1]