class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        llen = len(self.low)
        hlen = len(self.high)
        if llen + 1 == hlen:
            hmax = self.high[0]
            if num > hmax:
                h = heapq.heappop(self.high)
                heapq.heappush(self.low, -h)
                heapq.heappush(self.high, num)
            else:
                heapq.heappush(self.low, -num)
        
        elif hlen + 1 == llen:
            lmax = -self.low[0]
            if num < lmax:
                l = -heapq.heappop(self.low)
                heapq.heappush(self.high, l)
                heapq.heappush(self.low, -num)
            else:
                heapq.heappush(self.high, num)
        else:
            if not self.low:
                heapq.heappush(self.low, -num)
            else:
                lmax = -self.low[0]
                if num <= lmax:
                    heapq.heappush(self.low, -num)
                else:
                    heapq.heappush(self.high, num)

    def findMedian(self) -> float:
        llen = len(self.low)
        hlen = len(self.high)
        if llen == hlen:
            return (-self.low[0] + self.high[0]) / 2
        elif llen > hlen:
            return -self.low[0]
        else:
            return self.high[0]
        