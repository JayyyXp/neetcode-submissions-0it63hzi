
class MyCircularQueue:
    class LinkedList:
        def __init__(self, val, nxt=None):
            self.val = val
            self.nxt = nxt # another LinkedList object

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.n = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.LinkedList(value)
            self.tail = self.head 
        else:
            newTail = self.LinkedList(value)
            self.tail.nxt = newTail
            self.tail = newTail
        self.n += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        newHead = self.head.nxt
        self.head = newHead
        self.n -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()