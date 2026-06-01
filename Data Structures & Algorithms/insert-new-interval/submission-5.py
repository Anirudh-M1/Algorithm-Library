class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        ans = []
        for s,e in intervals: 
            if e < start:
                ans.append([s,e])
            
            if s <= start <= e:
                start = s 

            if s <= end <= e:
                end = e
        
        ans.append([start, end])

        for s,e in intervals: 
            if s > end:
                ans.append([s,e])

        return ans