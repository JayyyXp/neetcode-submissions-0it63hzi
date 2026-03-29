class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        mapHelp = {}
        for time in times:
            org = time[0]
            neig = time[1]
            t = time[2]
            if org in mapHelp:
                mapHelp[org].append([neig, t])
            else:
                mapHelp[org] = [[neig, t]]
        print(mapHelp)
        timeMap = {node: float("inf") for node in range(1, n + 1)}
        def dfs(curr, time):

            if time >= timeMap[curr]:
                return
            timeMap[curr] = time
            if curr not in mapHelp:
                return
            print(curr)
            for n, t in mapHelp[curr]:
                dfs(n, time + t)
        
        dfs(k, 0)
        ans = max(timeMap.values())
        return -1 if ans == float('inf') else ans

        