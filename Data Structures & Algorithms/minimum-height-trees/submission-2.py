class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [i for i in range(0, n)]
        degree = collections.defaultdict(list)
        for ai, bi in edges:
            degree[ai].append(bi)
            degree[bi].append(ai)

        visited = set()
        def dfs(curr):
            if curr in visited:
                return 0             
            ret = 0
            visited.add(curr)
            for child in degree[curr]:
                ret = max(1+dfs(child), ret)

            visited.remove(curr)
            return ret

        helper = []
        heapq.heapify(helper)
        for node in degree:
            visited.clear()
            h = dfs(node)
            heapq.heappush(helper, [h, node])

        h1, n1 = heapq.heappop(helper)
        ans = [n1]

        while True:
            if not helper:
                return ans
            h, n = heapq.heappop(helper)
            if h == h1:
                ans.append(n)
            else:
                return ans

        