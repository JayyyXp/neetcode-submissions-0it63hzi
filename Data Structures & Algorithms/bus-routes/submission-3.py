from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # stop -> buses
        adj = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                adj[stop].append(bus)

        q = deque([source])
        seen_stop = {source}
        seen_bus = set()
        changes = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return changes

                for bus in adj[cur]:
                    if bus in seen_bus:
                        continue
                    seen_bus.add(bus)

                    for nxt in routes[bus]:
                        if nxt not in seen_stop:
                            seen_stop.add(nxt)
                            q.append(nxt)
            changes += 1

        return -1
