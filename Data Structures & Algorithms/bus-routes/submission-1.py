class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj = defaultdict(list)
        routes = {i: set(route) for i, route in enumerate(routes) }
        print(routes)
        q = deque()
        visited = set()
        target_routes = set()
        for route1, stops1 in routes.items():
            if source in stops1:
                q.append([route1, 1])
                visited.add(route1)
            if target in stops1:
                target_routes.add(route1)

            for route2, stops2 in routes.items():
                if route1 == route2:
                    continue                
                if stops1 & stops2:
                    adj[route1].append(route2)

        print(adj)

        while q:
            route, changes = q.popleft()
            if route in target_routes:
                return changes

            for nxt in adj[route]:
                if (
                    nxt not in visited
                ): 
                    visited.add(nxt)
                    q.append([nxt, changes + 1])

        return -1