"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        
        points = []

        for tup in intervals: 
            points.append((tup.start, 2))
            points.append((tup.end, 1))
        
        #  (10,2), (20, 1), (0, 2), (10, 1)
        points.sort()
        # (0, 2), (10, 1), (10, 2), (20, 1)
        minRooms = 0 
        counter = 0
        for p in points:
            if p[1] == 2: 
                counter+=1
                minRooms = max(counter, minRooms)
            else: 
                counter -=1
        
        return minRooms
            
