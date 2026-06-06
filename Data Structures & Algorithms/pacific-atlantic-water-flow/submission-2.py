class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        def bfs(queue):
            ans = set()
            visited = set()
            for v in queue: 
                ans.add(v)
            neighbors =[(1, 0),(0,1),(-1,0), (0,-1)]
            while queue:
                    x,y = queue.popleft()
                    for r,c in neighbors:
                        xn, yn = x + r, y + c

                        if 0 <= xn< len(heights) and 0<= yn<len(heights[0]): 
                            if heights[xn][yn] >= heights[x][y] and (xn,yn) not in visited: 
                                visited.add((xn,yn))
                                ans.add((xn,yn))
                                queue.append((xn,yn))
        
            return ans
        p = deque()
        a = deque()
        for i in range(len(heights)): 
            for j in range(len(heights[0])): 
                if i == 0 or j == 0: 
                    p.append((i,j))
                
                if i == len(heights) - 1 or j == len(heights[0]) - 1: 
                    a.append((i,j))

        print(f"pasific {p}")
        print(f"atlantic {a}")

        sp = bfs(p)
        sq = bfs(a)

        ans = sp & sq

        return list(ans)


