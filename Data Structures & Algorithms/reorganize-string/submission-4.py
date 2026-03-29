class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] -= 1
        ret = ""
        counter = [[count, c] for c, count in counter.items()]
        heapq.heapify(counter)
        hold = None
        while counter:
            print(hold)
            count, c = heapq.heappop(counter)
            ret += c
            count += 1
            if hold is not None and hold[0] != 0:
                heapq.heappush(counter, hold)
            hold = [count, c]
        if len(ret) == len(s):
            return ret
        return ""