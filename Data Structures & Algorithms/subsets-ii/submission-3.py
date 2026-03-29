class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        cache = set()
        def dfs(idx, a):
            if idx > len(nums) - 1:
                aa = tuple(a)
                ans.add(aa)
                return
            dfs(idx + 1, a)
            dfs(idx + 1, a+ [nums[idx]] )
        nums.sort()
        dfs(0, [])
        return [list(a) for a in ans]