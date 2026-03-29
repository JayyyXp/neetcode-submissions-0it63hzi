class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for ai, bi in prerequisites:
            adj[ai].append(bi)
        memo = {}
        def dfs(curr, target):
            if curr == target:
                return True
            if (curr, target) in memo:
                return memo[(curr, target)]
            for nxt in adj[curr]:
                if dfs(nxt, target):
                    memo[(curr, target)] = True
                    return True
            memo[(curr, target)] = False
            return False
        ans = [False] * len(queries)
        for i,(ai,bi) in enumerate(queries):
            if dfs(ai,bi):
                ans[i] = True
        return ans
            