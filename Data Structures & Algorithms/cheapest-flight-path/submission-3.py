class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        for _ in range(k+1):
            temp = costs.copy()
            for s, d, p in flights:
                if costs[s] == float('inf'):
                    continue
                if costs[s] + p < temp[d]:
                    temp[d] = costs[s] + p 
            costs = temp

        return -1 if costs[dst] == float('inf') else costs[dst]