class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return ans 
            matching = strs[0][i]
            for s in strs[1:]:
                if i >= len(s):
                    return ans 
                if s[i] != matching:
                    return ans
            ans += matching 
            i += 1