class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        def dfs(curr):
            ret = 0
            visited.add(curr)
            for nxt in adj[curr]:
                if nxt not in visited:
                    ret = max(ret, 1+dfs(nxt))
            visited.remove(curr)
            return ret
        
        ans = collections.defaultdict(list)
        for i in range(n):
            ans[dfs(i)].append(i)
        print(ans)

        return ans[min(ans)]