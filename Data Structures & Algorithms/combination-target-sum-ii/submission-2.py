class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()

        def dfs(i, t): 
            if t == 0: 
                ans.append(subset.copy())
                return 
            elif t < 0 or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i + 1, t - candidates[i])

            subset.pop()
            j = i
            while candidates[j] == candidates[i]: 
                j+=1
                if j == len(candidates): 
                    break
            
            dfs(j, t)

        dfs(0 , target)
    
        return ans