class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()

        def dfs(selected, curr):
            #print(nums, selected, curr)
            if curr == 0:
                print(selected, curr)
                a = tuple(sorted(selected))
                if a not in ans:
                    ans.add(a)
                return
            if curr < 0:
                return
            for i, num in enumerate(nums):
                dfs(selected + [num], curr - num)
            

        dfs([], target)
        return [list(a) for a in ans]