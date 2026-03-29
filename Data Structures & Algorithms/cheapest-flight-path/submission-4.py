class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k+1):
            temp = list(cost)
            for s,d,p in flights:
                if cost[s] == float('inf'):
                    continue
                if cost[s] + p < temp[d]:
                    temp[d] = cost[s] + p
            cost = temp
        return -1 if cost[dst] == float('inf') else cost[dst]