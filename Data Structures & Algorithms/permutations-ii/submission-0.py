class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        def dfs(available, ret):
            if len(available) == 0:
                ans.add(tuple(ret))
                return
            for i, n in enumerate(available):
                dfs(available[:i]+available[i+1:], ret + [n])
        dfs(nums, [])
        return [list(s) for s in ans]

