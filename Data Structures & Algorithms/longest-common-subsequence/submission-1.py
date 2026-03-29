class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #ans = [0]
        cache = {}
        def helper(idx1, idx2):
            print(idx1, idx2)
            #idx1 = min(idx1, len(text1)-1)
            #idx2 = min(idx2, len(text2)-1)
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]
            if text1[idx1] == text2[idx2]:
                c = helper(idx1 + 1, idx2 + 1) + 1
                cache[(idx1, idx2)] = c
                return c
            else:
                c = max(
                    helper(idx1 + 1, idx2),
                    helper(idx1, idx2 + 1)
                )
                cache[(idx1, idx2)] = c
                return c
        return helper(0, 0)
        #return ans[0]
        