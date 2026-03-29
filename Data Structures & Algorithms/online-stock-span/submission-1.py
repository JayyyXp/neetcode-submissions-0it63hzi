class StockSpanner:

    def __init__(self):
        self.l = []
        
    def next(self, price: int) -> int:
        self.l.append(price)
        l = len(self.l) -1
        i = l
        while self.l[i] <= price and i > -1:
            i -= 1

        return l - i


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)