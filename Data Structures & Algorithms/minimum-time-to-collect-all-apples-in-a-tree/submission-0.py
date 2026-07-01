class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        nodes = [0] * n
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)

            mark = 0
            for nxt in adj[node]:
                mark += dfs(nxt) 

            if hasApple[node]:
                mark += 1
            
            nodes[node] = mark
            visited.remove(node)
            return mark
        ret = dfs(0)
        print(nodes)
        return sum([1 for i in range(1,n) if nodes[i] >= 1])*2
                