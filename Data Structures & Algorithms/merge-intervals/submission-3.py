class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort(key = lambda x:x[0])
        if intervals: 
            start = intervals[0][0]
            end = intervals[0][1]
        else: 
            return ans

        i = 0 
        while i < len(intervals): 
            if intervals[i][0] <= end:
                end = max(end,intervals[i][1])
                start= min(start, intervals[i][0])
            else:
                ans.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
            i+=1 

        ans.append([start,end])
        return ans