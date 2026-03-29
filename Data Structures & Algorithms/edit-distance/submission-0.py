class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i,j) in cache:
                return cache[(i,j)]
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            ret = min(
                # insert
                dfs(i, j + 1) + 1,
                # delete
                dfs(i + 1, j) + 1,
                # replace
                dfs(i + 1, j + 1) + 1
            )
            cache[(i,j)] = ret
            return ret


        return dfs(0, 0)