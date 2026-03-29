class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        helper = {}
        for s, d, p in flights:
            if s in helper:
                helper[s].append([d, p])
            else:
                helper[s] = [[d, p]]
        visited = set()
        ans = [float('inf')]
        def dfs(curr, amount, nFlights):
            print(curr, amount, nFlights)
            if curr == dst:
                ans[0] = min(ans[0], amount)
                return 
            if nFlights == -1:
                return
            #if curr in visited:
            #    return
            if curr in helper:
                for d, p in helper[curr]:
                    dfs(d, amount + p, nFlights - 1)
            visited.add(curr)

        dfs(src, 0, k)
        return ans[0] if ans[0] != float('inf') else -1  