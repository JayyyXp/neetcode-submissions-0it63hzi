class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = collections.defaultdict(list)
        for p,(s,e) in zip(succProb, edges):
            adj[s].append([p,e])
            adj[e].append([p,s])

        h = [[-1, start_node]]
        visited = set()
        while h:
            p, node = heapq.heappop(h)
            if node == end_node:
                return -p
            if node in visited:
                continue
            visited.add(node)
            for np,nn in adj[node]:
                heapq.heappush(h, [p*np ,nn])
        return 0.0