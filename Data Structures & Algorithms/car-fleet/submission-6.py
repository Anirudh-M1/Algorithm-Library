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
        print(cars)
        fleets = 1
        
        numCars = len(cars)
        c = numCars - 2
        prevFleetTime = (target - cars[-1][0])/cars[-1][1]

        while c >= 0:
            print(f" prevFleet time: {prevFleetTime}")
            curCarTime = (target - cars[c][0])/cars[c][1]
            print(cars[c])
            print(f" cur car time: {curCarTime}")

            if curCarTime > prevFleetTime:
                print(f"new fleet for {cars[c]}")
                fleets+=1
                prevFleetTime = curCarTime
            
            c-=1 
        return fleets