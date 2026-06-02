class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[1])
        deleteIntervals = 0

        start = intervals[0][0]
        end = intervals[0][1]

        for i in intervals[1:]: 
            if end > i[0]: 
                deleteIntervals+=1
            else:
                end = i[1]
        
        return (deleteIntervals)

