class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        prev = target[0]
        s = prev
        for i in range(1, len(target)):
            if target[i] > prev:
                s += target[i] - prev
            prev = target[i]
        return s