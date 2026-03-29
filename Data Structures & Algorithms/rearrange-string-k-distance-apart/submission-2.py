class Solution:
    def rearrangeString(self, s: str, k: int) -> str:

        h = [(-count,c) for c,count in Counter(s).items()]
        
        heapq.heapify(h)

        q = []
        ans = []
        while h or q:
            # add cool down out here
            toDel = []
            for i in range(len(q)):
                if q[i][0] - 1 == 0:
                    heapq.heappush(h, (q[i][1], q[i][2]))
                    toDel.append(i)
                else:
                    q[i][0] -= 1
            for i in toDel:
                q.pop(i)
            #print(ans, h, q)
            if len(h) == 0:
                break
            count,c = heapq.heappop(h)
            ans.append(c)

            # add to cool-down
            count += 1
            if count < 0:
                if k > 0:
                    q.append([k, count, c])
                else:
                    heapq.heappush(h, (count, c))
        if len(ans) == len(s):
            return "".join(ans)
        return ""

