class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position with speed, and sort cars by starting position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd  # time for this car to reach target
            # if this car cannot catch up to the fleet ahead, it becomes a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: car merges with fleet ahead (do nothing)
        
        return len(stack)
