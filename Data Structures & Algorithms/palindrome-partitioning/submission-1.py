class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        def dfs(i): 
            if i == len(s): 
              ans.append(part.copy())
              return
            
            for j in range(i, len(s)): 
                if self.isPalendrome(s[i:j+1]): 
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
                
            
        dfs(0)

        return ans


    def isPalendrome(self, string): 
        l, r = 0, len(string) - 1

        while l <= r: 
            if string[l] != string[r]: 
                return False
            l +=1
            r -=1

        return True
    