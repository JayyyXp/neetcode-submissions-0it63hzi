class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), key=lambda x: -x[0])

        fleetNum = 0
        prevTime = 0 
        for pos, speed in cars:
            dist = target - pos
            time = dist / speed
            
            if time > prevTime:
                fleetNum += 1
                prevTime = time
        return fleetNum
