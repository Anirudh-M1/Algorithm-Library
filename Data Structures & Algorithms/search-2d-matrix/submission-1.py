class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lmatrix, rmatrix = 0 , len(matrix) - 1

        while lmatrix <= rmatrix: 
            midMatrix = (lmatrix + rmatrix)//2

            if target <=  matrix[midMatrix][-1] and target >= matrix[midMatrix][0]:
                return self.binarySearch(matrix[midMatrix], target)

            elif target > matrix[midMatrix][-1]:
                lmatrix = midMatrix + 1 
            
            elif target < matrix[midMatrix][-1]: 
                rmatrix = midMatrix - 1
        
        return False
    
    def binarySearch(self, array: List[int], target: int) -> bool:        
        larray, rarray = 0, len(array) - 1
        while larray <= rarray: 
            midArray = (larray + rarray)//2

            if target == array[midArray]:
                return True

            elif target > array[midArray]:
                larray = midArray + 1 
            
            elif target < array[midArray]: 
                rarray = midArray - 1

        return False
