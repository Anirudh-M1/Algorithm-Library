class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        RowZero = False


        for r in range(len(matrix)): 
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    # regarless the first val in the row will be 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        RowZero = True
                    
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])): 
                if matrix[0][c] == 0 or matrix[r][0] == 0: 
                    matrix[r][c] = 0


        if matrix[0][0] == 0: 
            for r in range(len(matrix)):
                matrix[r][0] = 0
            
        if RowZero == True:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0 
        



        