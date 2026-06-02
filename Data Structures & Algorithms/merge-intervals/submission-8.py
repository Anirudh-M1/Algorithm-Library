class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #planing, sort by end, 
        if not intervals:
            return []

        intervals.sort(key= lambda x:(x[0], x[1]))
        print(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for i in intervals:
            if i[0] <= end:
                start = min(start, i[0])
                end = max(i[1], end)
            elif i[0] > end:
                ans.append([start, end])
                start = i[0]
                end = i[1]


        ans.append([start, end])
        return ans