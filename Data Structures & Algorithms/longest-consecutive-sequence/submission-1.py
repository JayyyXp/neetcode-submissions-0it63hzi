class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSorted = sorted(set(nums))

        ans = 1
        cand = 1
        print(numsSorted)
        for num1, num2 in zip(numsSorted[:-1], numsSorted[1:]):
            if num2 - num1 == 1:
                cand += 1
                ans = max(ans, cand)
            else:
                cand = 1

        return ans