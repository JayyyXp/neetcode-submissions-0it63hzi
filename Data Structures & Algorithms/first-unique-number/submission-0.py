class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums
        self.uniqIdx = 0
        self.uniq = Counter(nums)

    def showFirstUnique(self) -> int:
        while self.uniqIdx < len(self.q) and self.uniq[self.q[self.uniqIdx]] != 1:
            self.uniqIdx += 1
        if self.uniqIdx == len(self.q):
            return -1
        return self.q[self.uniqIdx]

    def add(self, value: int) -> None:
        self.q.append(value)
        self.uniq[value] += 1 




# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
