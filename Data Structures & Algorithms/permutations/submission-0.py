class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(available, selected):
            if len(selected) == len(nums):
                ans.append(selected)
                return
            for i, n in enumerate(available):
                dfs(available[:i] + available[i+1:], selected + [n])
        dfs(nums, [])
        return ans