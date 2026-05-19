class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()

        def dfs (subset, remaining, i): 
            if remaining == 0:
                ans.add(tuple(subset.copy()))
                return 
            if i == len(candidates) or remaining < 0: 
                return

            subset.append(candidates[i])
            dfs(subset, remaining - candidates[i], i + 1)

            subset.pop()
            dfs(subset, remaining, i + 1)

        dfs([], target, 0)
        return [list(a) for a in ans]
            