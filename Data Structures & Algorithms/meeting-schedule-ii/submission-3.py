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

        for i in intervals:
            timestamps.append([i.start, "s"])
            timestamps.append([i.end, "e"])

        timestamps.sort()
    
        minRooms = 0
        concurrentRooms = 0
        for t in timestamps:
            if t[1] == "s":
                concurrentRooms+=1
                minRooms = max(concurrentRooms, minRooms)
            else: 
                concurrentRooms-=1


        return (minRooms)



