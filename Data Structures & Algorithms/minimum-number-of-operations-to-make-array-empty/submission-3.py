class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            if c % 3 == 0:
                ans += c // 3
            elif c % 3 == 1:
                ans += c // 3 + 1  # one group of 3 becomes two 2s
            else:  # % 3 == 2
                ans += c // 3 + 1

        return ans