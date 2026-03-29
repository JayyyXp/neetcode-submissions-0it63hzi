class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 # word1 pointer
        j = 0 # word2 pointer
        select = True # T == word1 and F == word2
        ans = ""
        while i < len(word1) and j < len(word2):
            if select:
                ans += word1[i]
                i += 1
                select = False
            else:
                ans += word2[j]
                j += 1
                select = True
        while i < len(word1):
            ans += word1[i]
            i += 1
        while j < len(word2):
            ans += word2[j]
            j += 1
        return ans
