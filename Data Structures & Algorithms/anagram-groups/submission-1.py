class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            sS = ''.join(sorted(s))
            if sS in ans:
                ans[sS].append(s)
            else:
                ans[sS] = [s]
        return [val for key, val in ans.items()]