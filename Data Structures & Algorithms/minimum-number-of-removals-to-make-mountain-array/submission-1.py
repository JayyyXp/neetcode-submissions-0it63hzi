class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        import bisect
        llis = []
        LIS = []
        for n in nums:
            i = bisect.bisect_left(LIS, n)
            if i == len(LIS):
                LIS.append(n)
            else:
                LIS[i] = n
            llis.append(i)
        
        rlis = []
        LIS = []
        for n in reversed(nums):
            i = bisect.bisect_left(LIS, n)
            if i == len(LIS):
                LIS.append(n)
            else:
                LIS[i] = n
            rlis.append(i)
        rlis.reverse()
        
        return len(nums) - max(l+r+1 for l,r in zip(llis,rlis) if l > 0 and r > 0)

         