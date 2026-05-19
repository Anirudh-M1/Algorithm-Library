class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0 , len(matrix) - 1

        while left <= right: 
            midArray = (left + right)//2

            if target <=  matrix[midArray][-1] and target >= matrix[midArray][0]:
                l, r = 0, len(matrix[midArray]) - 1
                while l <= r: 
                    midVal = (l + r)//2

                    if target == matrix[midArray][midVal]:
                        return True

                    elif target > matrix[midArray][midVal]:
                        l = midVal + 1 
                    
                    elif target < matrix[midArray][midVal]: 
                        r = midVal - 1

                left = right + 1

            elif target > matrix[midArray][-1]:
                left = midArray + 1 
            
            elif target < matrix[midArray][-1]: 
                right = midArray - 1
        
        return False