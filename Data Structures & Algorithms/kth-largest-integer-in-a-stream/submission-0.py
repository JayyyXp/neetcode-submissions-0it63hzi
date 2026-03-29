class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.stream.append(val)
        s = sorted(self.stream)
        return s[-self.k] 
        
