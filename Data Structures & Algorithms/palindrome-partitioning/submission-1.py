class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # aabcb
        # abbab

        ans = []
        helper = []
        def dfs(idx):
            if idx == len(s):
                #print(l)
                ans.append(list(helper))
                return
            for j in range(idx, len(s)):
                if s[idx:j+1] == s[idx:j+1][::-1]:
                    helper.append(s[idx:j+1])
                    dfs(j+1)
                    helper.pop()
        dfs(0)
        return ans 
