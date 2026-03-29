class ListNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.right = self.right
        self.map = {}
    
    def lenght(self): 
        return len(self.map)
    
    def pushRight(self, val): 
        node = ListNode(val, self.right.left, self.right)
        self.map[val] = node
        self.right.left = node
        node.left.right = node
    
    def pop(self, val): 
        if val in self.map:
            node = self.map[val]
            nodeLeft = node.left
            nodeRight = node.right
            nodeLeft.right = nodeRight
            nodeRight.left = nodeLeft
            self.map.pop(val, None)
    
    def popLeft(self):
        res = self.left.right.val
        self.pop(self.left.right.val)
        return res        

    def update(self, val):
        self.pop(val)
        self.pushRight(val)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.valMap = {} # Map key -> val
        self.countMap = collections.defaultdict(int) # Map key -> count
        self.listMap = collections.defaultdict(LinkedList) # Map count of key -> linkedlist

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)

        if self.lfuCnt == cnt and self.listMap[cnt].lenght() == 0:
            self.lfuCnt += 1
    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.valMap and len(self.valMap) == self.cap:
            node = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(node)
            self.countMap.pop(node)
        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)