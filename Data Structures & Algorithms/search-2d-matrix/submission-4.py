class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r: 
            m = int((l + r)/2) 

            if matrix[m][0] <= target <= matrix[m][len(matrix[0]) - 1]: 
                ans = self.binarySearch(matrix[m], target)
                return ans 
            elif target < matrix[m][0]: 
                r = m - 1
            else: 
                l = m + 1
            
        return False

    def binarySearch(self, array, target): 
        print(f"binary search on {array}")
        l, r = 0, len(array) - 1

        while l <=r: 
            m = int((l+r)/2)

            if array[m] == target: 
                return True
            elif target<array[m]: 
                r = m - 1
            else: 
                l = m + 1

        return False
        
                