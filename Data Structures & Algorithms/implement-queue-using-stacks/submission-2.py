class MyQueue:

    def __init__(self):
        self.fifo = []        

    def push(self, x: int) -> None:
        self.fifo.append(x)

    def pop(self) -> int:
        ans = self.fifo[0]
        self.fifo = self.fifo[1:]
        return ans        

    def peek(self) -> int:
        return self.fifo[0]

    def empty(self) -> bool:
        return len(self.fifo) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()