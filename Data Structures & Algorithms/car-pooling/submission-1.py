class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1]) # sort by start location
        print(trips)
        car = []
        heapq.heapify(car)
        curPassanger = 0
        for numPassengers, fromI, toI in trips:
            # empty the car of passangers that have already
            # gotten off
            while len(car) > 0 and car[0][0] <= fromI:
                _, offPass = heapq.heappop(car)
                curPassanger -= offPass
                print(curPassanger, offPass)
            # add the new passangers
            curPassanger += numPassengers
            print(curPassanger)
            if curPassanger > capacity:
                return False
            heapq.heappush(car, [toI, numPassengers])
        return True
            