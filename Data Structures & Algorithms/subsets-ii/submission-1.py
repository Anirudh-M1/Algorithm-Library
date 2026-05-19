class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()
        def dfs(i, subset): 
            if i == len(nums):
                res.add(tuple(subset.copy()))
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(i+1,subset)


        dfs(0, [])
        res = [list(tup) for tup in res]
        return res