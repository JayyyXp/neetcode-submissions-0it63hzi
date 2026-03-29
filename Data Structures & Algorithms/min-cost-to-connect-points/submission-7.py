class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #from collections import defaultdict
        helper = collections.defaultdict(list)
        for i, (ix, iy) in enumerate(points):
            for j, (jx, jy) in enumerate(points):
                if i == j:
                    continue
                dist = abs(ix - jx) + abs(iy - jy)
                helper[i].append([dist, j])
                helper[j].append([dist, i])

        visited = set()
        ans = 0
        minHeap = [[0,0]] # [cost, pointIdx]
        heapq.heapify(minHeap)
        while len(visited) != len(points):
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            ans += cost
            visited.add(i)
            for minCost, j in helper[i]:
                if j not in visited:
                    heapq.heappush(minHeap, [minCost, j])
        return ans
