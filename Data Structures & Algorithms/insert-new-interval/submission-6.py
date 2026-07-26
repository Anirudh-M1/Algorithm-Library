class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervalIdx = 0
        ans = []
        while intervalIdx < len(intervals) and intervals[intervalIdx][1] < newInterval[0]:
            ans.append(intervals[intervalIdx])
            intervalIdx +=1
        

        while intervalIdx < len(intervals) and intervals[intervalIdx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[intervalIdx][0])
            newInterval[1] = max(newInterval[1],intervals[intervalIdx][1])
            intervalIdx +=1
            
        
        ans.append(newInterval)

        while intervalIdx < len(intervals):
            ans.append(intervals[intervalIdx])
            intervalIdx +=1
        return ans
