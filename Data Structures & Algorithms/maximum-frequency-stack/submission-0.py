class FreqStack:

    def __init__(self):
        self.helpMap = collections.defaultdict(int)
        self.stack = []
        

    def push(self, val: int) -> None:
        self.helpMap[val] += 1
        self.stack.append(val)
        
    def pop(self) -> int:
        ans = set()
        helper = -1
        print(self.helpMap)
        print(self.stack)
        for val, freq in self.helpMap.items():
            if freq > helper:
                ans = set()
                ans.add(val)
                helper = freq
            elif freq == helper:
                ans.add(val)
        print(ans)
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] in ans:
                ret = self.stack[i]
                self.helpMap[ret] -=1

                self.stack = self.stack[:i] + self.stack[i+1:]
                return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()