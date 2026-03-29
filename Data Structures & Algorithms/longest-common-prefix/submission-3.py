class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        while i < len(strs[0]):
            matching = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != matching:
                    return ans
            ans += matching 
            i += 1
        return ans 