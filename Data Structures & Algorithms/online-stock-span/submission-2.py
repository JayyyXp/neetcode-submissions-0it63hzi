class StockSpanner:

    def __init__(self):
        self.l = [] # p, s
        
    def next(self, price: int) -> int:
        i = len(self.l) -1
        span = 1
        while self.l and self.l[-1][0] <= price:
            p, s = self.l.pop()
            span += s

        self.l.append([price,span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)