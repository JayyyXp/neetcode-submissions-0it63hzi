class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # ['JFK', 'ANU', 'EZE', 'AXA', 'TIA', 'ANU', 'JFK', 'TIA', 'JFK']
        # ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]

        helper = collections.defaultdict(list)
        for flightStart, flightEnd in tickets:
            helper[flightStart].append(flightEnd)

        for flightStart in helper:
            helper[flightStart].sort() 
        #print(len(tickets))
        #print(helper)

        ans = []
        usedPath = set()
        def dfs(path):
            #print(path)
            if len(path) == len(tickets) + 1:
                ans.append(path)
                return path
                        
            for i, nextStop in enumerate(helper[path[-1]]):
                if (path[-1], i) not in usedPath:
                    usedPath.add((path[-1], i))
                    res = dfs(path + [nextStop])
                    if len(res) == len(tickets) + 1:
                        return res 
                    usedPath.remove((path[-1], i))
            return []
        dfs(["JFK"])
        #print(ans)
        return sorted(ans)[0]