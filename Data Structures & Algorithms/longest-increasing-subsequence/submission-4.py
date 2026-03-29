class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        ans = []
        for n in nums:

            if not ans or n > ans[-1]:
                ans.append(n)
            else:
                idx = bisect.bisect_left(ans, n)
                #print(ans, n, idx)
                ans[idx] = n
        return len(ans)