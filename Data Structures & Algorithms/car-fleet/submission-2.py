class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        for i, (p, sp) in enumerate(zip(position, speed)): 
            fleets.append((i,sp,p))
        
        fleets.sort(key = lambda x :x[2])
        counter = 0
        while fleets: 
            curFleet = fleets.pop()
            curFleetPos = curFleet[2]
            curFleetSpeed =  curFleet[1]
            if fleets: 
                nextFleet = fleets.pop()
                nextFleetPos = nextFleet[2]
                nextFleetSpeed =  nextFleet[1]

                # If the car behind takes LESS or EQUAL time, it merges
                if (target - nextFleetPos) / nextFleetSpeed <= (target - curFleetPos) / curFleetSpeed:
                    # It merges into curFleet (the one ahead), so we put curFleet back
                    fleets.append(curFleet)
                else: 
                    # It cannot catch up, so curFleet is officially a finished fleet
                    counter += 1
                    fleets.append(nextFleet)
            else:
                # If there are no more cars to compare, this is the final fleet
                counter += 1
        return counter