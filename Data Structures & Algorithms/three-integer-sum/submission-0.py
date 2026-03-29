class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        def dfs(available, chosen, s):
            if len(chosen) == 3:
                if s == 0:
                    a = tuple(sorted(chosen))
                    if a not in ans:
                        ans.add(a)
                return
             
            for i, a in enumerate(available):
                dfs(available[:i] + available[i+1:], chosen + [a], s + a)

        dfs(nums, [], 0)
        return [list(a) for a in ans]