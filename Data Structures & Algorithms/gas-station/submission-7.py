class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        def travel(tank, i):
            newTank = tank - cost[i]
            if newTank < 0:
                return -1, i
            else:
                newStation = (i + 1) % (len(gas))
                newTank += gas[newStation]
                return newTank, newStation
        #for i, station in enumerate(gas):
        #    tank = station
        #    curr = i
        #    counter = 0
        #    while True:
        #        print(i, tank, curr)
        #        tank, curr = travel(tank, curr)
        #        print(i, tank, curr)
        #        counter += 1
        #        if tank < 0 or counter == len(gas):
        #            break
        #    if counter == len(gas) and tank > 0:
        #        return i

        diff = [
            g - c
            for g, c in zip(gas, cost)
        ]
        ans = 0
        t = 0
        for i, d in enumerate(diff):
            t += d
            if t < 0:
                t = 0
                ans = i + 1
        return ans