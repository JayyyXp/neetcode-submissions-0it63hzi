class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        cache = set()
        def dfs(idx, a):
            if idx > len(nums) - 1:
                aa = tuple(sorted(a))
                ans.add(aa)
                return
            dfs(idx + 1, a)
            dfs(idx + 1, a+ [nums[idx]] )

        dfs(0, [])
        return [list(a) for a in ans]