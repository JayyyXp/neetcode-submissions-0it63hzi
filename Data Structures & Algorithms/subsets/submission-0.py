class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        helper = []

        def dfs(idx):
            if idx == len(nums):
                ans.append(list(helper))
                return
            helper.append(nums[idx])
            dfs(idx+1)
            helper.pop()
            dfs(idx+1)

        dfs(0)
        return ans