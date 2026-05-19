class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs (subset, remaining, i): 
            if remaining == 0:
                ans.append(subset.copy())
                return 
            if i == len(candidates) or remaining < 0: 
                return

            subset.append(candidates[i])
            dfs(subset, remaining - candidates[i], i + 1)

            subset.pop()
            j = i 
            while j<len(candidates) and candidates[j]== candidates[i]: 
                    j+=1

            dfs(subset, remaining, j)
            

        dfs([], target, 0)
        return ans
            