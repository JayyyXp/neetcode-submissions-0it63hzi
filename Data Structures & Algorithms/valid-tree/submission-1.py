class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        helper = defaultdict(list)
        for s, e in edges:
            helper[s].append(e)
            helper[e].append(s)
        print(helper)    

        canGetToAll = False
        def dfs(curr):
            if not curr:
                True
            if curr in seen:
                return False
            seen.add(curr)
            res = True
            for e in helper[curr]:
                if (curr, e) in edgesUsed:
                    continue
                edgesUsed.add((curr, e))
                edgesUsed.add((e, curr))
                if not dfs(e):
                    res = False
            return res


        for node in range(n):
            seen = set()
            edgesUsed = set()
            if not dfs(node):
                return False
            if len(seen) == n:
                canGetToAll = True
        
        return canGetToAll