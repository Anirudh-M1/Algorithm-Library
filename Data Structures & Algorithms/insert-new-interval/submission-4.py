class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        newS, newE = newInterval
        ans = []
        for s,e in intervals: 
            if e < newS:
                ans.append([s,e])
            
            if s <= newS <= e:
                start = s 

            if s <= newE <= e:
                end = e
        
        ans.append([start, end])

        for s,e in intervals: 
            if s > newE:
                ans.append([s,e])

        return ans