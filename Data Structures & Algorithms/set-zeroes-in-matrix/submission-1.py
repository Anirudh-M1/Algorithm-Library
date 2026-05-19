class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                if matrix[i][j]== 0: 
                    for r in range(len(matrix)): 
                        matrix[r][j] = 0 if matrix[r][j] == 0 else -1
                    for c in range(len(matrix[0])): 
                        matrix[i][c] = 0 if matrix[i][c] == 0 else -1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                if matrix[i][j] == -1: 
                    matrix[i][j] = 0
