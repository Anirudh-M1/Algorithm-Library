class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Planning 
        # Fleet occurs when previous car gets to me before I get to target, 
        # speed = distance/time
        # distance / speed = time

        # (target - position) / mySpeed > (target - prevCarPosition)/prevCarSpeed , prev car joins my fleet 
        # we should start at the end of the array to avoid double, triple... merges


        cars = [[position[car],speed[car]] for car in range(len(position))]
        cars.sort()
        fleets = 1
        
        numCars = len(cars)
        prevFleetTime = (target - cars[-1][0])/cars[-1][1]

        for c in range(numCars -2, -1, -1): 
            p,s = cars[c]
            curCarTime = (target - p)/s

            if curCarTime > prevFleetTime:
                fleets+=1
                prevFleetTime = curCarTime

        return fleets