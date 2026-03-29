class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), key=lambda x: -x[0])

        for i, (pos, speed) in enumerate(cars):
            dist = target - pos
            time = dist / speed
            cars[i] = (pos, speed, time)
        print(cars)
        fleetNum = 1
        prevTime = cars[0][2] 
        for i in range(1, len(cars)):
            if cars[i][2] > prevTime:
                fleetNum += 1
                prevTime = cars[i][2]
        return fleetNum
