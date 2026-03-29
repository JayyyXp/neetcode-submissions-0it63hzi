class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        helper = []
        def dfs(i):
            if len(helper) == k:
                ans.append(list(helper))
                return
            if i > n:
                return 
            helper.append(i)
            dfs(i+1)
            helper.pop()
            dfs(i+1)
        dfs(1)
        return ans