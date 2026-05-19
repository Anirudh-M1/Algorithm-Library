class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowStr = s.lower()
        left, right = 0, len(s) - 1

        while left<=right:
            if left< len(s) and not lowStr[left].isalnum(): 
                left +=1
            elif right> -1 and not lowStr[right].isalnum(): 
                right -=1

            else:
                if lowStr[left] != lowStr[right]: 
                    print(f"missmatch, left: {lowStr[left]} right: {lowStr[right]}")
                    return False
                left+=1 
                right-=1
        
        return True
            
