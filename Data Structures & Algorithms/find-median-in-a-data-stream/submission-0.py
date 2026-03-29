class MedianFinder:

    def __init__(self):
        self.stream = []
        heapq.heapify(self.stream)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.stream, num)

    def findMedian(self) -> float:
        temp = self.stream[:]
        n = len(temp)
        if n % 2 == 0:
            first = heapq.heappop(temp)
            for i in range(1,n):
                second = heapq.heappop(temp)
                print(first, second)
                if i >= n//2:
                    return (first + second) / 2
                first = second
        else:
            for i in range(n):
                item = heapq.heappop(temp)
                if i == n//2:
                    return item
        