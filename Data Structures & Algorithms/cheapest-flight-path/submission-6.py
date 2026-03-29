class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        costs = [float('inf')] * n
        costs[src] = 0
        
        for _ in range(k+1):
            print(costs)
            tmp = list(costs)
            for fromI, toI, priceI in flights:
                if costs[fromI] == float('inf'):
                    continue    
                tmp[toI] = min(tmp[toI],costs[fromI] + priceI)
            costs = list(tmp)
        print(costs)
        return -1 if costs[dst] == float('inf') else costs[dst]