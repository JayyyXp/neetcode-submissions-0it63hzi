class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        LIS = []
        for n in nums:
            i = bisect.bisect_left(LIS, n)
            if i == len(LIS):
                LIS.append(n)
            else:
                LIS[i] = n
        return len(LIS)