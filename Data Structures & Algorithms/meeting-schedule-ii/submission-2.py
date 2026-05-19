"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        timestamps = []
        for interval in intervals:
            timestamps.append([interval.start, "s"])
            timestamps.append([interval.end, "e"])

        timestamps.sort()

        maxConCt = 0 
        curConCt = 0 

        for t in timestamps: 
            if t[1] == "s": 
                curConCt += 1 
                maxConCt = max(maxConCt, curConCt)
            else:
                curConCt -= 1


        return maxConCt