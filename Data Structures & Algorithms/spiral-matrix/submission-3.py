class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visited = set()
        i, j = 0, 0
        visited.add((i,j))
        ans = []
        ans.append(matrix[i][j])
        while len(visited) != len(matrix) * len(matrix[0]): 
            
            while j + 1 < len(matrix[0]) and (i,j + 1) not in visited: 
                j = j + 1
                visited.add((i,j))
                ans.append(matrix[i][j])


            while i + 1 < len(matrix) and (i+ 1,j) not in visited: 
                i  = i + 1
                visited.add((i,j))
                ans.append(matrix[i][j])


            while j - 1 >= 0 and (i,j - 1) not in visited: 
                j  = j - 1
                visited.add((i,j))
                ans.append(matrix[i][j])


            while i - 1 >= 0 and (i - 1,j) not in visited: 
                i  = i - 1
                visited.add((i,j))
                ans.append(matrix[i][j])


        return ans

        
        