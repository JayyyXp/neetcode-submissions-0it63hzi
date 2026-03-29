class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def wrapper(idx, maxi):
            cache = {}
            def dfs(idx, maxi):
                if idx < 0 or idx > maxi:
                    return 0
                if idx in cache:
                    return cache[idx]

                ans = max(
                    nums[idx] + dfs(idx + 2, maxi),
                    dfs(idx + 1, maxi)
                )
                print(ans)
                cache[idx] = ans
                return ans
            return dfs(idx,maxi)
        return max(wrapper(0, len(nums)-2), wrapper(1, len(nums)-1))